'''Project 1_5B
Указания:
• для каждой задачи данного раздела сначала создаются функции, а затем,
используя их, выполняется решение задачи;
• ввод и вывод данных для функции необходимо обеспечить самостоятельно;
• для каждой написанной функции нужно использовать строки документации;
• при выводе вещественных результатов оставьте два знака после запятой.
Задания:
1. Дан список температурных изменений в течение дня (целые числа). Известно,
что измеряющее устройство иногда сбоит и записывает отсутствие
температуры (значение None). Выведите среднюю температуру за
наблюдаемый промежуток времени, предварительно очистив список от
неопределенных значений. Гарантируется, что хотя бы одно определенное
значение в списке есть.
2. Напишите функцию, которая принимает неограниченное количество
числовых аргументов и возвращает кортеж из двух списков: отрицательных
значений (отсортирован по убыванию); неотрицательных значений
(отсортирован по возрастанию).
3. Составьте две функции для возведения числа в степень: один из вариантов
реализуйте в рекурсивном стиле.'''

# 1
import random

temp_list = [4, 19, 35, None, -13, -21, -1, 1, 28, 24, -4, None, -7, -27, -39, -4, -8, -16, None, -19, -39, 45, 27, -7]
temp_list_clear = []

for i in temp_list:
    if i == None:
        temp_list.remove(i)
    else:
        temp_list_clear.append(i)

def mid_temp_period(templist, st_hours, end_hours):
    temp_range = templist[st_hours:end_hours]
    mid_temp = "{:.2f}".format(sum(temp_range) / len(temp_range))
    return mid_temp

h_1 = int(input("Введите час начала измерений: "))
h_2 = int(input("Введите час конца измерений: "))

mdt = mid_temp_period(temp_list_clear, h_1, h_2)
print("Средняя температура за период =", mdt)

# 2

# Тестовый список
numbers = []
for i in range(100):
    n = random.randint(-100, 100)
    numbers.append(n)
def sort_func(hueta):
    over_zero = []
    under_zero = []
    for i in hueta:
        if i >= 0:
            over_zero.append(i)
        elif i < 0:
            under_zero.append(i)

    s_overzero = sorted(over_zero)
    s_underzero = sorted(under_zero, reverse=True)

    res = (list(s_underzero),  list(over_zero))
    print(res)

sort_func(numbers)

# 3.1
num1 = 4
num2 = 2
def expon (a, b):
    c = a ** b
    print(c)

expon(num1, num2)


# 3.2

def expon1(a,b):
    if b == 1:
        return a
    if b != 1:
        return (a * expon1(a, b -1))
    print("Результат возведения в степень равен:", expon1(a,b))

res = expon1(num1,num2)

print(res)