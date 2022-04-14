print('КРЕСТИКИ - НОЛИКИ\n'
      'инструкция по игре:\n'
      'перед вами игровое поле с координатами,\n'
      'ввод координат следует осуществлять в формате\n'
      '"вертикаль - горизонталь" через пробел\n'
      'пример: "1 2"(без ковычек).\n'
      'первым ходит Х, вторым О.\n'
      'приятной игры!')

def print_table(t): #выводим таблицу
    print('  0 1 2')
    for i in range(len(table)):
        print(str(i) + ' ' + ' '.join(table[i]))


def player_int(t, player): #ввод игрока
    while True:
        place = input(f"Ход игрока {player} \nВведите координаты:").split()
        if len(place) != 2:
            print('Введите две координаты')
            continue

        if not(place[0].isdigit() and place[1].isdigit()):
            print('Введите числа')
            continue
        x, y = map(int, place)
        if not(x >= 0 and x <= 2 and y >= 0 and  y <= 2):
            print('Вышли из диапазона')
            continue
        if t[x][y] != '-':
            print('Клетка занята')
            continue
        break
    return x, y

def win(t, player): #комбинации выигрыша
    def win_line(a1, a2, a3, player):
        if a1 == player and a2 == player and a3 == player:
            return True
    for n in range(3):
        if \
        win_line(t[n][0], t[n][1], t[n][2], player) or \
        win_line(t[0][n], t[1][n], t[2][n], player) or \
        win_line(t[0][0], t[1][1], t[2][2], player) or \
        win_line(t[2][0], t[1][1], t[0][2], player):
            return True
    return False

def begin_play(table): #начало игры и условия

    count = 0
    while True:
        print_table(table)
        if count % 2 == 0:
            player = 'Х'
        else:
            player = 'О'
        if count < 9:
            x, y = player_int(table, player)
            table[x][y] = player

        elif count == 9:
            print ('Ничья')
            break
        if win(table, player):
            print_table(table)
            print(f"Выиграл {player}")
            break
        count += 1


table = [['-'] * 3 for _ in range(3)]

begin_play(table)