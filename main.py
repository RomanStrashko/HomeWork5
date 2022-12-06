#1. Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. Первый ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота ""интеллектом""

# from random import randint
#
# def data(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x
#
#
# def print1(name, k, counter, value):
#     print(f"Вы взяли {k} конфет. На столе осталось {value} конфет.")
#
# def print2(name, k, counter, value):
#     print(f"Был ход {name}, он взял {k} конфет. Осталось на столе {value} конфет.")
#
#
# player1 = input("Введите имя первого игрока: ")
# player2 = 'computer'
# value = int(input("Введите количество конфет на столе: "))
# priority = randint(0, 2)  # флаг очередности
# if priority:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
#
# counter1 = 0
# counter2 = 0
#
# while value > 28:
#     if priority:
#         k = data(player1)
#         counter1 += k
#         value -= k
#         priority = False
#         print1(player1, k, counter1, value)
#         print()
#     else:
#         k = randint(1, 28)
#         counter2 += k
#         value -= k
#         priority = True
#         print2(player2, k, counter2, value)
#         print()
#
# if priority:
#     print(f"Поздравляю Вас {player1}! Вы выиграли!!!")
# else:
#     print(f"ВЫИГРАЛ {player2}!")





#2. Создайте программу для игры в ""Крестики-нолики"".


# print('Начало игры в КРЕСТИКИ-НОЛИКИ!')
#
# board = list(range(1, 10))
#
# def g_board(board):
#     print('-'*13)
#     for i in range(3):
#         print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
#         print('-'*13)
#
#
#
# def choice(tic_tac):
#     valid = False
#     while not valid:
#         player_index = input('Ваш ход, выберите ячейку ' + tic_tac + ' --> ')
#         try:
#             player_index =int(player_index)
#         except:
#             print('Что то не то нажали')
#             continue
#         if player_index >= 1 and player_index <= 9:
#             if(str(board[player_index-1]) not in 'XO'):
#                 board[player_index-1] = tic_tac
#                 valid = True
#             else:
#                 print('Занято')
#         else:
#             print('Еще раз попробуй')
#
# def victory(board):
#     v = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
#                (0, 3, 6), (1, 4, 7), (2, 5, 8),
#                (0, 4, 8), (2, 4, 6))
#     for i in v:
#         if board[i[0]] == board[i[1]] == board[i[2]]:
#             return board[i[0]]
#     return False
#
# def game(board):
#     counter =0
#     vic = False
#     while not vic:
#         g_board(board)
#         if counter % 2 == 0:
#             choice('X')
#         else:
#             choice('0')
#         counter +=1
#         if counter > 4:
#             win = victory(board)
#             if win:
#                 print(win, 'Победа!!!')
#                 vic = True
#                 break
#             if counter == 9:
#                 print('НИЧЬЯ')
#         g_board(board)
#
# game(board)




#3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.

t = input("Введите текст: ")


with open('text.txt', 'w', encoding='UTF-8') as data:
    data.writelines(t)



def compres(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def recov(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res



print(f"Текст после сжатия: {compres(t)}")

with open('text2.txt', 'w', encoding='UTF-8') as data:
    data.writelines(compres(t))


print(f"Текст после восставления: {recov(compres(t))}")










