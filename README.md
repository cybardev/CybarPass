# PassGen

## Minimalistic Passphrase Generation script

```
usage: passgen [-h] [-n NUM] [-g] [WORD_LIST]

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
