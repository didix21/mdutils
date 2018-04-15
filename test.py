from mdutils.mdutils import MdUtils

md_file = MdUtils(file_name='Test', title='Test Title')

text_array = ['**Test**', '**Descripción**', '**Estado**',
              'Test 1', 'Carga de configuración correcta', md_file.textUtils.text_color("OK", 'green'),
              'Test 2', 'Lectura de Configuración', md_file.textUtils.text_color("NOK", 'red'),
              'Test 3', 'Lectura de Soporte', md_file.textUtils.text_color("OK", 'green'),
              'Test 4', 'Modificación de entradas y lectura de salidas de cantón', md_file.textUtils.text_color("OK", 'green'),
              'Test 5', 'Lectura de estados de Pedal de Rearme y Aviso', md_file.textUtils.text_color("OK", 'green'),
              'Test 6', 'Actualización de datos de unidades de vía', md_file.textUtils.text_color("OK", 'green'),
              'Test 7', 'Fallos en carga de configuración - Campo IdApp Erróneo', md_file.textUtils.text_color("OK", 'green'),
              'Test 8', 'Fallos en carga de configuración - Campo VersTAbla Erróneo', md_file.textUtils.text_color("NOK", 'red'),
              'Test 9', 'Fallos en carga de configuración - Campo IdUc Erróneo', md_file.textUtils.text_color("NOK", 'red'),
              'Test 10', 'Fallos en carga de configuración - Campo Addresses Erróneo', md_file.textUtils.text_color("NOK", 'red'),
              'Test 11', 'Fallos en carga de configuración - Campo NumTc Erróneo', md_file.textUtils.text_color("NOK", 'red'),
              'Test 12', 'Fallos en carga de configuración - Campo NumUv Erróneo', md_file.textUtils.text_color("NOK", 'red'),
              'Test 13', 'Fallos en carga de configuración - Campo CRC Erróneo', md_file.textUtils.text_color("NOK", 'red'),
              'Test 14', 'Fallos en carga de configuración - Campo IdTc Erróneo', md_file.textUtils.text_color("NOK", 'red')]


md_file.new_header(1, "Results Tests")
print(repr(md_file.create_table(3, 15, text_array)))
md_file.new_header(1, "Test Details")
md_file.add_new_paragraph("All test will be written at the following lines.")
md_file.new_header(2, "Test 1")
md_file.new_header(2, "Test 2")
md_file.new_header(2, "Test 3")
md_file.new_header(3, "Test 3.0")
md_file.new_header(4, "Test 3.0.0")
md_file.new_header(4, "Test 3.0.1")
md_file.new_header(3, "Test 3.1")
md_file.new_header(2, "Test 4")

print(repr(md_file.new_table_of_contents()))

md_file.create_md_file()
