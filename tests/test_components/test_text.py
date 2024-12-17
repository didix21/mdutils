# Python
#
# This module implements tests for Header class.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# MIT License: (C) 2024 Dídac Coll

from unittest import TestCase
from mdutils.components import Text

class TestTextClass(TestCase):
    def test_bold(self):
        """Test bold styling"""
        text = Text("Bold Text").bold()
        self.assertEqual(text.render(), "**Bold Text**")

    def test_italic(self):
        """Test italic styling"""
        text = Text("Italic Text").italic()
        self.assertEqual(text.render(), "_Italic Text_")

    def test_strikethrough(self):
        """Test strikethrough styling"""
        text = Text("Strikethrough Text").strikethrough()
        self.assertEqual(text.render(), "~~Strikethrough Text~~")

    def test_inline_code(self):
        """Test inline code styling"""
        text = Text("Inline Code").inline_code()
        self.assertEqual(text.render(), "`Inline Code`")

    def test_blockquote(self):
        """Test blockquote styling"""
        text = Text("Blockquote Text").blockquote()
        self.assertEqual(text.render(), "> Blockquote Text")

    def test_uppercase(self):
        """Test uppercase transformation"""
        text = Text("Uppercase Text").uppercase()
        self.assertEqual(text.render(), "UPPERCASE TEXT")

    def test_lowercase(self):
        """Test lowercase transformation"""
        text = Text("Lowercase Text").lowercase()
        self.assertEqual(text.render(), "lowercase text")

    def test_combined_styles(self):
        """Test combining multiple styles"""
        text = Text("Hello, Markdown!").bold().italic()
        self.assertEqual(text.render(), "_**Hello, Markdown!**_")

    def test_combined_styles_with_transformation(self):
        """Test combining styles with uppercase transformation"""
        text = Text("Important").uppercase().bold().blockquote()
        self.assertEqual(text.render(), "> **IMPORTANT**")

    def test_empty_text(self):
        """Test styling an empty string"""
        text = Text("").bold()
        self.assertEqual(text.render(), "")

    def test_no_styles(self):
        """Test rendering without any styles"""
        text = Text("Plain Text")
        self.assertEqual(text.render(), "Plain Text")

    def test_repeated_styles(self):
        """Test applying the same style multiple times"""
        text = Text("Repeated").bold().bold()
        self.assertEqual(text.render(), "**Repeated**")  # Styles shouldn't stack if redundant