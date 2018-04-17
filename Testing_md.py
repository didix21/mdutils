from mdutils.mdutils import MdUtils

md_file = MdUtils("Testing_md", title="Testing Tables")
text_array = ["Test", "Description", "State", "Test 1", "Carga de configuración correcta", "OK"]

md_file.create_md_file()
md_file.markdown_file.append_end('\n\n')
md_file.create_table(3, 3, text_array)


