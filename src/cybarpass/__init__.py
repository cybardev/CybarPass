# __init__.py

from types import MappingProxyType
from cybarpass.passgen import PassGen
from cybarpass.app import AppFrame

# specify package version
__version__ = "2.0"


# map of constants
CONST = MappingProxyType(
    {
        "win-title": "PassGen",
        "win-width": 450,
        "win-height": 200,
        "pass-strength": {"Low": 16, "Medium": 24, "High": 32},
    }
)


def run(filename: str | None = None, char_limit: int = 16, gui_mode: bool = True):
    if filename is None or gui_mode:
        AppFrame(filename=filename)
    else:
        print(PassGen(filename, char_limit).passphrase)
