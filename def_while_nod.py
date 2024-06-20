﻿""" 1. Подсчет количества итераций """
k = 0   # глобальная переменная
def Countgit_1(n):
    ''' Функция как процедура, изменяющая глобальную переменную'''
    global k
    while n > 0:    # прекратить действия, когда n станет 0
        n = n//10   # Отбрасывание последней цифры числа n
        k = k + 1   # Увеличение значения переменной-счетчика

test_num = 1234568
Countgit_1(test_num) # вызов процедуры
print("Количество цифр в числе", k)  # вывод результата


def Countgit_2(n):
    ''' Функция, возвращающая значение'''
    k = 0   # локальная переменная
    while n > 0:    # прекратить действия, когда n станет 0
        n = n//10   # Отбрасывание последней цифры числа n
        k = k + 1   # Увеличение значения переменной-счетчика
    return k

test_num = 1234568

h = Countgit_2(test_num)
print("Количество цифр в числе", h)



''' Задание. Требуется реализовать алгоритм Евклида как функцию -
вариант на свое усмотрение
2. Алгоритм Евклида '''

a = int(input('Задайте первое число: '))
b = int(input('Задайте второе число: '))

def evkd (a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    nod = a
    return nod

print("Нод равен:", evkd(a, b))