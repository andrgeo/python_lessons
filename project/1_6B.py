'''Создайте сценарий, который использует список имен файлов CSV в качестве
источника для копирования содержимого этих файлов в плоский файл. Текущая дата
и время должны быть добавлены к имени файла в качестве префикса перед
копированием. Каждая операция копирования должна быть записана в файл журнала
на локальном компьютере. Исключения для файлов, которые не были найдены,
также должны быть записаны в журнал.
Пояснение к заданию:
На входе программы должен быть список имён файлов CSV, сами файлы произвольно
содержания, например те, с которыми вы уже работали. Программа должна принять список,
скопировать содержимое каждого из них в текстовый файл (на ваше усмотрение в
отдельные файлы или общий, идея - должна быть копия данных, в задании только есть
требование к имени этого файла).
При выполнении копировании информацию об этом
программа сохраняет в файле журнала. Может возникнуть ситуация, при которой
некоторых файлов из исходного списка не окажется, тогда нужно это учесть в программе с
помощью механизма обработки исключений - если файла нет, то в файл журнал нужно
сделать запись, что файл не найден.'''

from pathlib import Path
import datetime
import csv
import asposecells
from asposecells.api import Workbook

my_folder = Path.cwd()

files_list = ["new_orderdate.csv", "orderdata_sample.csv", "new.csv"]
counter = 0
for f in files_list:
    workbook = Workbook(my_folder/f)
    if workbook


