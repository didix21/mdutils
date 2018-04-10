# ! Python
#
#  This file is part of mdutils. https://github.com/didix21/mdutils
# (C) 2018 Dídac Coll
"""Module **mdutils**

The different features availables are:
    * Create Heades, Til 6 sub-lvels.
    * Auto generate a table of contents.
    * Create List and sub-list.
    * Create paragraph.
    * Generate tables of different sizes.
    * Insert Links.
    * Insert Images.
    * Insert Code.
"""
from mdutils.fileutils.fileutils import NewFile


class Header(object):
    """Contain the main methods to define Headers on a Markdown file."""
    @staticmethod
    def level_1(title):
        return '# ' + title

    @staticmethod
    def level_2(title):
        return '\n\n## ' + title

    @staticmethod
    def level_3(title):
        return '\n\n### ' + title

    @staticmethod
    def level_4(title):
        return '\n\n#### ' + title

    @staticmethod
    def level_5(title):
        return '\n\n##### ' + title

    @staticmethod
    def level_6(title):
        return '\n\n###### ' + title


class TableOfContents(object):
    def _loop_trought(self, elements, tab=''):
        """Method that go trough a list of elements that contain strings and other list and return a string \
        reade to be written inside a markdown file in order to create a table of contents.

        - **elements**: contain all the headers defined on the main class.
        - **tab:** Inserts tabulations."""
        elements_to_string = ""
        for item in elements:
            if isinstance(item, list):
                if item != []:
                    if tab == '\t':
                        elements_to_string += self._loop_trought(item, tab='\t\t')
                    else:
                        elements_to_string += self._loop_trought(item, tab='\t')
            else:
                elements_to_string += '\n' + tab + '* [' + item + '](#' + item.lower().replace(' ', '-') + ')'

        return elements_to_string

    def create_table_of_contents(self, array_of_title_contents):
        table_of_contents = "\n\n"
        table_of_contents += self._loop_trought(array_of_title_contents)

        return table_of_contents


class MdUtils:
    def __init__(self, file_name, title="", author=""):
        self.file_name = file_name
        self.title = title
        self.author = author
        self.header = Header()
        self.markdown_file = self.create_md_file()
        self._table_titles = []

    def create_md_file(self):
        md_file = NewFile(self.file_name)
        md_file.rewrite_all_file(data=self.header.level_1(self.title))
        return md_file

    def new_header(self, level, title):
        if level == 1:  # Check header's level
            return self.header.level_1(title)
        elif level == 2:
            self._add_new_item_table_of_content(level, title)  # Add Header level 2 to print in a table of contents
            self.markdown_file.append_end(self.header.level_2(title))
        elif level == 3:
            self._add_new_item_table_of_content(level, title)  # Add Header level 3 to print in a table of contents
            self.markdown_file.append_end(self.header.level_3(title))
        elif level == 4:
            self._add_new_item_table_of_content(level, title)  # Add Header level 4 to print in a table of contents
            self.markdown_file.append_end(self.header.level_4(title))
        elif level == 5:
            self.markdown_file.append_end(self.header.level_5(title))
        elif level == 6:
            self.markdown_file.append_end(self.header.level_6(title))

    def _add_new_item_table_of_content(self, level, item):
        if level == 2:
            self._table_titles.append(item)
            self._table_titles.append([])
        elif level == 3:
            self._table_titles[-1].append(item)
            self._table_titles[-1].append([])
        elif level == 4:
            self._table_titles[-1][-1].append(item)
            self._table_titles[-1][-1].append([])
        elif level == 5:
            self._table_titles[-1][-1][-1].append(item)
            self._table_titles[-1][-1][-1].append([])
        elif level == 6:
            self._table_titles[-1][-1][-1][-1].append(item)

    def new_table_of_contents(self):
        table = TableOfContents().create_table_of_contents(self._table_titles)
        self.markdown_file.append_end(table)


if __name__ == '__main__':
    heeader = Header()
