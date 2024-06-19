import json
from random import randint
import time

game = {}


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
    return gamers

def battle():
    team = create_gamers()
    total = []
    for name in team:
        print("Игрок", name, "бросает кубик!")
        time.sleep(2)
        result = kub_task()
        if result in total:
            print("Результат:", result)
            print("Такой результат уже есть, переброс")
            result = kub_task()
            print("Новый результат", result)
            total.append(result)
        else:
            print("Результат:", result)
            total.append(result)
            global game
            game[name] = result
    return total

def who_win(total_p):
    st = 0
    winner = str()
    if len(total_p) > 2:
        st = max(total_p)
    else:
        if len(set(total_p)) == 1:
            print("Ничья!")
        else:
            st = max(total_p)
    for key, values in game.items():
        if values == st:
            winner = key

    print("Победил игрок:", winner, "С результатом:", st)
    return

who_win(battle())
