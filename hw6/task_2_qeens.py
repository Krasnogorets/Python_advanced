"""
Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и heck_queens(queens),
 которая проверяет все возможные пары ферзей.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка
 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.
# """
# queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
queens = [(4, 4)]

chessboard = [[0] * 10 for i in range(10)]


def print_array():
    global chessboard
    for row in chessboard:
        for elem in row:
            print(elem, end=" ")
        print()
    print()


def put_the_figure_and_fill_array(row, col):
    global chessboard
    if chessboard[row][col] == 0:
        chessboard[row][col] = 2
        row1 = row
        col1 = col
        flag_horizon_right = True
        while flag_horizon_right:
            if chessboard[row1][col1 + 1] == 2:
                return False
            elif chessboard[row1][col1 + 1] <= 1:
                chessboard[row1][col1 + 1] = 1
                col1 += 1
            else:
                row1 = row
                col1 = col
                flag_horizon_right = False
        flagdiagonal_right_down = True
        while flagdiagonal_right_down:
            if chessboard[row1 + 1][col1 + 1] == 2:
                return False
            elif chessboard[row1 + 1][col1 + 1] <= 1:
                chessboard[row1 + 1][col1 + 1] = 1
                col1 += 1
                row1 += 1
            else:
                row1 = row
                col1 = col
                flagdiagonal_right_down = False
        flag_down = True
        while flag_down:
            if chessboard[row1 + 1][col1] == 2:
                return False
            elif chessboard[row1 + 1][col1] <= 1:
                chessboard[row1 + 1][col1] = 1
                row1 += 1
            else:
                row1 = row
                col1 = col
                flag_down = False
        flag_down_left = True
        while flag_down_left:
            if chessboard[row1 + 1][col1 - 1] == 2:
                return False
            elif chessboard[row1 + 1][col1 - 1] <= 1:
                chessboard[row1 + 1][col1 - 1] = 1
                col1 -= 1
                row1 += 1
            else:
                row1 = row
                col1 = col
                flag_down_left = False
        flag_left = True
        while flag_left:
            if chessboard[row1][col1 - 1] == 2:
                return False
            elif chessboard[row1][col1 - 1] <= 1:
                chessboard[row1][col1 - 1] = 1
                col1 -= 1
            else:
                row1 = row
                col1 = col
                flag_left = False
        flagdiagonal_left_up = True
        while flagdiagonal_left_up:
            if chessboard[row1 - 1][col1 - 1] == 2:
                return False
            elif chessboard[row1 - 1][col1 - 1] <= 1:
                chessboard[row1 - 1][col1 - 1] = 1
                col1 -= 1
                row1 -= 1
            else:
                row1 = row
                col1 = col
                flagdiagonal_left_up = False
        flag_up = True
        while flag_up:
            if chessboard[row1 - 1][col1] == 2:
                return False
            elif chessboard[row1 - 1][col1] <= 1:
                chessboard[row1 - 1][col1] = 1
                row1 -= 1
            else:
                row1 = row
                col1 = col
                flag_up = False
        flagdiagonal_right_up = True
        while flagdiagonal_right_up:
            if chessboard[row1 - 1][col1 + 1] == 2:
                return False
            elif chessboard[row1 - 1][col1 + 1] <= 1:
                chessboard[row1 - 1][col1 + 1] = 1
                col1 += 1
                row1 -= 1
            else:
                row1 = row
                col1 = col
                flagdiagonal_right_up = False

        return True
    else:
        return False


def fill_the_borders():  # заполение границ символом 3
    global chessboard
    row = 0
    col = 0
    for i in range(0, 40):
        if i <= 9:
            chessboard[row][col] = 3
            col += 1
        elif 10 <= i <= 19:
            col = 9
            chessboard[row][col] = 3
            row += 1
        elif 20 < i <= 30:
            row = 9
            chessboard[row][col] = 3
            col -= 1
        elif 30 < i <= 39:
            col = 0
            chessboard[row][col] = 3
            row -= 1


# def put_the_figures():
#     global chessboard
#     for k in range(1, 9):
#         for v in range(1, 9):
#             clean_array()
#             put_the_figure_and_fill_array(k, v)
#             count = 0
#             count_flag = 0
#             while count < 8:
#                 count += 1
#                 flag = False
#                 for i in range(1, 9):
#                     if flag:
#                         break
#                     for j in range(1, 9):
#                         if not put_the_figure_and_fill_array(i, j):
#                             continue
#                         else:
#                             flag = True
#                             break
#
#                 if flag:
#                     count_flag += 1
#                 if count_flag < count:
#                     break
#
#                 if count_flag == 7:
#                     clean_fig_path()
#                     # print_array()
#
#     return


def clean_array():  # ф-ция очистки массива
    global chessboard
    for i in range(1, 9):
        for j in range(1, 9):
            chessboard[i][j] = 0


def clean_fig_path():  # ф-ция очистки пути фигуры (при проверке путь заполняется символом 1)
    global chessboard
    for i in range(1, 9):
        for j in range(1, 9):
            if chessboard[i][j] == 1:
                chessboard[i][j] = 0


def is_attacking(q1, q2):
    if put_the_figure_and_fill_array(q1, q2):
        return True
    else:
        return False
    # print_array()


def check_queens(queens):
    lst = []
    for el in queens:
        lst.append(is_attacking(el[0], el[1]))
        print(lst)

    if all(lst):
        return True
    return False


# print("3 - границы массива, 2 - ферзи")
# print()
# print("  готовая расстановка ферзей:")
# print()
clean_array()
fill_the_borders()
# put_the_figures()
# fill_the_borders()
# print_array()
# print(is_attacking(4,4))
print(check_queens(queens))
# clean_fig_path()
print_array()
