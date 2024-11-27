# Python
#
# This module implements tests for Header class.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# MIT License: (C) 2024 Dídac Coll

from mdutils.components import H1, H2, H3, H4, H5, H6, H1Setext, H2Setext
from unittest import TestCase

class TestMarkdownHeadings(TestCase):
    def test_h1_render(self):
        """Test rendering of H1"""
        heading = H1("Heading 1")
        self.assertEqual(heading.render(), "# Heading 1")

    def test_h2_render(self):
        """Test rendering of H2"""
        heading = H2("Heading 2")
        self.assertEqual(heading.render(), "## Heading 2")

    def test_h3_render(self):
        """Test rendering of H3"""
        heading = H3("Heading 3")
        self.assertEqual(heading.render(), "### Heading 3")

    def test_h4_render(self):
        """Test rendering of H4"""
        heading = H4("Heading 4")
        self.assertEqual(heading.render(), "#### Heading 4")

    def test_h5_render(self):
        """Test rendering of H5"""
        heading = H5("Heading 5")
        self.assertEqual(heading.render(), "##### Heading 5")

    def test_h6_render(self):
        """Test rendering of H6"""
        heading = H6("Heading 6")
        self.assertEqual(heading.render(), "##### Heading 6")

    def test_empty_content(self):
        """Test rendering with empty content"""
        heading = H1("")
        self.assertEqual(heading.render(), "# ")

    def test_special_characters(self):
        """Test rendering with special characters in content"""
        heading = H2("Special *chars* _here_")
        self.assertEqual(heading.render(), "## Special *chars* _here_")

    def test_numeric_content(self):
        """Test rendering with numeric content"""
        heading = H3("12345")
        self.assertEqual(heading.render(), "### 12345")

    def test_long_content(self):
        """Test rendering with long content"""
        content = "This is a very long heading with multiple words and characters"
        heading = H4(content)
        self.assertEqual(heading.render(), f"#### {content}")

    def test_h1_setext_render(self):
        """Test rendering of H1Setext"""
        h1 = H1Setext("Header Level 1")
        self.assertEqual(h1.render(), "Header Level 1\n==============")

    def test_h2_setext_render(self):
        """Test rendering of H2Setext"""
        h2 = H2Setext("Header Level 2")
        self.assertEqual(h2.render(), "Header Level 2\n--------------")

    def test_h1_empty_content(self):
        """Test H1Setext with empty content"""
        h1 = H1Setext("")
        self.assertEqual(h1.render(), "\n")

    def test_h2_empty_content(self):
        """Test H2Setext with empty content"""
        h2 = H2Setext("")
        self.assertEqual(h2.render(), "\n")

    def test_h1_special_characters(self):
        """Test H1Setext with special characters"""
        h1 = H1Setext("Special *chars* _here_!")
        self.assertEqual(h1.render(), "Special *chars* _here_!\n=======================")

    def test_h2_special_characters(self):
        """Test H2Setext with special characters"""
        h2 = H2Setext("Special *chars* _here_!")
        self.assertEqual(h2.render(), "Special *chars* _here_!\n-----------------------")

    def test_h1_numeric_content(self):
        """Test H1Setext with numeric content"""
        h1 = H1Setext("1234567890")
        self.assertEqual(h1.render(), "1234567890\n==========")

    def test_h2_numeric_content(self):
        """Test H2Setext with numeric content"""
        h2 = H2Setext("1234567890")
        self.assertEqual(h2.render(), "1234567890\n----------")

    def test_h1_long_content(self):
        """Test H1Setext with long content"""
        content = "This is a very long header with multiple words and characters"
        h1 = H1Setext(content)
        self.assertEqual(h1.render(), f"{content}\n{'=' * len(content)}")

    def test_h2_long_content(self):
        """Test H2Setext with long content"""
        content = "This is a very long header with multiple words and characters"
        h2 = H2Setext(content)
        self.assertEqual(h2.render(), f"{content}\n{'-' * len(content)}")


if __name__ == "__main__":
    unittest.main()