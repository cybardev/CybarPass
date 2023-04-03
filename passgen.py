#!/usr/bin/env python3

import argparse
import tkinter as tk
from tkinter.constants import DISABLED
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox, Frame
from types import MappingProxyType
from secrets import choice

# map of constants
CONST = MappingProxyType(
    {
        "win-title": "PassGen",
        "win-width": 450,
        "win-height": 200,
        "pass-strength": {"Low": 16, "Medium": 24, "High": 32},
    }
)


class PassGen:
    def __init__(self, filename=None, char_limit=16):
        self.char_limit = char_limit
        if filename is not None:
            self.word_list = filename

    @property
    def char_limit(self):
        return self.__char_limit

    @char_limit.setter
    def char_limit(self, value):
        if value < 16:
            print("Character limit must be at least 16 for security reasons.")
        else:
            self.__char_limit = value

    @property
    def word_list(self):
        return self.__word_list

    @word_list.setter
    def word_list(self, filename):
        with open(filename, "r") as file:
            self.__word_list = [line.strip() for line in file.readlines()]

    def __word_gen(self, word_list: list[str], char_limit: int):
        char_count = 0
        while char_count < char_limit:
            word = choice(word_list)
            char_count += len(word)
            yield word

    @property
    def passphrase(self) -> str:
        return " ".join(self.__word_gen(self.word_list, self.char_limit))


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title(str(CONST["win-title"]))
        self.geometry(f"{CONST['win-width']}x{CONST['win-height']}")
        self.resizable(False, False)


class AppFrame(Frame):
    def __init__(self, container: tk.Tk) -> None:
        self.__container = container
        super().__init__(self.__container)

        # --- variable elements --- #
        self.__passgen: PassGen = PassGen()
        self.__txt_password = tk.StringVar()
        self.__word_list_filename = tk.StringVar()

        # --- UI grid layout --- #

        # rows
        self.__container.grid_rowconfigure(0, weight=2)
        self.__container.grid_rowconfigure(1, weight=1)
        self.__container.grid_rowconfigure(2, weight=1)
        self.__container.grid_rowconfigure(3, weight=2)

        # columns
        self.__container.grid_columnconfigure(0, weight=2)
        self.__container.grid_columnconfigure(1, weight=3)
        self.__container.grid_columnconfigure(2, weight=1)

        # call UI builder methods --- #

        # passphrase
        self.lbl_password()
        self.entry_password()

        # word list
        self.lbl_word_list()
        self.entry_word_list()
        self.btn_word_list()

        # strength selector
        self.lbl_strength()
        self.combo_strength()

        # action buttons
        self.btn_generate()
        self.btn_copy()
        self.btn_clear()

        # --- render the frame --- #
        self.__container.mainloop()

    # --- password UI items --- #

    def lbl_password(self) -> None:
        self.__lbl_password = tk.Label(self.__container, text="Password:")
        self.__lbl_password.grid(row=0, column=0)

    def entry_password(self) -> None:
        self.__entry_password = tk.Entry(
            self.__container,
            textvariable=self.__txt_password,
        )
        self.__entry_password.grid(
            row=0, column=1, columnspan=2, sticky=tk.EW, padx=16
        )

    # --- word list UI items --- #

    def lbl_word_list(self) -> None:
        self.__lbl_password = tk.Label(self.__container, text="Word List:")
        self.__lbl_password.grid(row=1, column=0)

    def entry_word_list(self) -> None:
        self.__entry_word_list = tk.Entry(
            self.__container,
            textvariable=self.__word_list_filename,
            state=DISABLED,
        )
        self.__entry_word_list.grid(row=1, column=1)

    def btn_word_list(self) -> None:
        self.__btn_word_list = tk.Button(
            self.__container,
            text="Open",
            command=lambda: self.__word_file(),
        )
        self.__btn_word_list.grid(row=1, column=2, sticky=tk.W)

    # --- strength selector UI items --- #

    def lbl_strength(self) -> None:
        self.__lbl_password = tk.Label(self.__container, text="Strength:")
        self.__lbl_password.grid(row=2, column=0)

    def combo_strength(self) -> None:
        self.__strength = Combobox(self.__container, width=18)
        self.__strength["values"] = tuple(CONST["pass-strength"].keys())
        self.__strength["state"] = "readonly"
        self.__strength.current(0)
        self.__strength.grid(
            row=2, column=1, columnspan=2, sticky=tk.EW, padx=16
        )

    # --- action button group --- #

    def btn_generate(self) -> None:
        self.__btn_generate = tk.Button(
            self.__container,
            text="Generate",
            command=lambda: self.__show_pass(),
        )
        self.__btn_generate.grid(row=3, column=0, sticky=tk.E)

    def btn_copy(self) -> None:
        self.__btn_copy = tk.Button(
            self.__container,
            text="Copy",
            command=lambda: self.__copy_pass(self.__txt_password.get()),
        )
        self.__btn_copy.grid(row=3, column=1)

    def btn_clear(self) -> None:
        self.__btn_clear = tk.Button(
            self.__container,
            text="Clear",
            command=lambda: self.__clear_pass(),
        )
        self.__btn_clear.grid(row=3, column=2, sticky=tk.W)

    # --- callback methods for buttons --- #

    def __word_file(self):
        filename = askopenfilename()
        if filename:
            self.__word_list_filename.set(filename)
            self.__passgen.word_list = self.__word_list_filename.get()

    def __show_pass(self):
        self.__passgen.char_limit = CONST["pass-strength"][
            self.__strength.get()
        ]
        self.__txt_password.set(self.__passgen.passphrase)

    def __copy_pass(self, passphrase):
        if passphrase:
            self.__container.clipboard_clear()
            self.__container.clipboard_append(passphrase)

    def __clear_pass(self):
        self.__txt_password.set("")


if __name__ == "__main__":
    # argument parsing
    parser = argparse.ArgumentParser(
        description="Generate a secure passphrase",
        epilog="Launch without arguments for GUI",
        allow_abbrev=False,
    )
    parser.add_argument(
        "filename",
        help="Path to dictionary file",
        metavar="WORD_LIST",
        type=str,
        nargs="?",
        default=None,
    )
    parser.add_argument(
        "-n",
        "--len",
        help="Minimum length of passphrase",
        dest="char_limit",
        metavar="NUM",
        type=int,
        default=16,
    )
    args = parser.parse_args()

    # main program logic
    if args.filename is None:
        AppFrame(App())
    else:
        print(PassGen(args.filename, args.char_limit).passphrase)
