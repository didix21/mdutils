=======
mdutils
=======
|build-status| |documentation-status| |coverage-status|

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
- Align text.
- Add headers of levels 1 til 6 (atx style) or 1 and 2 (setext style).
- Create tables.
- Create a table of contents.
- Add Links.
- Add Lists.
- Add Markdown Images.
- Add Html Images.

.. note::

    Some available features will depen on which CSS you are using. For example, GitHub do not allows to give color to text.


Installation
============

Pip
---
Use pip to install mdutils:

.. code:: bash

    $ pip install mdutils

Poetry
------
Use poetry to install mdutils:

.. code:: bash

    $ poetry add mdutils


.. |build-status| image:: https://github.com/didix21/mdutils/actions/workflows/main.yml/badge.svg
    :target: https://github.com/didix21/mdutils
    :alt: Build Status

.. |documentation-status| image:: https://readthedocs.org/projects/mdutils/badge/?version=latest
    :target: http://mdutils.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |coverage-status| image:: https://codecov.io/gh/didix21/mdutils/branch/master/graph/badge.svg?token=0DN72Z1B6V
    :target: https://codecov.io/gh/didix21/mdutils
    :alt: Coverage Status
