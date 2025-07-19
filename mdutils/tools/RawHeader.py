from enum import Enum
from Header import HeaderStyle, AtxHeaderLevel, SetextHeaderLevel
from typing import Optional

class RawHeader:
    """Header generator without leading or trailing newlines."""

    def __init__(self, level: int, title: str, style: HeaderStyle, header_id: Optional[str] = None) -> None:
        self.level = level
        self.title = title
        self.style = style
        self.header_id = header_id

    def __str__(self) -> str:
        return self._new(self.level, self.title, self.style, self.header_id)

    @staticmethod
    def atx(level: AtxHeaderLevel, title: str, header_id: Optional[str] = None) -> str:
        header_id = RawHeader._get_header_id(header_id)
        return "#" * level.value + " " + title + header_id

    @staticmethod
    def setext(level: SetextHeaderLevel, title: str) -> str:
        if level == SetextHeaderLevel.H1:
            separator = "="
        else:
            separator = "-"
        return title + "\n" + separator * len(title)

    @staticmethod
    def header_anchor(text: str, link: Optional[str] = None) -> str:
        if not link:
            link = "#" + text.lower().replace(" ", "-")
        elif link[0] != "#":
            link = link.lower().replace(" ", "-")
        else:
            link = "#" + link
        return "[" + text + "](" + link + ")"

    def _new(self, level: int, title: str, style: HeaderStyle = HeaderStyle.ATX, header_id: Optional[str] = None) -> str:
        if style == HeaderStyle.ATX:
            return RawHeader.atx(AtxHeaderLevel(level), title, header_id)
        elif style == HeaderStyle.SETEXT:
            return RawHeader.setext(SetextHeaderLevel(level), title)
        else:
            raise ValueError("style's expected value: 'HeaderStyle.ATX' or 'HeaderStyle.SETEXT'")

    @staticmethod
    def _get_header_id(header_id: Optional[str] = None) -> str:
        if header_id:
            return " {#" + header_id + "}"
        return ""

if __name__ == "__main__":
    # Example usage
    print(str(RawHeader(1, "Example Header", HeaderStyle.ATX)))
    print(str(RawHeader(2, "Example Subheader", HeaderStyle.SETEXT)))