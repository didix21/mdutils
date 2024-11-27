
class Style:
    @staticmethod
    def bold(text: str) -> str:
        """Bold text style.

        :param text: a text string.
        :type text: str
        :return: a string like this example: ``'**text**'``
        :rtype: str"""
        return f"**{text}**"

    @staticmethod
    def italic(text: str) -> str:
        """Italics text style.

        :param text: a text string.
        :type text: str
        :return: a string like this example: ``'_text_'``
        :rtype: str"""
        return f"_{text}_"

    @staticmethod
    def strikethrough(text: str) -> str:
        """Strikethrough text style.

        :param text: a text string.
        :type text: str
        :return: a string like this example: ``'~~text~~'``
        :rtype: str"""
        return f"~~{text}~~"

    @staticmethod
    def inline_code(text: str) -> str:
        """Inline code text converter.

        :param text: a text string.
        :type text: str
        :return: a string like this example: ``'``text``'``
        :rtype: str"""
        return f"`{text}`"

    @staticmethod
    def blockquote(text: str) -> str:
        """Blockquote text style.

        :param text: a text string.
        :type text: str
        :return: a string like this example: ``'> text'``
        :rtype: str"""
        return f"> {text}"

    @staticmethod
    def uppercase(text: str) -> str:
        return text.upper()

    @staticmethod
    def lowercase(text: str) -> str:
        return text.lower()