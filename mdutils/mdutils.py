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
    @staticmethod
    def level_1(title):
        return '# ' + title

    @staticmethod
    def level_2(title):
        return '## ' + title

    @staticmethod
    def level_3(title):
        return '### ' + title

    @staticmethod
    def level_4(title):
        return '#### ' + title

    @staticmethod
    def level_5(title):
        return '##### ' + title

    @staticmethod
    def level_6(title):
        return '###### ' + title


class MdUtils:
    def __init__(self, file_name, title="", author=""):
        self.file_name = file_name
        self.title = title
        self.author = author
        self.header = Header()
        self.create_md_file()
        self._table_titles = []

    def create_md_file(self):
        md_file = NewFile(self.file_name)
        md_file.rewrite_all_file(data=self.header.level_1(self.title))

    def new_header(self, level, title):
        if level == 1:
            return self.header.level_1(title)
        elif level == 2:
            self._add_new_item_table_of_content(title)
            return self.header.level_2(title)
        elif level == 3:
            self._add_new_item_table_of_content(title)
            return self.header.level_3(title)
        elif level == 4:
            self._add_new_item_table_of_content(title)
            return self.header.level_4(title)
        elif level == 5:
            self._add_new_item_table_of_content(title)
            return self.header.level_5(title)
        elif level == 6:
            self._add_new_item_table_of_content(title)
            return self.header.level_6(title)

    def _add_new_item_table_of_content(self, item):
        self._table_titles.append(item)
        self._table_titles[-1].append([])


if __name__ == '__main__':
    heeader = Header()
