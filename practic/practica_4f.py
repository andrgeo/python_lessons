import os

folder = "/Users/ekaterina/PycharmProjects/python_lessons/PythonPrim/Textfiles"
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

file_n = folder + "/2.txt"
