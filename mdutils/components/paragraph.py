# Python
#
# This module implements tests for Header class.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# MIT License: (C) 2024 Dídac Coll

from .md_component import MDComponent

class Paragraph(MDComponent):
    """
    A class representing a Markdown paragraph composed of child components.

    This class is designed to group multiple Markdown components or text elements
    into a single paragraph, rendering them as a unified Markdown block.

    Attributes:
        children (tuple): A collection of child components or strings to be included
                          in the paragraph.
    """

    def __init__(self, *children):
        """
        Initializes the Paragraph instance with the given child components.

        Args:
            *children: A variable-length argument list of child components or strings
                       that make up the content of the paragraph.

        Example:
            text1 = Text("Hello World, ")
            text2 = Text("Another Hello World")
            paragraph = Paragraph(text1, text2)
            # Creates a paragraph containing two text components.
        """
        self.children = children

    def render(self):
        return "\n" + "".join(child.render() for child in self.children)