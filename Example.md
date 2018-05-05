
This is a Markdown File Example
===============================

Contents
========

* [Overview](#overview)
* [What you can do](#what-you-can-do)
	* [Create Headers](#create-headers)
	* [Paragraph and Text Format](#paragraph-and-text-format)

# Overview


This is an example of markdown file created using mdutils python package. In this example youare going to see how to create a markdown file using this library. Moreover, you're finding the available features which makes easy create this type of files while you are runningpython code.


# What you can do

## Create Headers


Using ``new_header`` method you can create headers of different levels depending on the style.There are two available styles: 'atx' and 'setext'. The first one, it has til 6 different header levels and levels 1 and 2 of this style are added automatically to the table of contents. The'setext' style only has two levels of headers and they are not added to the table of contents.


## Paragraph and Text Format


mdutils allows you to create paragraph, line breaks or simply writing text:

Using ``new_paragraph`` method you can add very easily a new paragraph on your markdown file. This example of paragraph has been added using this method. Moreover, ``new_paragraph`` method make your live easy because it can give format to the text. Lets see an example:

_**<font color="purple"> This is an example of text in which has been added color, bold and italics text. </font>**_

mdutils has a method which can create new line breaks. Lets see it.  
This is an example of line break which has been created with ``new_line`` method.

As ``new_paragraph``, ``new_line`` allows users to give format to text using ``bold_italics_code`` and ``color`` parameters:  
<font color="blue">``This is an inline code with color``</font>