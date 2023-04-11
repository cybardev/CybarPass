#!/usr/bin/env python3

import os
import sys
import argparse
from .__runner import run

if __name__ == "__main__":
    # argument parsing
    parser = argparse.ArgumentParser(
        prog="cybarpass",
        description="Generate a secure passphrase",
        epilog="NOTE: -n | --len has no effect in GUI mode",
        allow_abbrev=False,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "filename",
        help="Path to dictionary file",
        metavar="WORD_LIST",
        type=str,
        nargs="?",
        default=f"{os.path.dirname(sys.argv[0])}/words",
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

    # invoke main program logic
    run(args.filename, args.char_limit, args.gui_mode)
