=====================
Markdown File Example
=====================

Contents
========

-  `Overview <#overview>`__
-  `This is what you can do <#this-is-what-you-can-do>`__

   -  `Create Markdown files <#create-markdown-files>`__
   -  `Create Headers <#create-headers>`__
   -  `Table of Contents <#table-of-contents>`__
   -  `Paragraph and Text Format <#paragraph-and-text-format>`__
   -  `Create a Table <#create-a-table>`__

Overview
========

This is an example of markdown file created using mdutils python
package. In this example you are going to see how to create a markdown
file using this library. Moreover, you’re finding the available features
which makes easy the creation of this type of files while you are
running Python code.

**IMPORTANT:** some features available on this library have no effect
with the GitHub Markdown CSS. Some of them are: coloring text, centering
text…

This is what you can do
=======================

Create Markdown files
---------------------

It is the last command that has to be called.

.. code:: python

    import Mdutils


    mdFile = MdUtils(file_name='Example_Markdown',title='Markdown File Example')
    mdFile.create_md_file()

Create Headers
--------------

Using ``new_header`` method you can create headers of different levels
depending on the style. There are two available styles: ‘atx’ and
‘setext’. The first one has til 6 different header levels. Atx’s levels
1 and 2 are automatically added to the table of contents unless the
parameter ``add_table_of_contents`` is set to ‘n’. The ‘setext’ style
only has two levelsof headers.

.. code:: python

    mdFile.new_header(level=1, title='Atx Header 1')
    mdFile.new_header(level=2, title='Atx Header 2')
    mdFile.new_header(level=3, title='Atx Header 3')
    mdFile.new_header(level=4, title='Atx Header 4')
    mdFile.new_header(level=5, title='Atx Header 5')
    mdFile.new_header(level=6, title='Atx Header 6')

Atx Header 1
============

Atx Header 2
------------

Atx Header 3
~~~~~~~~~~~~

Atx Header 4
^^^^^^^^^^^^

Atx Header 5
''''''''''''

Atx Header 6
            

.. code:: python

    mdFile.new_header(level=1, title='Setext Header 1', style='setext')
    mdFile.new_header(level=2, title='Setext Header 2', style='setext')

Setext Header 1
===============

Setext Header 2
---------------

Table of Contents
-----------------

If you have defined some headers of level 1 and 2, you can create a
table of contents invoking the following command (Normally, the method
will be called at the end of the code before calling
``create_md_file()``)

.. code:: python

    mdFile.new_table_of_contents(table_title='Contents', depth=2)

Paragraph and Text Format
-------------------------

mdutils allows you to create paragraph, line breaks or simply write
text:

New Paragraph Method
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    mdFile.new_paragraph("Using ``new_paragraph`` method you can very easily add a new paragraph" 
                         " This example of paragraph has been added using this method. Moreover,"
                         "``new_paragraph`` method make your live easy because it can give format" 
                         " to the text. Lets see an example:")

Using ``new_paragraph`` method you can very easily add a new paragraph
on your markdown file. This example of paragraph has been added using
this method. Moreover, ``new_paragraph`` method make your live easy
because it can give format to the text. Lets see an example:

.. code:: python

    mdFile.new_paragraph("This is an example of text in which has been added color, bold and italics text.", bold_italics_code='bi', color='purple')

.. raw:: html

    <font color="purple"><b><i>

    This is an example of text in which has been added color, bold and
    italics text.

.. raw:: html

    </b></i></font>


--------------

New Line Method
~~~~~~~~~~~~~~~

``mdutils`` has a method which can create new line breaks. Lets see it.

.. code:: python

    mdFile.new_line("This is an example of line break which has been created with ``new_line`` method.")

This is an example of line break which has been created with
``new_line`` method.

As ``new_paragraph``, ``new_line`` allows users to give format to text
using ``bold_italics_code`` and ``color`` parameters:

.. code:: python

    mdFile.new_line("This is an inline code which contains bold and italics text and it is centered", bold_italics_code='cib', align='center')


.. raw:: html

   <center><b><i><code>

    This is an inline code which contains bold and italics text and it is centered

.. raw:: html

   </code></i></b></center>

--------------

Write Method
~~~~~~~~~~~~

``write`` method writes text in a markdown file without jump lines
``'\n'`` and as ``new_paragraph`` and ``new_line``, you can give format
to text using the arguments ``bold_italics_code``, ``color`` and
``align``:

.. code:: python

    mdFile.write("The following text has been written with ``write`` method. You can use markdown directives to write:"
                 "**bold**, _italics_, ``inline_code``... or ")
    mdFile.write("use the following available parameters:  \n")

The following text has been written with ``write`` method. You can use
markdown directives to write: **bold**, *italics*, ``inline_code``\ … or
use the following available parameters:

.. code:: python

    mdFile.write('  \n')
    mdFile.write('bold_italics_code', bold_italics_code='bic')
    mdFile.write('  \n')
    mdFile.write('Text color', color='green')
    mdFile.write('  \n')
    mdFile.write('Align Text to center', align='center')

.. raw:: html

    <b><i><code>

    bold_italics_code

.. raw:: html

    </code></i></b><br/>


.. raw:: html

    <font color="green">

    Text color

.. raw:: html

    </font>


.. raw:: html

   <center>

    Align Text to center

.. raw:: html

   </center>

Create a Table
--------------

The library implements a method called ``new_table`` that can create
tables using a list of strings. This method only needs: the number of
rows and columns that your table must have. Optionally you can align the
content of the table using the parameter ``text_align``

.. code:: python

    list_of_strings = ["Items", "Descriptions", "Data"]
    for x in range(5):
        list_of_strings.extend(["Item " + str(x), "Description Item " + str(x), str(x)])
    mdFile.new_line()
    mdFile.new_table(columns=3, rows=6, text=list_of_strings, text_align='center')

+--------+--------------------+------+
| Items  | Descriptions       | Data |
+========+====================+======+
| Item 0 | Description Item 0 | 0    |
+--------+--------------------+------+
| Item 1 | Description Item 1 | 1    |
+--------+--------------------+------+
| Item 2 | Description Item 2 | 2    |
+--------+--------------------+------+
| Item 3 | Description Item 3 | 3    |
+--------+--------------------+------+
| Item 4 | Description Item 4 | 4    |
+--------+--------------------+------+
