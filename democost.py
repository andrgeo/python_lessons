'''
Задача. Требуется вычислить значение стоимости в зависимости от условия
Предлагается решение без применения if'''

'''Используется преобразование типа при арифметической операции
и операции сравнения'''

rate = 0.12
cost = 100
cost = cost + cost * rate * (rate > 0.13)
print(cost) # 118.0


''' Задание 1
Для диапазона условие:
    если параметр больше 5 и меньше или равен 30, то (a - 5) * 1.2
    если параметр больше 30, то (a - 30) * 1.5'''


a = 28  # тестовое значение
y = (5 < a <= 30) * 1.2 * (a - 5) + (a > 30) * 1.5 * (a - 30)   # укажите требуемое выражение

print(y)

'''
def test_task(a):
    while a >= 5 and a <= 30:
        y = 1.2
        res = a * y
        return res
    else:
        y = 1.5
        res = a * y
        return res
    

print(test_task(a))
'''
''' Задание 2
Реализовать смену флага без if'''
n = 12
flag = False

def change_flag(n):
  chislo = int(n%2)
  while chislo == 0:
    flag = True
    return flag
  else:
     flag = False
     return flag

print(change_flag(n))