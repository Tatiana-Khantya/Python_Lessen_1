# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from operator import truediv
import random

total_sweets = 100
player_turn = True
int_bot = 0

def correct_logic(arg_int):
    target = 29
    if arg_int == target:
        return target - 1
    elif arg_int < target:
        return arg_int
    else:
        return arg_int - target



while total_sweets > 28:
    if player_turn:
        int_player = int(input('Сколько конфет возьмет первый игрок?  '))
        # if 28 >= int_player <= 1:
        #     int_player = 13
        print(f'игрок взял = {int_player}')
        total_sweets -= int_player
        player_turn = False
        print(f'конфет осталось = {total_sweets}')
    else:
        if total_sweets <= 56:
            int_bot = correct_logic(total_sweets)
            print(f'бот взял = {int_bot}')
            total_sweets -= int_bot
            player_turn = True
            print(f'конфет осталось = {total_sweets}')
        else:
            int_bot = random.randrange(1,28)
            print(f'бот взял = {int_bot}')
            total_sweets -= int_bot
            player_turn = True
            print(f'конфет осталось = {total_sweets}')
if player_turn == True:
    print(f'победил игрок = конфет осталось {total_sweets}')
else:
    print(f'победил AI = конфет осталось {total_sweets}')

