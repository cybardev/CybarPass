# CybarPass

## Minimalistic Passphrase Generation script with GUI

<img width="562" alt="image" src="https://user-images.githubusercontent.com/50134239/229692629-20cb301f-b577-4e9b-9299-b25516116861.png">

### Dependencies

-   Python \>= 3.9
-   `tkinter` module

**PS**: Also requires a word list file where each word is on a new line. You can supply your own, or, on MacOS and Linux, use `/usr/share/dict/words`.

### Installation

1.  Open terminal and run `python3 -m pip install cybarpass`
2.  Set a shell alias: `alias cybarpass="python3 -m cybarpass"`
3.  Run according to the instructions below

### Usage

1.  GUI mode: run `cybarpass` in the terminal
2.  GUI mode with word list preload: run
    `cybarpass -g /path/to/word/list`
3.  CLI mode: run `cybarpass /path/to/word/list` with optional parameter
    `-n`

#### Help Screen

> output of `cybarpass -h`

```
usage: cybarpass [-h] [-n NUM] [-g] [WORD_LIST]

Generate a secure passphrase

positional arguments:
  WORD_LIST          Path to dictionary file

options:
  -h, --help         show this help message and exit
  -n NUM, --len NUM  Minimum length of passphrase
  -g, --gui          Run the program in GUI mode

Launch without arguments for GUI mode
or use -g | --gui with /path/to/word/list to preload the file

PS: -n | --len has no effect in GUI mode
```

#### Example Runs

```sh
$ cybarpass -h

$ cybarpass

$ cybarpass -g

$ cybarpass -g /usr/share/dict/words

$ cybarpass /usr/share/dict/words

$ cybarpass /usr/share/dict/words -n 512
```

### Resources

-   [Developing a Full Tkinter Object-Oriented Application](https://www.pythontutorial.net/tkinter/tkinter-object-oriented-application/) on [pythontutorial.net](https://www.pythontutorial.net/)
-   [Tkinter Grid](https://www.pythontutorial.net/tkinter/tkinter-grid/) on [pythontutorial.net](https://www.pythontutorial.net/)
-   [Tkinter Open File Dialog](https://www.pythontutorial.net/tkinter/tkinter-open-file-dialog/) on [pythontutorial.net](https://www.pythontutorial.net/)
-   [Tkinter – Read only Entry Widget](https://www.geeksforgeeks.org/tkinter-read-only-entry-widget/) on [GeeksforGeeks](https://www.geeksforgeeks.org/)
-   [tkinter — Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html) on [docs.python.org](https://docs.python.org/)
-   [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/) on [packaging.python.org](https://packaging.python.org)
-   [The .pypirc file](https://packaging.python.org/en/latest/specifications/pypirc/) on [packaging.python.org](https://packaging.python.org)
-   [How to Create and Upload Your First Python Package to PyPI](https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/) on [freecodecamp.org](https://www.freecodecamp.org)
