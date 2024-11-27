# Python
#
# This module implements tests for Header class.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# MIT License: (C) 2024 Dídac Coll

from .md_component import MDComponent
from .styles import Style


class Text(MDComponent):
    """
    A class for styling and rendering Markdown-formatted text dynamically.

    Attributes:
        content (str): The text content to style.
        styles (list): A list of style functions to be applied to the content.
    """

    def __init__(self, content):
        """
        Initializes the Text instance with the provided content.

        Args:
            content (str): The text to be styled.
        """
        self.content = content
        self.styles = []

    def _add_style(self, style):
        """
        Adds a style function to the list of styles.

        Args:
            style (function): A function that applies a style to a string.

        Returns:
            Text: The current instance (for chaining).
        """

        if style not in self.styles:  # Check if the style already exists
            self.styles.append(style)
        return self

    def bold(self):
        """
        Adds bold styling to the text.

        Returns:
            Text: The current instance (for chaining).

        Example:
            text = Text("Bold Text").bold()
            print(text.render())  # Output: **Bold Text**
        """
        return self._add_style(Style.bold)

    def italic(self):
        """
        Adds italic styling to the text.

        Returns:
            Text: The current instance (for chaining).

        Example:
            text = Text("Italic Text").italic()
            print(text.render())  # Output: _Italic Text_
        """
        return self._add_style(Style.italic)

    def strikethrough(self):
        """
        Adds strikethrough styling to the text.

        Returns:
            Text: The current instance (for chaining).

        Example:
            text = Text("Strikethrough Text").strikethrough()
            print(text.render())  # Output: ~~Strikethrough Text~~
        """
        return self._add_style(Style.strikethrough)

    def inline_code(self):
        """
        Adds inline code styling to the text.

        Returns:
            Text: The current instance (for chaining).

        Example:
            text = Text("Inline Code").inline_code()
            print(text.render())  # Output: `Inline Code`
        """
        return self._add_style(Style.inline_code)

    def blockquote(self):
        """
        Formats the text as a blockquote.

        Returns:
            Text: The current instance (for chaining).

        Example:
            text = Text("Blockquote Text").blockquote()
            print(text.render())  # Output: > Blockquote Text
        """
        return self._add_style(Style.blockquote)

    def uppercase(self):
        """
        Transforms the text to uppercase.

        Returns:
            Text: The current instance (for chaining).

        Example:
            text = Text("Uppercase Text").uppercase()
            print(text.render())  # Output: UPPERCASE TEXT
        """
        return self._add_style(Style.uppercase)

    def lowercase(self):
        """
        Transforms the text to lowercase.

        Returns:
            Text: The current instance (for chaining).

        Example:
            text = Text("Lowercase Text").lowercase()
            print(text.render())  # Output: lowercase text
        """
        return self._add_style(Style.lowercase)

    def render(self):
        """
        Applies all styles and renders the styled text as a Markdown-formatted string.

        The styles are applied in the order they were added.

        Returns:
            str: The final Markdown-formatted string.

        Example:
            text = Text("Hello, Markdown!").bold().italic()
            print(text.render())
            # Output: _**Hello, Markdown!**_
        """
        if self.content == "":
            return ""

        rendered_text = self.content
        for style in self.styles:
            rendered_text = style(rendered_text)

        return rendered_text
