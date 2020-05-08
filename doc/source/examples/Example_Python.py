# Python
#
# This file implements an example.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# MIT License: (C) 2018 Dídac Coll


from mdutils.mdutils import MdUtils
from mdutils import Html

mdFile = MdUtils(file_name='Example_Markdown', title='Markdown File Example')

mdFile.new_header(level=1, title='Overview')  # style is set 'atx' format by default.

mdFile.new_paragraph("This is an example of markdown file created using mdutils python package. In this example you "
                     "are going to see how to create a markdown file using this library. Moreover, you're "
                     "finding the available features which makes easy the creation of this type of files while you "
                     "are running Python code.")
mdFile.new_paragraph("**IMPORTANT:** some features available on this library have no effect with the GitHub Markdown "
                     "CSS. Some of them are: coloring text, centering text...")
mdFile.new_paragraph()

# Available Features
mdFile.new_header(level=1, title="This is what you can do")

# ********************************************************************************************************************
# ***************************************************** Markdown *****************************************************
# ********************************************************************************************************************
mdFile.new_header(level=2, title="Create Markdown files")
mdFile.new_paragraph("``create_md_file()`` is the last command that has to be called.")
mdFile.insert_code("import Mdutils\n"
                   "\n"
                   "\n"
                   "mdFile = MdUtils(file_name=\'Example_Markdown\',title=\'Markdown File Example\')\n"
                   "mdFile.create_md_file()", language='python')

# ********************************************************************************************************************
# ***************************************************** Headers ******************************************************
# ********************************************************************************************************************
mdFile.new_header(level=2, title="Create Headers")
mdFile.new_paragraph("Using ``new_header`` method you can create headers of different levels depending on the style. "
                     "There are two available styles: 'atx' and 'setext'. The first one has til 6 different header "
                     "levels. Atx's levels 1 and 2 are automatically added to the table of contents unless the "
                     "parameter ``add_table_of_contents`` is set to 'n'. The 'setext' style only has two levels"
                     "of headers.")

mdFile.insert_code("mdFile.new_header(level=1, title='Atx Header 1')\n"
                   "mdFile.new_header(level=2, title='Atx Header 2')\n"
                   "mdFile.new_header(level=3, title='Atx Header 3')\n"
                   "mdFile.new_header(level=4, title='Atx Header 4')\n"
                   "mdFile.new_header(level=5, title='Atx Header 5')\n"
                   "mdFile.new_header(level=6, title='Atx Header 6')", language='python')

mdFile.new_header(level=1, title='Atx Header 1', add_table_of_contents='n')
mdFile.new_header(level=2, title='Atx Header 2', add_table_of_contents='n')
mdFile.new_header(level=3, title='Atx Header 3')
mdFile.new_header(level=4, title='Atx Header 4')
mdFile.new_header(level=5, title='Atx Header 5')
mdFile.new_header(level=6, title='Atx Header 6')

mdFile.insert_code("mdFile.new_header(level=1, title='Setext Header 1', style='setext')\n"
                   "mdFile.new_header(level=2, title='Setext Header 2', style='setext')", language='python')

mdFile.new_header(level=1, title='Setext Header 1', style='setext', add_table_of_contents='n')
mdFile.new_header(level=2, title='Setext Header 2', style='setext', add_table_of_contents='n')
mdFile.new_paragraph()  # Add two jump lines

# ********************************************************************************************************************
# ******************************************** Create a table of contents ********************************************
# ********************************************************************************************************************
mdFile.new_header(level=2, title='Table of Contents')
mdFile.new_paragraph("If you have defined some headers of level 1 and 2, you can create a table of contents invoking "
                     "the following command (Normally, the method will be called at the end of the code before calling "
                     "``create_md_file()``)")
mdFile.insert_code("mdFile.new_table_of_contents(table_title='Contents', depth=2)", language='python')

# ********************************************************************************************************************
# ******************************************** Paragraph and Text format *********************************************
# ********************************************************************************************************************
mdFile.new_header(level=2, title="Paragraph and Text Format")
mdFile.new_paragraph("mdutils allows you to create paragraph, line breaks or simply write text:")
# *************************************************** Paragraph ******************************************************
mdFile.new_header(3, "New Paragraph Method")

mdFile.insert_code("mdFile.new_paragraph(\"Using ``new_paragraph`` method you can very easily add a new paragraph\" \n"
                   "\t\t\t\t\t \" This example of paragraph has been added using this method. Moreover,\"\n"
                   "\t\t\t\t\t \"``new_paragraph`` method make your live easy because it can give format\" \n"
                   "\t\t\t\t\t \" to the text. Lets see an example:\")", language='python')

mdFile.new_paragraph("Using ``new_paragraph`` method you can very easily add a new paragraph on your markdown file. "
                     "This example of paragraph has been added using this method. Moreover, ``new_paragraph`` method "
                     "make your live easy because it can give format to the text. Lets see an example:")

mdFile.insert_code("mdFile.new_paragraph(\"This is an example of text in which has been added color, "
                   "bold and italics text.\", bold_italics_code='bi', color='purple')", language='python')

mdFile.new_paragraph("This is an example of text in which has been added color, bold and italics text.",
                     bold_italics_code='bi', color='purple')
# ************************************************* New Line *********************************************************
mdFile.new_header(3, "New Line Method")

mdFile.new_paragraph("``mdutils`` has a method which can create new line breaks. Lets see it.")
mdFile.insert_code("mdFile.new_line(\"This is an example of line break which has been created with ``new_line`` "
                   "method.\")", language='python')
mdFile.new_line("This is an example of line break which has been created with ``new_line`` method.")
mdFile.new_paragraph("As ``new_paragraph``, ``new_line`` allows users to give format to text using "
                     "``bold_italics_code`` and ``color`` parameters:")

mdFile.insert_code("mdFile.new_line(\"This is an inline code which contains bold and italics text and it is centered\","
                   " bold_italics_code='cib', align='center')", language='python')

mdFile.new_line("This is an inline code which contains bold and italics text and it is centered",
                bold_italics_code='cib', align='center')
# ************************************************** write **********************************************************
mdFile.new_header(3, "Write Method")
mdFile.new_paragraph("``write`` method writes text in a markdown file without jump lines ``'\\n'`` and as "
                     "``new_paragraph`` and ``new_line``, you can give format to text using the arguments "
                     "``bold_italics_code``, ``color`` and ``align``: ")

mdFile.insert_code("mdFile.write(\"The following text has been written with ``write`` method. You can use markdown "
                   "directives to write:\"\n"
                   "\t\t\t \"**bold**, _italics_, ``inline_code``... or \")\n"
                   "mdFile.write(\"use the following available parameters:  \\n\")", language='python')

mdFile.write("\n\nThe following text has been written with ``write`` method. You can use markdown directives to write: "
             "**bold**, _italics_, ``inline_code``... or ")
mdFile.write("use the following available parameters:  \n")

mdFile.insert_code("mdFile.write('  \\n')\n"
                   "mdFile.write('bold_italics_code', bold_italics_code='bic')\n"
                   "mdFile.write('  \\n')\n"
                   "mdFile.write('Text color', color='green')\n"
                   "mdFile.write('  \\n')\n"
                   "mdFile.write('Align Text to center', align='center')", language='python')

mdFile.write('  \n')
mdFile.write('bold_italics_code', bold_italics_code='bic')
mdFile.write('  \n')
mdFile.write('Text color', color='green')
mdFile.write('  \n')
mdFile.write('Align Text to center', align='center')
mdFile.write('  \n')

# ********************************************************************************************************************
# ************************************************* Create a Table ***************************************************
# ********************************************************************************************************************
mdFile.new_header(2, "Create a Table")
mdFile.new_paragraph("The library implements a method called ``new_table`` that can create tables using a list of "
                     "strings. This method only needs: the number of rows and columns that your table must have. "
                     "Optionally you can align the content of the table using the parameter ``text_align``")

mdFile.insert_code("list_of_strings = [\"Items\", \"Descriptions\", \"Data\"]\n"
                   "for x in range(5):\n"
                   "\tlist_of_strings.extend([\"Item \" + str(x), \"Description Item \" + str(x), str(x)])\n"
                   "mdFile.new_line()\n"
                   "mdFile.new_table(columns=3, rows=6, text=list_of_strings, text_align='center')", language='python')

list_of_strings = ["Items", "Descriptions", "Data"]
for x in range(5):
    list_of_strings.extend(["Item " + str(x), "Description Item " + str(x), str(x)])
mdFile.new_line()
mdFile.new_table(columns=3, rows=6, text=list_of_strings, text_align='center')

# ********************************************************************************************************************
# ************************************************** Create Link *****************************************************
# ********************************************************************************************************************

mdFile.new_header(2, "Create Links")

# *********************************************** Inline link ********************************************************

mdFile.new_header(3, "Create inline links")

link = "https://github.com/didix21/mdutils"
text = "mdutils"

mdFile.new_paragraph("``new_inline_link`` method allows you to create a link of the style: "
                     "``[mdutils](https://github.com/didix21/mdutils)``.\n")
mdFile.new_paragraph("Moreover, you can add bold, italics or code in the link text. Check the following examples: \n")

mdFile.insert_code("mdFile.new_line('  - Inline link: '"
                   " + mdFile.new_inline_link(link='{}', text='{}')) \n".format(link, text) +
                   "mdFile.new_line('  - Bold inline link: ' "
                   "+ mdFile.new_inline_link(link='{}', text='{}', bold_italics_code='b') \n".format(link, text) +
                   "mdFile.new_line('  - Italics inline link: ' "
                   "+ mdFile.new_inline_link(link='{}', text='{}', bold_italics_code='i') \n".format(link, text) +
                   "mdFile.new_line('  - Code inline link: ' "
                   "+ mdFile.new_inline_link(link='{}', text='{}', bold_italics_code='i') \n".format(link, text) +
                   "mdFile.new_line('  - Bold italics code inline link: ' "
                   "+ mdFile.new_inline_link(link='{}', text='{}', bold_italics_code='cbi') \n".format(link, text) +
                   "mdFile.new_line('  - Another inline link: ' + mdFile.new_inline_link(link='{}') \n".format(link),
                   language='python')

mdFile.new_line('  - Inline link: ' + mdFile.new_inline_link(link=link, text=text))
mdFile.new_line('  - Bold inline link: ' + mdFile.new_inline_link(link=link, text=text, bold_italics_code='b'))
mdFile.new_line('  - Italics inline link: ' + mdFile.new_inline_link(link=link, text=text, bold_italics_code='i'))
mdFile.new_line('  - Code inline link: ' + mdFile.new_inline_link(link=link, text=text, bold_italics_code='c'))
mdFile.new_line(
    '  - Bold italics code inline link: ' + mdFile.new_inline_link(link=link, text=text, bold_italics_code='cbi'))
mdFile.new_line('  - Another inline link: ' + mdFile.new_inline_link(link=link))

# *********************************************** Reference link ******************************************************
mdFile.new_header(3, "Create reference links")

mdFile.new_paragraph("``new_reference_link`` method allows you to create a link of the style: "
                     "``[mdutils][1]``. All references will be added at the end of the markdown file automatically as: \n")

mdFile.insert_code("[1]: https://github.com/didix21/mdutils", language="python")
mdFile.new_paragraph("Lets check some examples: \n")

link = "https://github.com/didix21/mdutils"

mdFile.insert_code("mdFile.write('\\n  - Reference link: ' "
                   "+ mdFile.new_reference_link(link='{}', text='mdutils', reference_tag='1')\n".format(link) +
                   "mdFile.write('\\n  - Reference link: ' "
                   "+ mdFile.new_reference_link(link='{}', text='another reference', reference_tag='md')\n".format(
                       link) +
                   "mdFile.write('\\n  - Bold link: ' "
                   "+ mdFile.new_reference_link(link='{}', text='Bold reference', reference_tag='bold', bold_italics_code='b')\n".format(
                       link) +
                   "mdFile.write('\\n  - Italics link: ' "
                   "+ mdFile.new_reference_link(link='{}', text='Bold reference', reference_tag='italics', bold_italics_code='i')\n".format(
                       link),
                   language="python")

mdFile.write("\n  - Reference link: " + mdFile.new_reference_link(link=link, text='mdutils', reference_tag='1'))
mdFile.write(
    "\n  - Reference link: " + mdFile.new_reference_link(link=link, text='another reference', reference_tag='md'))
mdFile.write("\n  - Bold link: " + mdFile.new_reference_link(link=link, text='Bold reference', reference_tag='bold',
                                                             bold_italics_code='b'))
mdFile.write(
    "\n  - Italics link: " + mdFile.new_reference_link(link=link, text='Italics reference', reference_tag='italics',
                                                       bold_italics_code='i'))

# ********************************************************************************************************************
# ************************************************** Create Lists ****************************************************
# ********************************************************************************************************************
mdFile.new_header(2, "Create Lists")
# *********************************************** Unordered Lists ****************************************************
mdFile.new_header(3, "Create unordered lists")
mdFile.new_paragraph(
    "You can add Mark down unordered list using ``mdFile.new_list(items, marked_with)``. Lets check an example: ")
items = ["Item 1", "Item 2", "Item 3", "Item 4", ["Item 4.1", "Item 4.2", ["Item 4.2.1", "Item 4.2.2"],
                                                  "Item 4.3", ["Item 4.3.1"]], "Item 5"]
mdFile.insert_code(f'items = {items}\n'
                   f'mdFile.new_list(items)')
mdFile.new_list(items=items)

# *********************************************** Ordered Lists ******************************************************
mdFile.new_header(3, "Create ordered lists")
mdFile.new_paragraph("You can add ordered ones easily, too: ``mdFile.new_list(items, marked_with='1')``")
mdFile.new_list(items=items, marked_with='1')

mdFile.new_paragraph("Moreover, you can add mixed list, for example: ")
items = ["Item 1", "Item 2", ["1. Item 2.1", "2. Item 2.2"], "Item 3"]
mdFile.insert_code(f'items = {items}\n'
                   f'mdFile.new_list(items)')
mdFile.new_list(items)
mdFile.new_paragraph("Maybe you want to replace the default hyphen ``-`` by a ``+`` or ``*`` then you can do: "
                     "``mdFile.new_list(items, marked_with='*')``.")

# *********************************************** Checkbox Lists *****************************************************
mdFile.new_header(3, "Create checkbox lists")
mdFile.new_paragraph("For creating checkbox lists you can use ``mdFile.new_checkbox_list(items)``.")
items = ["Item 1", "Item 2", ["Item 2.1", "Item 2.2"], "Item 3"]
mdFile.new_checkbox_list(items)

mdFile.new_paragraph("If you want to check all of them you can do: ``mdFile.new_checkbox_list(items, checked=True)``")
mdFile.new_checkbox_list(items, checked=True)

mdFile.new_paragraph("Or maybe you only want to check some of them, then you can add an ``x`` before each item that "
                     "you want to check: ")
items = ["Item 1", "Item 2", ["Item 2.1", "x Item 2.2"], "x Item 3"]
mdFile.insert_code(f'{items}\n'
                   'mdFile.new_checkbox_list(items)')
mdFile.new_checkbox_list(items)

# ********************************************************************************************************************
# ************************************************** Add Images ******************************************************
# ********************************************************************************************************************

mdFile.new_header(2, "Add images")

# *********************************************** Inline Image *******************************************************

image_text = "snow trees"
path = "./doc/source/images/photo-of-snow-covered-trees.jpg"

mdFile.new_header(3, "Inline Images")

mdFile.new_paragraph("You can add inline images using ``new_inline_image`` method. Method will return: "
                     "``[image](../path/to/your/image.png)``. Check the following example: ")
mdFile.insert_code("mdFile.new_line(mdFile.new_inline_image(text='{}', path='{}'))".format(image_text, path))
mdFile.new_line(mdFile.new_inline_image(text=image_text, path=path))

# *********************************************** Reference Image ****************************************************
mdFile.new_header(3, "Reference Images")
mdFile.new_paragraph("You can add inline images using ``new_reference_image`` method. Method will return: "
                     "``[image][im]``. Check the following example: ")
mdFile.insert_code(
    "mdFile.new_line(mdFile.new_reference_image(text='{}', path='{}', reference_tag='im'))".format(image_text, path))
mdFile.new_line(mdFile.new_reference_image(text=image_text, path=path, reference_tag='im'))

# ************************************************* Html Image *******************************************************

mdFile.new_header(2, "Add HTML images")

# *********************************************** Size Image *********************************************************

mdFile.new_header(3, "Change size to images")
path = "./doc/source/images/sunset.jpg"

mdFile.new_paragraph("With ``Html.image`` you can change size of images in a markdown file. For example you can do"
                     "the following for changing width: ``mdFile.new_paragraph(Html.image(path=path, size='200'))``")

mdFile.new_paragraph(Html.image(path=path, size='200'))

mdFile.new_paragraph(
    "Or maybe only want to change height: ``mdFile.new_paragraph(Html.image(path=path, size='x300'))``")
mdFile.new_paragraph(Html.image(path=path, size='x300'))

mdFile.new_paragraph("Or change width and height: ``mdFile.new_paragraph(Html.image(path=path, size='300x300'))``")
mdFile.new_paragraph(Html.image(path=path, size='300x300'))
mdFile.write('\n')

# *********************************************** Align Image *******************************************************

mdFile.new_header(3, "Align images")
mdFile.new_paragraph("Html.image allow to align images, too. For example you can run: "
                     "``mdFile.new_paragraph(Html.image(path=path, size='300x200', align='center'))``")

mdFile.new_paragraph(Html.image(path=path, size='300x200', align='center'))

# Create a table of contents
mdFile.new_table_of_contents(table_title='Contents', depth=2)
mdFile.create_md_file()
