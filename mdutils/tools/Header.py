# Python
#
# This module implements a text class that allows to modify and create text on Markdown files.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# MIT License: (C) 2020 Dídac Coll


class Header:
    """Contain the main methods to define Headers on a Markdown file.

    **Features available:**

    * Create Markdown Titles: *atx* and *setext* formats are available.
    * Create Header Hanchors.
    * Auto generate a table of contents.
    * Create Tables.
    * **Bold**, *italics*, ``inline_code`` text converters.
    * Align text to center.
    * Add color to text.
    """

    # ********************************************************************
    # *                             Atx-Style                            *
    # ********************************************************************
    @staticmethod
    def atx_level_1(title: str, header_id: str = "") -> str:
        """Return a atx level 1 header.

        :param str title: text title.
        :param header_id: ID of the header for extended Markdown syntax
        :return: a header title of form: ``'\\n#' + title + '\\n'``
        :rtype: str
        """
        if len(header_id):
            header_id = " {#" + header_id + "}"

        return "\n# " + title + header_id + "\n"

    @staticmethod
    def atx_level_2(title: str, header_id: str = "") -> str:
        """Return a atx level 2 header.

        :param str title: text title.
        :param header_id: ID of the header for extended Markdown syntax
        :return: a header title of form: ``'\\n##' + title + '\\n'``
        :rtype: str
        """
        if len(header_id):
            header_id = " {#" + header_id + "}"

        return "\n## " + title + header_id + "\n"

    @staticmethod
    def atx_level_3(title: str, header_id: str = "") -> str:
        """Return a atx level 3 header.

        :param str title: text title.
        :param header_id: ID of the header for extended Markdown syntax
        :return: a header title of form: ``'\\n###' + title + '\\n'``
        :rtype: str
        """
        if len(header_id):
            header_id = " {#" + header_id + "}"

        return "\n### " + title + header_id + "\n"

    @staticmethod
    def atx_level_4(title: str, header_id: str = "") -> str:
        """Return a atx level 4 header.

        :param str title: text title.
        :param header_id: ID of the header for extended Markdown syntax
        :return: a header title of form: ``'\\n####' + title + '\\n'``
        :rtype: str
        """
        if len(header_id):
            header_id = " {#" + header_id + "}"

        return "\n#### " + title + header_id + "\n"

    @staticmethod
    def atx_level_5(title: str, header_id: str = "") -> str:
        """Return a atx level 5 header.

        :param str title: text title.
        :param header_id: ID of the header for extended Markdown syntax
        :return: a header title of form: ``'\\n#####' + title + '\\n'``
        :rtype: str
        """
        if len(header_id):
            header_id = " {#" + header_id + "}"

        return "\n##### " + title + header_id + "\n"

    @staticmethod
    def atx_level_6(title: str, header_id: str = "") -> str:
        """Return a atx level 6 header.

        :param str title: text title.
        :param header_id: ID of the header for extended Markdown syntax
        :return: a header title of form: ``'\\n######' + title + '\\n'``
        :rtype: str
        """
        if len(header_id):
            header_id = " {#" + header_id + "}"

        return "\n###### " + title + header_id + "\n"

    # ********************************************************************
    # *                          Setext-Style                            *
    # ********************************************************************
    @staticmethod
    def setext_level_1(title: str) -> str:
        """Return a setext level 1 header.

        :param str title: text title.
        :return: a header titlte of form: ``'\\n' + title +'\\n==========\\n'``.
        :rtype: str
        """

        return "\n" + title + "\n" + "".join(["=" for _ in title]) + "\n"

    @staticmethod
    def setext_level_2(title: str) -> str:
        """Return a setext level 1 header.

        :param str title: text title.
        :return: a header titlte of form: ``'\\n' + title +'\\n------------\\n'``.
        :rtype: str
        """

        return "\n" + title + "\n" + "".join(["-" for _ in title]) + "\n"

    @staticmethod
    def header_anchor(text: str, link: str = "") -> str:
        """Creates an internal link of a defined Header level 1 or level 2 in the markdown file.

        Giving a text string an text link you can create an internal link of already existing header. If the ``link``
        string does not contain '#', it will creates an automatic link of the type ``#title-1``.

        :param text: it is the text that will be displayed.
        :param link: it is the internal link.
        :return: ``'[text](#link)'``
        :type text: str
        :type link: str
        :rtype: string

        **Example:** [Title 1](#title-1)
        """
        if link:
            if link[0] != "#":
                link = link.lower().replace(" ", "-")
            else:
                link = "#" + link
        else:
            link = "#" + text.lower().replace(" ", "-")

        return "[" + text + "](" + link + ")"

    @staticmethod
    def choose_header(
        level: int, title: str, style: str = "atx", header_id: str = ""
    ) -> str:
        # noinspection SpellCheckingInspection
        """This method choose the style and the header level.

            :Examples:
            >>> from mdutils.tools.Header import Header
            >>> Header.choose_header(level=1, title='New Header', style='atx')
            '\\n# New Header\\n'

            >>> Header.choose_header(level=2, title='Another Header 1', style='setext')
            '\\nAnother Header 1\\n----------------\\n'

        :param level: Header Level, For Atx-style 1 til 6. For Setext-style 1 and 2 header levels.
        :param title: Header Title.
        :param style: Header Style atx or setext.
        :param header_id: ID of the header for extended Markdown syntax
        :return:
        """
        if style.lower() == "atx":
            if level == 1:
                return Header.atx_level_1(title, header_id)
            elif level == 2:
                return Header.atx_level_2(title, header_id)
            elif level == 3:
                return Header.atx_level_3(title, header_id)
            elif level == 4:
                return Header.atx_level_4(title, header_id)
            elif level == 5:
                return Header.atx_level_5(title, header_id)
            elif level == 6:
                return Header.atx_level_6(title, header_id)
            else:
                raise ValueError(
                    "For 'atx' style, level's expected value: 1, 2, 3, 4, 5 or 6, but level = "
                    + str(level)
                )
        elif style.lower() == "setext":
            if level == 1:
                return Header.setext_level_1(title)
            elif level == 2:
                return Header.setext_level_2(title)
            else:
                raise ValueError(
                    "For 'setext' style, level's expected value: 1, 2, 3, 4, 5 or 6, but level = "
                    + str(level)
                )
        else:
            raise ValueError(
                "style's expected value: 'atx' or 'setext', but style = "
                + style.lower()
            )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
