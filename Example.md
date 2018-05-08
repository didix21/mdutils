
This is a Markdown File Example
===============================

Contents
========

* [Overview](#overview)
* [What you can do](#what-you-can-do)
	* [Create Markdown files](#create-markdown-files)
	* [Create Headers](#create-headers)
	* [Table of Contents](#table-of-contents)
	* [Paragraph and Text Format](#paragraph-and-text-format)
	* [Create a Table](#create-a-table)

# Overview


This is an example of markdown file created using mdutils python package. In this example youare going to see how to create a markdown file using this library. Moreover, you're finding the available features which makes easy create this type of files while you are runningpython code.


# What you can do

## Create Markdown files


It is the last command that has to be called.

```python
import Mdutils


mdFile = MdUtils(file_name='Example',title='This is a Markdown File Example')
mdFile.create_md_file()
```
## Create Headers


Using ``new_header`` method you can create headers of different levels depending on the style.There are two available styles: 'atx' and 'setext'. The first one, it has til 6 different header levels and levels 1 and 2 of this style are added automatically to the table of contents. The'setext' style only has two levels of headers and they are not added to the table of contents.

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


If you have defined some headers of level 1 and 2, you can create a table of contents invokingthe following command (Normally, the method will be called at the end of the code before calling``create_md_file()``)

```python
mdFile.new_table_of_contents(table_title='Contents', depth=2)
```
## Paragraph and Text Format


mdutils allows you to create paragraph, line breaks or simply writing text:

```python
mdFile.new_paragraph(Using ``new_paragraph`` method you can add very easily a new paragraph 
			on your markdown file. This example of paragraph has been added using this method. Moreover,
			``new_paragraph`` method make your live easy because it can give format to the text. Lets 
			see an example:)
```

Using ``new_paragraph`` method you can add very easily a new paragraph on your markdown file. This example of paragraph has been added using this method. Moreover, ``new_paragraph`` method make your live easy because it can give format to the text. Lets see an example:

***<font color="purple"> This is an example of text in which has been added color, bold and italics text. </font>***

mdutils has a method which can create new line breaks. Lets see it.  
This is an example of line break which has been created with ``new_line`` method.

As ``new_paragraph``, ``new_line`` allows users to give format to text using ``bold_italics_code`` and ``color`` parameters:  
***<center>``This is an inline code which contains bold and italics text and it is centered``</center>***

''write'' method write text in markdown file without jump lines ('\n') and as ``new_paragraph`` and ``new_line`` using the arguments ``bold_italics_code``, ``color`` and ``align`` you cangive format to text: The following text has been written with ``write`` method. You can use markdown directives to write: **bold**, _italics_, ``inline_code``... or use the following available parameters:  
- ***``bold_italics_code``*** <---------------------------------  ``mdFile.write('bold_italics_code', bold_italics_code='bic')``
- <font color="green"> color </font> <---------------------------------  ``mdFile.write('color', color='green')``
- <center>center</center> <-----------  ``mdFile.write('center', align='center')``

## Create a Table


The library implements a method called ``new_table`` that can create table using a list of strings. This method only needs, the number of rows and columns that your table must have.  

|Items|Descriptions|Data|
| :---: | :---: | :---: |
|Item 0|Description Item 0|0|
|Item 1|Description Item 1|1|
|Item 2|Description Item 2|2|
|Item 3|Description Item 3|3|
|Item 4|Description Item 4|4|
