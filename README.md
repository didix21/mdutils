# mdutils
[![Build Status](https://travis-ci.org/didix21/mdutils.svg?branch=master)](https://travis-ci.org/didix21/mdutils)
[![Documentation Status](https://readthedocs.org/projects/mdutils/badge/?version=latest)](http://mdutils.readthedocs.io/en/latest/?badge=latest)

Table of Contents
=================
- [Overview](#overview)
- [Features](#features)
    - [Writing and Reading Files](#writing-and-reading-files)
    - [Markdown](#markdown)    
- [Installation](#installation)
- [Things to do](#things-to-do)
- [Markdown File Example](#markdown-file-example)

Overview
=======
This Python package contains a set of basic tools that can help to create a markdown file while running a Python code.
Thus, if you are executing a Python code and you save the result in a text file, Why not format it? So
using files such as Markdown can give a great look to those results. In this way, mdutils will make things easy for
creating Markdown files.

- Project Homepage: https://github.com/didix21/mdutils
- Download Page: https://pypi.python.org/pypi/mdutils
- Documentation: http://mdutils.readthedocs.io/en/latest/

MIT License, (C) 2018 Dídac Coll <didaccoll_93@hotmail.com>

Features
========
These are the following available features:

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

**NOTE:** some available features will depen on which CSS you are using. For example, GitHub do not allows to give color to text.

Installation
============
Use pip to install mdutils:
```bash
$ pip install mdutils
```

Markdown File Example
=====================

Contents
========

* [Overview](#overview)
* [This is what you can do](#this-is-what-you-can-do)
	* [Create Markdown files](#create-markdown-files)
	* [Create Headers](#create-headers)
	* [Table of Contents](#table-of-contents)
	* [Paragraph and Text Format](#paragraph-and-text-format)
	* [Create a Table](#create-a-table)

# Overview


This is an example of markdown file created using mdutils python package. In this example you are going to see how to create a markdown file using this library. Moreover, you're finding the available features which makes easy the creation of this type of files while you are running Python code.

**IMPORTANT:** some features available on this library have no effect with the GitHub Markdown CSS. Some of them are: coloring text, centering text...

The Python file has been generated this file can be found [here](doc/source/examples/Example_Python.md).


# This is what you can do

## Create Markdown files


``create_md_file()`` is the last command that has to be called.

```python
import Mdutils


mdFile = MdUtils(file_name='Example',title='This is a Markdown File Example')
mdFile.create_md_file()
```
## Create Headers


Using ``new_header`` method you can create headers of different levels depending on the style. There are two available styles: 'atx' and 'setext'. The first one has til 6 different header levels. Atx's levels 1 and 2 are automatically added to the table of contents unless the parameter ``add_table_of_contents`` is set to 'n'. The 'setext' style only has two levelsof headers.

```python
mdFile.new_header(level=1, title='Atx Header 1')
mdFile.new_header(level=2, title='Atx Header 2')
mdFile.new_header(level=3, title='Atx Header 3')
mdFile.new_header(level=4, title='Atx Header 4')
mdFile.new_header(level=5, title='Atx Header 5')
mdFile.new_header(level=6, title='Atx Header 6')
```
# Atx Header 1

## Atx Header 2

### Atx Header 3

#### Atx Header 4

##### Atx Header 5

###### Atx Header 6


```python
mdFile.new_header(level=1, title='Setext Header 1', style='setext')
mdFile.new_header(level=2, title='Setext Header 2', style='setext')
```
Setext Header 1
===============

Setext Header 2
---------------



## Table of Contents


If you have defined some headers of level 1 and 2, you can create a table of contents invoking the following command (Normally, the method will be called at the end of the code before calling ``create_md_file()``)

```python
mdFile.new_table_of_contents(table_title='Contents', depth=2)
```
## Paragraph and Text Format


mdutils allows you to create paragraph, line breaks or simply write text:
### New Paragraph Method


```python
mdFile.new_paragraph("Using ``new_paragraph`` method you can very easily add a new paragraph"
					 " This example of paragraph has been added using this method. Moreover,"
					 "``new_paragraph`` method make your live easy because it can give format"
					 " to the text. Lets see an example:")
```

Using ``new_paragraph`` method you can very easily add a new paragraph on your markdown file. This example of paragraph has been added using this method. Moreover, ``new_paragraph`` method make your live easy because it can give format to the text. Lets see an example:

```python
mdFile.new_paragraph("This is an example of text in which has been added color, bold and italics text.", bold_italics_code='bi', color='purple')
```

***<font color="purple"> This is an example of text in which has been added color, bold and italics text. </font>***
### New Line Method


``mdutils`` has a method which can create new line breaks. Lets see it.

```python
mdFile.new_line("This is an example of line break which has been created with ``new_line`` method.")
```  
This is an example of line break which has been created with ``new_line`` method.

As ``new_paragraph``, ``new_line`` allows users to give format to text using ``bold_italics_code`` and ``color`` parameters:

```python
mdFile.new_line("This is an inline code which contains bold and italics text and it is centered", bold_italics_code='cib', align='center')
```  
***<center>``This is an inline code which contains bold and italics text and it is centered``</center>***
### Write Method


``write`` method writes text in a markdown file without jump lines ``'\n'`` and as ``new_paragraph`` and ``new_line``, you can give format to text using the arguments ``bold_italics_code``, ``color`` and ``align``:

```python
mdFile.write("The following text has been written with ``write`` method. You can use markdown directives to write:"
			 "**bold**, _italics_, ``inline_code``... or ")
mdFile.write("use the following available parameters:  \n")
```

The following text has been written with ``write`` method. You can use markdown directives to write: **bold**, _italics_, ``inline_code``... or use the following available parameters:  


```python
mdFile.write('  \n')
mdFile.write('bold_italics_code', bold_italics_code='bic')
mdFile.write('  \n')
mdFile.write('Text color', color='green')
mdFile.write('  \n')
mdFile.write('Align Text to center', align='center')
```  
***``bold_italics_code``***  
<font color="green"> Text color </font>  
<center>Align Text to center</center>  

## Create a Table


The library implements a method called ``new_table`` that can create tables using a list of strings. This method only needs: the number of rows and columns that your table must have. Optionally you can align the content of the table using the parameter ``text_align``

```python
list_of_strings = ["Items", "Descriptions", "Data"]
for x in range(5):
	list_of_strings.extend(["Item " + str(x), "Description Item " + str(x), str(x)])
mdFile.new_line()
mdFile.new_table(columns=3, rows=6, text=list_of_strings, text_align='center')
```  

|Items|Descriptions|Data|
| :---: | :---: | :---: |
|Item 0|Description Item 0|0|
|Item 1|Description Item 1|1|
|Item 2|Description Item 2|2|
|Item 3|Description Item 3|3|
|Item 4|Description Item 4|4|
