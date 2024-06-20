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

current_folder = Path.cwd()
my_folder = current_folder / "1_6B_files"
cur_date = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M")
backup_file = str(cur_date) + "-backup.txt"
(my_folder / backup_file).touch(exist_ok=True)

f_for_log = my_folder / "files_copy.log"
f_for_log.touch(exist_ok=True)


files_list = ["new_orderdate.csv", "orderdata_sample.csv", "new.csv"]

def read_file (file):
    with open(my_folder / f, 'r') as inp_file:
        data = inp_file.read()
        return data

def wrond_log(file, log_file):
    with open(log_file, 'a') as log_file:
        log_file.write(str(cur_date) + " " + "невыполнено копирование данных файла:" + " " + file + '\n')

def right_log(file, log_file):
    with open(log_file, 'a') as log_file1:
        log_file1.write(str(cur_date) + " " + "выполнено копирование данных файла:" + " " + file + '\n')

def copy_data (data, file):
    with open(file, 'w') as back_file:
        back_file.write(data)


for f in files_list:
    try:
        file = my_folder / f
        data = read_file(file)
        '''with open(my_folder / f, 'r') as inp_file:
            data = inp_file.read()'''
    except FileNotFoundError:
        print("Невозможно открыть файл", f)
        wrond_log(f, f_for_log)
        '''with open(my_folder / "files_copy.log", 'a') as log_file:
            log_file.write(str(cur_date) + " " + "невыполнено копирование данных файла:" + " " + f + '\n')'''
        continue

    copy_data(data, file)
    '''with open(my_folder / backup_file, 'w') as back_file:
        back_file.write(data)'''
    right_log(f, f_for_log)
    '''with open(my_folder/ "files_copy.log", 'a') as log_file1:
        log_file1.write(str(cur_date) + " " + "выполнено копирование данных файла:" + " " + f + '\n')'''
