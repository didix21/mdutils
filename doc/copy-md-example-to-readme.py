#!/usr/bin/python3

from mdutils.fileutils.fileutils import MarkdownFile
from pathlib import Path


readme_path = "../README.md"
readme_content = MarkdownFile.read_file(readme_path)
readme = MarkdownFile(readme_path)
markdown_example = MarkdownFile.read_file("./source/examples/Example_Markdown.md")
replace_index = readme_content.find("Markdown File Example\n=====================")
new_readme = readme_content[:replace_index] + markdown_example
readme.write(new_readme)

