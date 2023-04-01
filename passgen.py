#!/usr/bin/env python3
import sys
import argparse
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox
from secrets import choice

# configuration variables
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 275
DEFAULT_FONT = "Arial"
DEFAULT_FONT_SIZE = 14
PASS_STRENGTH = {
    "Low": 16,
    "Medium": 24,
    "High": 36,
}  # strength: password length


def get_word_list(filename: str) -> list[str]:
    with open(filename, "r") as f:
        words = [line.strip() for line in f.readlines()]
    return words


def word_gen(word_list: list[str], char_limit: int):
    char_count = 0
    while char_count < char_limit:
        word = choice(word_list)
        char_count += len(word)
        yield word


def passphrase_gen(word_list: list[str], char_limit: int) -> str:
    return " ".join(word_gen(word_list, char_limit))


def word_file():
    types = (("text files", "*.txt"), ("All files", "*.*"))
    return askopenfilename(filetypes=types)


def copy_pass(passphrase, app):
    app.clipboard_clear()
    app.clipboard_append(passphrase)


# def show_pass(textbox):
#     textbox.set(passphrase_gen(PASS_STRENGTH[strength_selector.get()]))


def clear_pass(textbox):
    textbox.set("")


def create_gui():
    # initialize window
    app = tk.Tk()
    app.title("PassGen")
    app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    # --- generated password --- #

    # label
    lbl_password = tk.Label(
        app, text="Password:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE)
    )
    lbl_password.place(x=25, y=25)

    # text box
    txt_password = tk.StringVar()
    entry_result = tk.Entry(
        app,
        font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
        textvariable=txt_password,
    )
    entry_result.place(x=100, y=25)

    # --- word list to use --- #

    # label
    lbl_word_list = tk.Label(
        app, text="Word List:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE)
    )
    lbl_word_list.place(x=25, y=100)

    # text box
    word_list_filename = tk.StringVar()
    word_list_namebox = tk.Entry(
        app,
        font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
        textvariable=word_list_filename,
    )
    word_list_namebox.place(x=100, y=100)

    # button
    btn_fileopen = tk.Button(
        app,
        text="Open",
        font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
        command=lambda: word_list_filename.set(word_file()),
    )
    btn_fileopen.place(x=300, y=100)

    # -_- strength selection dropdown --- #

    # label
    lbl_strength = tk.Label(
        app, text="Strength:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE)
    )
    lbl_strength.place(x=25, y=75)

    # combo box
    strength_selector = Combobox(
        app, font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), width=18
    )
    strength_selector["values"] = tuple(
        k for k in PASS_STRENGTH.keys() if k
    )  # set non-empty values from dictionary
    strength_selector["state"] = "readonly"
    strength_selector.current(2)
    strength_selector.place(x=100, y=75)

    # --- spawn the GUI --- #
    app.mainloop()

    # exit after user quits
    sys.exit(0)


if __name__ == "__main__":
    # argument parsing
    parser = argparse.ArgumentParser(
        description="Generate a secure passphrase", allow_abbrev=False
    )
    parser.add_argument(
        "filename",
        help="Path to dictionary file",
        metavar="WORD_LIST",
        type=str,
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
    parser.add_argument(
        "-g",
        "--gui",
        help="Run the program in GUI mode",
        action="store_true",
        dest="gui_mode",
    )
    args = parser.parse_args()

    if args.gui_mode:
        create_gui()
    else:
        # print a randomly generated passphrase
        print(passphrase_gen(get_word_list(args.filename), args.char_limit))
