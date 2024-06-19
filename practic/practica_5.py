import json
from random import randint
import time
game = {}
#Ввод имен играющих
def kub_task():
    total_sum = 0
    for i in range(5):
        total = randint(1, 6)
        total_sum += total
    return total_sum
def create_gamers():
    gamers = []
    while True:
        gamer = input('Введите имя игрока: ')
        if len(gamer) == 0:
            break
        else:
            gamers.append(gamer)

def battle():
    team = create_gamers()
    for name in team:
        global game
        game[name] = kub_task()

battle()

print(game)



print(game)
'''#Моделирование бросания кубика первым играющим
print('Кубик бросает', gamer1)
time.sleep(2)
total1 = []


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

with open('../result.json', "w", encoding="utf-8") as file:
json.dumps(json_data)'''