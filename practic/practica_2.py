
# 1. Составьте программу в которой объявите две строковые переменные
string1 = " This is a string. "
string2 = " This is another string."

# 2. Проверьте работу операции «+» со строками.
string3 = string1 + string2
print(string3)

# 3

print(len(string1), string1.lower(), string1.upper(), string1.rstrip(), string1.lstrip(), string1.strip(), string1.strip('.'), sep="|")

# 4

d = "qwerty"
ch = d[2]

print(ch)

# 5

list1 = [3, 4, 5, 6, 7, 8, 9, 0, 1]
sl = list1[3:6]

print(sl)

# 6

sl1 = list1[1:]
sl2 = list1[:3]
sl3 = list1[:]
sl4 = list1[1:5:2]

print(sl1, sl2, sl3, sl4)

# 7
list1[2] = 'o'
print(list1)

# Работа с числами

# 1

a = 22
b = 3

c = a / b
d = a % b
e = a ** b

print(c, d, e)

# 2

param = "string" + str(15)

print(param)

# 3

n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", n3)

# 4

a = 1/3
print("{:7.3f}".format(a))

# 5

a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))

# Списки

#1
list1 = [82,8,23,97,92,44,17,39,11,12]

#4. Измените значения элементов списка (по вашему усмотрению) с помощью
list1[3] = 43

#5. Добавьте новый элемент в конец списка.

list1.append(88)

#6. Добавьте новый элемент в произвольную (на ваше усмотрение) позицию
list1.insert(3, 67)

#7. Удалите элемент из списка по известной позиции.

list1.pop(4)

#8. Удалите последний элемент из списка

list1.pop(-1)

# Сортировка элементов списка

# 1 

list1.sort(reverse=True)

# 2
lis1 = list1.sorted()

# 3
list2 = [3,5,6,2,33,6,11]

# 4
lis2 = sorted(list2)

#5. Проверьте содержимое исходного и отсортированного списков.

print(lis1, lis2)

#Кортежи

#3

seq = (2,8,23,97,92,44,17,39,11,12)

# 4
seq.count(8)
seq.index(44)

#5. Преобразуйте кортеж к типу «список»:
listseq = list(seq)

print(listseq)

#6. С помощью команды type(listseq) проверьте правильность преобразования.

print(type(listseq))

#Словари

# 1
 
dict1 = {‘food’: ‘Apple’, ‘quantity’: 4, ‘color’: ‘Red’}

# 2

dict1[‘food’]
dict1[‘quantity’] += 10

# 3. Создайте пустой словарь:
dp = {}
''''''

#1. Создайте словарь, реализующий требуемую структуру:

rec = {‘name’: {‘firstname’: ‘Bob’, ‘lastname’: ‘Smith’},‘job’: [‘dev’, ‘mgr’],‘age’: 25}

#2. Реализуйте вывод значения полного имени, отдельно имени firstname,
#список должностей.

print("Полное имя: ", dict1['name'], dict1['lastname'])
print("Имя: ", dict1['name'])
print("До: ", dict1['job'])

#3. Напишите инструкцию, расширяющую список должностей, например:

rec[‘job’].append(‘janitor’)

#4. Выведите полную информацию о персоне.