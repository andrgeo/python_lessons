import json
from random import randint
import time
#Ввод имен играющих
gamer1 = input('Введите имя 1-го играющего ')
gamer2 = input('Введите имя 2-го играющего ')
#Моделирование бросания кубика первым играющим
print('Кубик бросает', gamer1)
time.sleep(2)
total1 = []
for i in range(5):
    n1 = randint(1, 6)
    total1.append(n1)

game_total_1 = sum(total1)

print('Выпало:', game_total_1)

#Моделирование бросания кубика вторым играющим
print('Кубик бросает', gamer2)
time.sleep(2)
total2 = []
for i in range(5):
    n2 = randint(1, 6)
    total2.append(n2)

game_total_2 = sum(total2)

print('Выпало:', game_total_2)

#Определение результата (3 возможных варианта)
if game_total_1 > game_total_2:
  print('Выиграл', gamer1)
elif game_total_1 < game_total_2:
  print('Выиграл', gamer2)
else:
  print('Ничья')

gamer1_result = {'name': gamer1, 'result': game_total_1}

json_data = json.dumps(gamer1_result)

with open('result.json', "w", encoding="utf-8") as file:
    json.dumps(json_data)