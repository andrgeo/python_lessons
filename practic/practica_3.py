import math
import statistics
from statistics import median
import random

numbers = []

for i in range(0, 10):
    number = random.randint(0, 100)
    numbers.append(number)

print(numbers)

sum_numbers = sum(numbers)
medium = sum(numbers) / len(numbers)
mediana = median(numbers)
stdev = statistics.stdev(numbers)

print("Сумма: ", sum_numbers)
print("Среднее значение: ", medium)
print("Медиана: ", mediana)
print("Стандартное отклонение: ", stdev)

print("Случайное число: ", random.choice(numbers))
print("Случайное число 2: ", random.sample(numbers, 3))