from unittest import TestCase
from mdutils.tools.tools import Table
from mdutils.mdutils import MdUtils


class TestTable(TestCase):
    def test_create_table(self):
        md_file = MdUtils("file_name")
        table = Table()
        result_table = '\n|**Test**|**Descripción**|**Estado**|\n| :---: | :---: | :---: ' \
                       '|\n|Test 1|Carga de configuración correcta|<font color="green"> OK </font>|\n' \
                       '|Test 2|Lectura de Configuración|<font color="red"> NOK </font>|\n' \
                       '|Test 3|Lectura de Soporte|<font color="green"> OK </font>|\n' \
                       '|Test 4|Modificación de entradas y lectura de salidas de cantón|<font color="green"> ' \
                       'OK </font>|'\
                       '\n|Test 5|Lectura de estados de Pedal de Rearme y Aviso|<font color="green"> OK </font>|\n' \
                       '|Test 6|Actualización de datos de unidades de vía|<font color="green"> OK </font>|\n' \
                       '|Test 7|Fallos en carga de configuración - Campo IdApp Erróneo|<font color="green"> ' \
                       'OK </font>|' \
                       '\n' \
                       '|Test 8|Fallos en carga de configuración - Campo VersTAbla Erróneo' \
                       '|<font color="red"> NOK </font>|'\
                       '\n|Test 9|Fallos en carga de configuración - Campo IdUc Erróneo|<font color="red"> ' \
                       'NOK </font>|' \
                       '\n|Test 10|Fallos en carga de configuración - Campo Addresses Erróneo' \
                       '|<font color="red"> NOK </font>|\n' \
                       '|Test 11|Fallos en carga de configuración - Campo NumTc Erróneo' \
                       '|<font color="red"> NOK </font>|\n' \
                       '|Test 12|Fallos en carga de configuración - Campo NumUv Erróneo' \
                       '|<font color="red"> NOK </font>|\n' \
                       '|Test 13|Fallos en carga de configuración - Campo CRC Erróneo|<font color="red"> NOK </font>|\n'

        text_array = ['**Test**', '**Descripción**', '**Estado**',
                      'Test 1', 'Carga de configuración correcta', md_file.textUtils.text_color("OK", 'green'),
                      'Test 2', 'Lectura de Configuración', md_file.textUtils.text_color("NOK", 'red'),
                      'Test 3', 'Lectura de Soporte', md_file.textUtils.text_color("OK", 'green'),
                      'Test 4', 'Modificación de entradas y lectura de salidas de cantón',
                      md_file.textUtils.text_color("OK", 'green'),
                      'Test 5', 'Lectura de estados de Pedal de Rearme y Aviso',
                      md_file.textUtils.text_color("OK", 'green'),
                      'Test 6', 'Actualización de datos de unidades de vía',
                      md_file.textUtils.text_color("OK", 'green'),
                      'Test 7', 'Fallos en carga de configuración - Campo IdApp Erróneo',
                      md_file.textUtils.text_color("OK", 'green'),
                      'Test 8', 'Fallos en carga de configuración - Campo VersTAbla Erróneo',
                      md_file.textUtils.text_color("NOK", 'red'),
                      'Test 9', 'Fallos en carga de configuración - Campo IdUc Erróneo',
                      md_file.textUtils.text_color("NOK", 'red'),
                      'Test 10', 'Fallos en carga de configuración - Campo Addresses Erróneo',
                      md_file.textUtils.text_color("NOK", 'red'),
                      'Test 11', 'Fallos en carga de configuración - Campo NumTc Erróneo',
                      md_file.textUtils.text_color("NOK", 'red'),
                      'Test 12', 'Fallos en carga de configuración - Campo NumUv Erróneo',
                      md_file.textUtils.text_color("NOK", 'red'),
                      'Test 13', 'Fallos en carga de configuración - Campo CRC Erróneo',
                      md_file.textUtils.text_color("NOK", 'red')]

        self.assertEqual(table.create_table(columns=3, rows=13, text=text_array), result_table)

