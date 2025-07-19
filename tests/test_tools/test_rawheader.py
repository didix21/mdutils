import unittest
from mdutils.tools.RawHeader import RawHeader
from mdutils.tools.Header import  AtxHeaderLevel, SetextHeaderLevel, HeaderStyle

class TestRawHeader(unittest.TestCase):
    def test_atx_h1(self):
        header = RawHeader.atx(AtxHeaderLevel.H1, "Title")
        self.assertEqual(header, "# Title")

    def test_atx_h3_with_id(self):
        header = RawHeader.atx(AtxHeaderLevel.H3, "Subtitle", "sub-id")
        self.assertEqual(header, "### Subtitle {#sub-id}")

    def test_setext_h1(self):
        header = RawHeader.setext(SetextHeaderLevel.H1, "Main Title")
        self.assertEqual(header, "Main Title\n" + "=" * len("Main Title"))

    def test_setext_h2(self):
        header = RawHeader.setext(SetextHeaderLevel.H2, "Section")
        self.assertEqual(header, "Section\n" + "-" * len("Section"))

    def test_header_anchor_default(self):
        anchor = RawHeader.header_anchor("Section 1")
        self.assertEqual(anchor, "[Section 1](#section-1)")

    def test_header_anchor_custom(self):
        anchor = RawHeader.header_anchor("Section 1", "custom-link")
        self.assertEqual(anchor, "[Section 1](#custom-link)")

    def test_str_atx(self):
        header = str(RawHeader(2, "Header", HeaderStyle.ATX))
        self.assertEqual(header, "## Header")

    def test_str_setext(self):
        header = str(RawHeader(2, "Header", HeaderStyle.SETEXT))
        self.assertEqual(header, "Header\n" + "-" * len("Header"))

if __name__ == "__main__":
    unittest.main()