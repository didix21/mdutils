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

# Headers
mdFile.new_header(level=2, title="Create Headers")
mdFile.new_paragraph("Using ``new_header`` method you can create headers of different levels depending on the style."
                     "There are two available styles: 'atx' and 'setext'. The first one, it has til 6 different header "
                     "levels and levels 1 and 2 of this style are added automatically to the table of contents. The"
                     "'setext' style only has two levels of headers and they are not added to the table of contents.")
mdFile.new_paragraph()  # Add two jump lines

# Paragraph and Text format
mdFile.new_header(level=2, title="Paragraph and Text Format")
mdFile.new_paragraph("mdutils allows you to create paragraph, line breaks or simply writing text:")
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
mdFile.write('- ');  mdFile.write('bold_italics_code', bold_italics_code='bic'); mdFile.write('\n')
mdFile.write('- ');  mdFile.write('color', color='green'); mdFile.write('\n')
mdFile.write('- ');  mdFile.write('center', align='center'); mdFile.write('\n')

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

