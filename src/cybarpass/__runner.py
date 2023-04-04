from typing import Union
from .passgen import PassGen
from .app import AppFrame


def run(
    filename: Union[str, None] = None,
    char_limit: int = 16,
    gui_mode: bool = True,
) -> None:
    if filename is None or gui_mode:
        AppFrame(filename=filename)
    else:
        print(PassGen(filename, char_limit).passphrase)
