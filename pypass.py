#!/usr/bin/env python3
import secrets
import string
import sys
import tkinter as tk
from tkinter.ttk import Combobox
import passgen

# configuration variables
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 175
DEFAULT_FONT = "Arial"
DEFAULT_FONT_SIZE = 14
PASS_STRENGTH = {
    "Low": 8,
    "Medium": 12,
    "High": 16,
    "": 16,
}  # strength: password length


def generate_password(length: int = PASS_STRENGTH["High"]) -> str:
    """Generate a random password of the given length.

    Args:
        length (int, optional): length of password. Defaults to PASS_STRENGTH["High"].

    Returns:
        str: generated password
    """
    mixed_chars = string.digits + string.ascii_letters + string.punctuation
    return "".join([secrets.choice(mixed_chars) for _ in range(length)])


def create_gui() -> None:
    """Create a GUI window to generate password"""

    # initialize window
    screen = tk.Tk()
    screen.title("PyPass")
    screen.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    # generated password
    lbl_password = tk.Label(
        screen, text="Password:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE)
    )
    lbl_password.place(x=25, y=25)
    txt_password = tk.StringVar()
    entry_result = tk.Entry(
        screen,
        font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
        textvariable=txt_password,
    )
    entry_result.place(x=100, y=25)

    # strength selection dropdown
    lbl_strength = tk.Label(
        screen, text="Strength:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE)
    )
    lbl_strength.place(x=25, y=75)
    strength_selector = Combobox(
        screen, font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), width=18
    )
    strength_selector["values"] = tuple(
        k for k in PASS_STRENGTH.keys() if k
    )  # set non-empty values from dictionary
    strength_selector["state"] = "readonly"
    strength_selector.current(2)
    strength_selector.place(x=100, y=75)

    # generate button
    btn_generate = tk.Button(
        screen,
        text="Generate",
        font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
        command=lambda: txt_password.set(
            generate_password(PASS_STRENGTH[strength_selector.get()])
        ),
    )
    btn_generate.place(x=50, y=125)

    # clear button
    btn_clear = tk.Button(
        screen,
        text="Clear",
        font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
        command=lambda: txt_password.set(""),
    )
    btn_clear.place(x=175, y=125)

    # spawn the GUI
    screen.mainloop()

    # exit after user quits
    sys.exit(0)


if __name__ == "__main__":
    strength = "High"
    args = sys.argv[1:]
    if len(args) > 0:
        if args[0] in {"-g", "--gui"}:
            create_gui()
        elif args[0] in {"-h", "--high"}:
            strength = "High"
        elif args[0] in {"-m", "--medium"}:
            strength = "Medium"
        elif args[0] in {"-l", "--low"}:
            strength = "Low"
        else:
            print("\nPyPass - Password Generation Utility.\n")
            print(
                "usage: pypass.py [--help] [--gui | -g] [--high | --medium | --low] [-h | -m | -l]\n"
            )
            print("options:")
            print("        --help      show this help message")
            print("    -g, --gui       open in GUI mode")
            print("    -h, --high      16-character password")
            print("    -m, --medium    12-character password")
            print("    -l, --low        8-character password")
            print(
                "\nPS: If no options are specified, a 16-character password is generated."
            )
            sys.exit(0 if args[0] == "--help" else 1)

    print(generate_password(PASS_STRENGTH[strength]))
