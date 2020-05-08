#!/usr/bin/python3

from mdutils.fileutils.fileutils import MarkDownFile
from pathlib import Path


readme_path = "../README.md"
readme_content = MarkDownFile.read_file(readme_path)
readme = MarkDownFile(readme_path)
markdown_example = MarkDownFile.read_file("./source/examples/Example_Markdown.md")
replace_index = readme_content.find("Markdown File Example\n=====================")
new_readme = readme_content[:replace_index] + markdown_example
readme.rewrite_all_file(new_readme)

