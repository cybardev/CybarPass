#!/usr/bin/env python3
import random
import string
import sys
from tkinter import *
from tkinter.ttk import Combobox

# configuration variables
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400
DEFAULT_FONT = "Arial"
DEFAULT_FONT_SIZE = 14
PASS_STRENGTHS = {
    "Low": 8,
    "Medium": 12,
    "High": 16,
    "": 16,
}  # strength: password length


def generate_password(length: int = PASS_STRENGTHS["High"]) -> str:
    """Generate a random password of the given length.

    Args:
        length (int, optional): length of password. Defaults to PASS_STRENGTHS["High"].

    Returns:
        str: generated password
    """
    mixed_chars = string.digits + string.ascii_letters + string.punctuation
    return "".join([random.choice(mixed_chars) for i in range(length)])


def create_gui() -> None:
    """Create a GUI window to generate password"""

    # initialize window
    screen = Tk()
    screen.title("PyPass")
    screen.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    # program title
    lbl_title = Label(
        screen, text="PyPass", font=(DEFAULT_FONT, 2 * DEFAULT_FONT_SIZE)
    )
    lbl_title.place(x=80, y=10)

    # generated password
    lbl_password = Label(
        screen, text="Password:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE)
    )
    lbl_password.place(x=100, y=100)
    txt_password = StringVar()
    entry_result = Entry(
        screen,
        font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
        textvariable=txt_password,
    )
    entry_result.place(x=200, y=100)

    # strength selection dropdown
    lbl_strength = Label(
        screen, text="Strength:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE)
    )
    lbl_strength.place(x=113, y=135)
    strength_selector = Combobox(
        screen, font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), width=18
    )
    strength_selector["values"] = tuple(PASS_STRENGTHS.keys())
    strength_selector["state"] = "readonly"
    strength_selector.current(2)
    strength_selector.place(x=200, y=135)

    # generate button
    btn_generate = Button(
        screen,
        text="Generate",
        font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
        command=lambda: txt_password.set(
            generate_password(PASS_STRENGTHS[strength_selector.get()])
        ),
    )
    btn_generate.place(x=200, y=200)

    # clear button
    btn_clear = Button(
        screen,
        text="Clear",
        font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
        command=lambda: txt_password.set(""),
    )
    btn_clear.place(x=300, y=200)

    # spawn the GUI
    screen.mainloop()

    # exit after user quits
    sys.exit(0)


if __name__ == "__main__":
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
            print("    --help          show this help message")
            print("    -g, --gui           open in GUI mode")
            print("    -h, --high      16-character password")
            print("    -m, --medium    12-character password")
            print("    -l, --low        8-character password")
            print(
                "\nPS: If no options are specified, a 16-character password is generated."
            )
            sys.exit(0 if args[0] == "--help" else 1)
    else:
        strength = "High"

    print(generate_password(PASS_STRENGTHS[strength]))
