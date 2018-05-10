=======
mdutils
=======
|build-status| |documentation-status|

.. contents:: Table of Contents

Overview
========
This Python package contains a set of basic tools that can help to create a markdown file while running a Python code.
Thus, if you are executing a Python code and you save the result in a text file, Why not format it? So
using files such as Markdown can give a great look to those results. In this way, mdutils will make things easy for
creating Markdown files.

- Project Homepage: https://github.com/didix21/mdutils
- Download Page: https://pypi.python.org/pypi/mdutils
- Documentation: http://mdutils.readthedocs.io/en/latest/

MIT License, (C) 2018 Didac Coll <didaccoll_93@hotmail.com>

Features
========
There are some different features available on that version of mdutils:

Writing and Reading Files
-------------------------
- Write and Read Markdown files.
- Append data to the end of a Markdown file.
- Use markers to place text.

Markdown
--------
- Implemented method to give format to the text: bold, italics, change color...
- Add headers of levels 1 til 6 (atx style) or 1 and 2 (setext style).
- Create tables.
- Create a table of contents.

.. note::

    Some available features will depen on which CSS you are using. For example, GitHub do not allows to give color to text.


Installation
============
Use pip to install mdutils:

.. code:: bash

    $ pip install mdutils



.. |build-status| image:: https://travis-ci.org/didix21/mdutils.svg?branch=master
    :target: https://travis-ci.org/didix21/mdutils
    :alt: Build status

.. |documentation-status| image:: https://readthedocs.org/projects/mdutils/badge/?version=latest
    :target: http://mdutils.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
