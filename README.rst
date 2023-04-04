CybarPass
=========

Minimalistic Passphrase Generation script with GUI
--------------------------------------------------

Dependencies
~~~~~~~~~~~~

-  Python >= 3.9
-  ``tkinter`` module

**PS**: Also requires a word list file where each word is on a new line.
You can supply your own, or, on MacOS and Linux, use
``/usr/share/dict/words``.

Installation
~~~~~~~~~~~~

1. Open terminal and run ``python3 -m pip install cybarpass``

2. Make sure it is executable on the ``$PATH``

2. Run according to the instructions below

Usage
~~~~~

1. GUI mode: run ``cybarpass`` in the terminal

2. GUI mode with word list preload: run
   ``cybarpass -g /path/to/word/list``

3. CLI mode: run ``cybarpass /path/to/word/list`` with optional parameter
   ``-n``

Help Screen
^^^^^^^^^^^

   output of ``cybarpass -h``

.. code::

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

Example Runs
^^^^^^^^^^^^

.. code:: sh

   $ cybarpass -h

   $ cybarpass

   $ cybarpass -g

   $ cybarpass -g /usr/share/dict/words

   $ cybarpass /usr/share/dict/words

   $ cybarpass /usr/share/dict/words -n 512

**PS**: the above commands assume ``cybarpass`` is available on ``$PATH``
or is aliased to the module

Resources
~~~~~~~~~

-  `Developing a Full Tkinter Object-Oriented
   Application <https://www.pythontutorial.net/tkinter/tkinter-object-oriented-application/>`__
   on `pythontutorial.net <https://www.pythontutorial.net/>`__

-  `Tkinter
   Grid <https://www.pythontutorial.net/tkinter/tkinter-grid/>`__ on
   `pythontutorial.net <https://www.pythontutorial.net/>`__

-  `Tkinter Open File
   Dialog <https://www.pythontutorial.net/tkinter/tkinter-open-file-dialog/>`__
   on `pythontutorial.net <https://www.pythontutorial.net/>`__

-  `Tkinter – Read only Entry
   Widget <https://www.geeksforgeeks.org/tkinter-read-only-entry-widget/>`__
   on `GeeksforGeeks <https://www.geeksforgeeks.org/>`__

-  `tkinter — Python interface to
   Tcl/Tk <https://docs.python.org/3/library/tkinter.html>`__ on
   `docs.python.org <https://docs.python.org/>`__

-  `Packaging Python
   Projects <https://packaging.python.org/en/latest/tutorials/packaging-projects/>`__
   on `packaging.python.org <https://packaging.python.org>`__

-  `The .pypirc
   file <https://packaging.python.org/en/latest/specifications/pypirc/>`__
   on `packaging.python.org <https://packaging.python.org>`__
