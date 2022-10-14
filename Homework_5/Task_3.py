# 5 Создайте программу для игры в "Крестики-нолики".

lines_v = ['1', '2', '3']
lines_h = ['a', 'b', 'c']
p = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
n = 1
player_turn = 1
while True:
    for i in p:
        print('|'.join(i), end = '\n-----\n')
    player_turn = n%2 +1
    x, y = input(f'Ход {player_turn} игрока. Введите координаты через пробел, q - выход').split()
    if x == 'q':
        break
    if not x.isdigit() and not y.isdigit or 0 < int(x) < 4 or 0 < int(y) < 4:
        continue
    n = n + 1

