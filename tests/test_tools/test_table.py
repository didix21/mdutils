# Python
#
# This module implements tests for Table class.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# MIT License: (C) 2018 Dídac Coll

from unittest import TestCase
from mdutils.tools.Table import Table
from mdutils.mdutils import MdUtils

__author__ = 'didix21'
__project__ = 'MdUtils'


class TestTable(TestCase):
    def test_create_centered_table(self):
        md_file = MdUtils("file_name")
        table = Table()
        result_table = '\n|**Test**|**Descripción**|**Estado**|\n| :---: | :---: | :---: ' \
                       '|\n|Test 1|Carga de configuración correcta|<font color="green">OK</font>|\n' \
                       '|Test 2|Lectura de Configuración|<font color="red">NOK</font>|\n' \
                       '|Test 3|Lectura de Soporte|<font color="green">OK</font>|\n' \
                       '|Test 4|Modificación de entradas y lectura de salidas de cantón|<font color="green">' \
                       'OK</font>|'\
                       '\n|Test 5|Lectura de estados de Pedal de Rearme y Aviso|<font color="green">OK</font>|\n' \
                       '|Test 6|Actualización de datos de unidades de vía|<font color="green">OK</font>|\n' \
                       '|Test 7|Fallos en carga de configuración - Campo IdApp Erróneo|<font color="green">' \
                       'OK</font>|' \
                       '\n' \
                       '|Test 8|Fallos en carga de configuración - Campo VersTAbla Erróneo' \
                       '|<font color="red">NOK</font>|'\
                       '\n|Test 9|Fallos en carga de configuración - Campo IdUc Erróneo|<font color="red">' \
                       'NOK</font>|' \
                       '\n|Test 10|Fallos en carga de configuración - Campo Addresses Erróneo' \
                       '|<font color="red">NOK</font>|\n' \
                       '|Test 11|Fallos en carga de configuración - Campo NumTc Erróneo' \
                       '|<font color="red">NOK</font>|\n' \
                       '|Test 12|Fallos en carga de configuración - Campo NumUv Erróneo' \
                       '|<font color="red">NOK</font>|\n' \
                       '|Test 13|Fallos en carga de configuración - Campo CRC Erróneo|<font color="red">NOK</font>|\n'

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

        self.assertEqual(table.create_table(columns=3, rows=14, text=text_array, text_align='center'), result_table)

    def test_create_default_table(self):
        md_file = MdUtils("file_name")
        table = Table()
        result_table = '\n|**Test**|**Descripción**|**Estado**|\n| --- | --- | --- ' \
                       '|\n|Test 1|Carga de configuración correcta|<font color="green">OK</font>|\n' \
                       '|Test 2|Lectura de Configuración|<font color="red">NOK</font>|\n' \
                       '|Test 3|Lectura de Soporte|<font color="green">OK</font>|\n' \
                       '|Test 4|Modificación de entradas y lectura de salidas de cantón|<font color="green">' \
                       'OK</font>|'\
                       '\n|Test 5|Lectura de estados de Pedal de Rearme y Aviso|<font color="green">OK</font>|\n' \
                       '|Test 6|Actualización de datos de unidades de vía|<font color="green">OK</font>|\n' \
                       '|Test 7|Fallos en carga de configuración - Campo IdApp Erróneo|<font color="green">' \
                       'OK</font>|' \
                       '\n' \
                       '|Test 8|Fallos en carga de configuración - Campo VersTAbla Erróneo' \
                       '|<font color="red">NOK</font>|'\
                       '\n|Test 9|Fallos en carga de configuración - Campo IdUc Erróneo|<font color="red">' \
                       'NOK</font>|' \
                       '\n|Test 10|Fallos en carga de configuración - Campo Addresses Erróneo' \
                       '|<font color="red">NOK</font>|\n' \
                       '|Test 11|Fallos en carga de configuración - Campo NumTc Erróneo' \
                       '|<font color="red">NOK</font>|\n' \
                       '|Test 12|Fallos en carga de configuración - Campo NumUv Erróneo' \
                       '|<font color="red">NOK</font>|\n' \
                       '|Test 13|Fallos en carga de configuración - Campo CRC Erróneo|<font color="red">NOK</font>|\n'

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

        self.assertEqual(table.create_table(columns=3, rows=14, text=text_array), result_table)

    def test_column_row_does_not_much_text_length_array(self):
        md_file = MdUtils("file_name")
        table = Table()
        text_array = ['**Test**', '**Descripción**', '**Estado**',
                      'Test 1', 'Carga de configuración correcta', md_file.textUtils.text_color("OK", 'green'),
                      'Test 2', 'Lectura de Configuración', md_file.textUtils.text_color("NOK", 'red'),
                      'Test 3', 'Lectura de Soporte', md_file.textUtils.text_color("OK", 'green')]

        self.assertRaises(ValueError, table.create_table, 3, 14, text_array)

    def test_invalid_text_align(self):
        md_file = MdUtils("file_name")
        table = Table()
        text_array = ['**Test**', '**Descripción**', '**Estado**',
                      'Test 1', 'Carga de configuración correcta', md_file.textUtils.text_color("OK", 'green'),
                      'Test 2', 'Lectura de Configuración', md_file.textUtils.text_color("NOK", 'red'),
                      'Test 3', 'Lectura de Soporte', md_file.textUtils.text_color("OK", 'green')]

        self.assertRaises(ValueError, table.create_table, 3, 14, text_array, 'invalid_align')

