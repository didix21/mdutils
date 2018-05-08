# Python
#
# This file implements an example.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# MIT License: (C) 2018 Dídac Coll


from mdutils.mdutils import MdUtils

mdFile = MdUtils(file_name='Example', title='This is a Markdown File Example')

mdFile.new_header(level=1, title='Overview')    # style is set 'atx' format by default.

mdFile.new_paragraph("This is an example of markdown file created using mdutils python package. In this example you"
                     "are going to see how to create a markdown file using this library. Moreover, you're "
                     "finding the available features which makes easy create this type of files while you are running"
                     "python code.")
mdFile.new_paragraph()

# Available Features
mdFile.new_header(level=1, title="What you can do")

# ********************************************************************************************************************
# ***************************************************** Markdown *****************************************************
# ********************************************************************************************************************
mdFile.new_header(level=2, title="Create Markdown files")
mdFile.new_paragraph("It is the last command that has to be called.")
mdFile.insert_code("import Mdutils\n"
                   "\n"
                   "\n"
                   "mdFile = MdUtils(file_name=\'Example\',title=\'This is a Markdown File Example\')\n"
                   "mdFile.create_md_file()", language='python')

# ********************************************************************************************************************
# ***************************************************** Headers ******************************************************
# ********************************************************************************************************************
mdFile.new_header(level=2, title="Create Headers")
mdFile.new_paragraph("Using ``new_header`` method you can create headers of different levels depending on the style."
                     "There are two available styles: 'atx' and 'setext'. The first one, it has til 6 different header "
                     "levels and levels 1 and 2 of this style are added automatically to the table of contents. The"
                     "'setext' style only has two levels of headers and they are not added to the table of contents.")

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
mdFile.new_paragraph("If you have defined some headers of level 1 and 2, you can create a table of contents invoking"
                     "the following command (Normally, the method will be called at the end of the code before calling"
                     "``create_md_file()``)")
mdFile.insert_code("mdFile.new_table_of_contents(table_title='Contents', depth=2)", language='python')

# ********************************************************************************************************************
# ******************************************** Paragraph and Text format *********************************************
# ********************************************************************************************************************
mdFile.new_header(level=2, title="Paragraph and Text Format")
mdFile.new_paragraph("mdutils allows you to create paragraph, line breaks or simply writing text:")

mdFile.insert_code("mdFile.new_paragraph(Using ``new_paragraph`` method you can add very easily a new paragraph \n"
                   "\t\t\ton your markdown file. This example of paragraph has been added using this method. Moreover,\n"
                   "\t\t\t``new_paragraph`` method make your live easy because it can give format to the text. Lets \n"
                   "\t\t\tsee an example:)", language='python')

mdFile.new_paragraph("Using ``new_paragraph`` method you can add very easily a new paragraph on your markdown file. "
                     "This example of paragraph has been added using this method. Moreover, ``new_paragraph`` method "
                     "make your live easy because it can give format to the text. Lets see an example:")
mdFile.new_paragraph("This is an example of text in which has been added color, bold and italics text.",
                     bold_italics_code='bi', color='purple')

mdFile.new_paragraph("mdutils has a method which can create new line breaks. Lets see it.")
mdFile.new_line("This is an example of line break which has been created with ``new_line`` method.")
mdFile.new_paragraph("As ``new_paragraph``, ``new_line`` allows users to give format to text using "
                     "``bold_italics_code`` and ``color`` parameters:")
mdFile.new_line("This is an inline code which contains bold and italics text and it is centered",
                bold_italics_code='cib', align='center')

mdFile.new_paragraph("''write'' method write text in markdown file without jump lines ('\\n') and as ``new_paragraph`` "
                     "and ``new_line`` using the arguments ``bold_italics_code``, ``color`` and ``align`` you can"
                     "give format to text: ")
mdFile.write("The following text has been written with ``write`` method. You can use markdown directives to write: "
             "**bold**, _italics_, ``inline_code``... or ")
mdFile.write("use the following available parameters:  \n")

mdFile.write('- ')
mdFile.write('bold_italics_code', bold_italics_code='bic')
mdFile.write(" <---------------------------------  ``mdFile.write('bold_italics_code', bold_italics_code='bic')``")
mdFile.write('\n')
mdFile.write('- ')
mdFile.write('color', color='green')
mdFile.write(" <---------------------------------  ``mdFile.write('color', color='green')``")
mdFile.write('\n')
mdFile.write('- ')
mdFile.write('center', align='center')
mdFile.write(" <-----------  ``mdFile.write('center', align='center')``")
mdFile.write('\n')

mdFile.new_header(2, "Create a Table")
mdFile.new_paragraph("The library implements a method called ``new_table`` that can create table using a list of "
                     "strings. This method only needs, the number of rows and columns that your table must have.")
list_of_strings = ["Items", "Descriptions", "Data"]
for x in range(5):
    list_of_strings.extend(["Item " + str(x), "Description Item " + str(x), str(x)])
mdFile.new_line()
mdFile.new_table(columns=3, rows=6, text=list_of_strings)

# Create a table of contents
mdFile.new_table_of_contents(table_title='Contents', depth=2)

mdFile.create_md_file()

