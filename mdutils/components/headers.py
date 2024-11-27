# Python
#
# This module implements tests for Header class.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# MIT License: (C) 2024 Dídac Coll

from .md_component import MDComponent

class H1(MDComponent):
    """
    Represents a Markdown ATX heading of level 1. # Header 1

    Attributes:
        content (str): The text content of the heading.

    Methods:
        render() -> str:
            Returns the Markdown representation of the heading.
    """
    def __init__(self, content):
        """
        Initializes the H1 instance with the provided content.

        Args:
            content (str): The text to be displayed as a level 1 heading.
        """
        self.content = content

    def render(self) -> str:
        """
        Renders the H1 content in Markdown format.

        Returns:
            str: The Markdown string for a level 1 heading.
        """
        return f"# {self.content}"


class H2(MDComponent):
    """
    Represents a Markdown ATX heading of level 2. ## Header 2

    Attributes:
        content (str): The text content of the heading.

    Methods:
        render() -> str:
            Returns the Markdown representation of the heading.
    """
    def __init__(self, content):
        """
        Initializes the H2 instance with the provided content.

        Args:
            content (str): The text to be displayed as a level 2 heading.
        """
        self.content = content

    def render(self) -> str:
        """
        Renders the H2 content in Markdown format.

        Returns:
            str: The Markdown string for a level 2 heading.
        """
        return f"## {self.content}"


class H3(MDComponent):
    """
    Represents a Markdown ATX heading of level 3. ### Header 3

    Attributes:
        content (str): The text content of the heading.

    Methods:
        render() -> str:
            Returns the Markdown representation of the heading.
    """
    def __init__(self, content):
        """
        Initializes the H3 instance with the provided content.

        Args:
            content (str): The text to be displayed as a level 3 heading.
        """
        self.content = content

    def render(self) -> str:
        """
        Renders the H3 content in Markdown format.

        Returns:
            str: The Markdown string for a level 3 heading.
        """
        return f"### {self.content}"


class H4(MDComponent):
    """
    Represents a Markdown ATX heading of level 4. #### Header 4

    Attributes:
        content (str): The text content of the heading.

    Methods:
        render() -> str:
            Returns the Markdown representation of the heading.
    """
    def __init__(self, content):
        """
        Initializes the H4 instance with the provided content.

        Args:
            content (str): The text to be displayed as a level 4 heading.
        """
        self.content = content

    def render(self) -> str:
        """
        Renders the H4 content in Markdown format.

        Returns:
            str: The Markdown string for a level 4 heading.
        """
        return f"#### {self.content}"


class H5(MDComponent):
    """
    Represents a Markdown ATX heading of level 5. ##### Header 5

    Attributes:
        content (str): The text content of the heading.

    Methods:
        render() -> str:
            Returns the Markdown representation of the heading.
    """
    def __init__(self, content):
        """
        Initializes the H5 instance with the provided content.

        Args:
            content (str): The text to be displayed as a level 5 heading.
        """
        self.content = content

    def render(self) -> str:
        """
        Renders the H5 content in Markdown format.

        Returns:
            str: The Markdown string for a level 5 heading.
        """
        return f"##### {self.content}"


class H6(MDComponent):
    """
    Represents a Markdown ATX heading of level 6. ##### Header 6

    Attributes:
        content (str): The text content of the heading.

    Methods:
        render() -> str:
            Returns the Markdown representation of the heading.
    """
    def __init__(self, content):
        """
        Initializes the H6 instance with the provided content.

        Args:
            content (str): The text to be displayed as a level 6 heading.
        """
        self.content = content

    def render(self) -> str:
        """
        Renders the H6 content in Markdown format.

        Returns:
            str: The Markdown string for a level 6 heading.
        """
        return f"##### {self.content}"

class H1Setext(MDComponent):
    """
    Represents a level 1 header in Setext style.
    """

    def __init__(self, content):
        self.content = content

    def render(self) -> str:
        """
        Renders the header as a level 1 Setext-style header.

        Returns:
            str: The Setext-style Markdown representation of a level 1 header.
        """
        underline = "=" * len(self.content)
        return f"{self.content}\n{underline}"


class H2Setext(MDComponent):
    """
    Represents a level 2 header in Setext style.
    """

    def __init__(self, content):
        self.content = content

    def render(self) -> str:
        """
        Renders the header as a level 2 Setext-style header.

        Returns:
            str: The Setext-style Markdown representation of a level 2 header.
        """
        underline = "-" * len(self.content)
        return f"{self.content}\n{underline}"