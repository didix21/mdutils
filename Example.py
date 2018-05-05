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

mdFile.new_header(level=1, title="What you can do")
mdFile.new_header(level=2, title="Create Headers")
mdFile.new_paragraph("Using ``new_header`` method you can create headers of different levels depending on the style."
                     "There are two available styles: 'atx' and 'setext'.")

mdFile.new_paragraph("The first one, it has til 6 different header"
                     "levels and levels 1 and 2 of this style are added automatically to the table of contents. ")

# Create a table of contents
mdFile.new_table_of_contents(table_title='Contents', depth=2)

mdFile.create_md_file()

