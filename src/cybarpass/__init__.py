# __init__.py

from typing import Union
from cybarpass.passgen import PassGen
from cybarpass.app import AppFrame

# specify package version
__version__ = "2.1"


def run(
    filename: Union[str, None] = None,
    char_limit: int = 16,
    gui_mode: bool = True,
):
    if filename is None or gui_mode:
        AppFrame(filename=filename)
    else:
        print(PassGen(filename, char_limit).passphrase)
