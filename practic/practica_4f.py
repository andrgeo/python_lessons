import os
#1
'''folder = "/Users/ekaterina/PycharmProjects/python_lessons/PythonPrim/Textfiles"
answ = set()
search = input("Что найти?: ")

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    with open(filepath, 'r') as fp:
        for line in fp:
            if search in line:
                answ.add(filename)

for i in answ:
    print(i)
#2
filename1 = open("/Users/ekaterina/PycharmProjects/python_lessons/PythonPrim/Textfiles/4.txt")

lines = 0
words = 0
symbols = 0

for line in filename1:
    lines += 1
    words += len(line.split())
    symbols += len(line)

print("Input file contains::",'\n', symbols, "letters",'\n',words, "words",'\n', lines, "lines")

'''
#3
from pathlib import Path
home = Path.cwd()
my_folder = home / "my_folder"
if not my_folder.exists():
    my_folder.mkdir()

file1 = my_folder / "file1.png"
file1.touch()

(my_folder / "images").mkdir(exist_ok=True)

for f in my_folder.glob('*.png'):
    path_destination = Path(my_folder / "images") / f.name
    f.replace(path_destination)

print(home)


#4
''' Задание расположено в папке /practic/pr_4_4'''