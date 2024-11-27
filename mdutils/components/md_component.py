# Python
#
# This module implements tests for Header class.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# MIT License: (C) 2024 Dídac Coll

class MDComponent(object):
    """
    A base class for Markdown components.
    This class is intended to be inherited by other Markdown elements.
    """
    def render(self) -> str:
        """
       Renders the Markdown content. This should be overridden by subclasses.

       Returns:
           str: The Markdown representation of the component.
        """
        raise NotImplementedError("Render method must be implemented by subclass")