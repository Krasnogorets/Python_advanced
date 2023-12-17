"""
Расстановка ферзей

Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске,
 в которой ни один ферзь не бьет другого. Другими словами, ферзи размещены таким образом,
 что они не находятся на одной вертикали, горизонтали или диагонали.

Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.
"""
import operator
import random


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


def put_the_figures():  # ф-ция подбора расстановки ферзей
    queen_num = 8
    temp_lst = []  # временное хранилище координат ферзей
    final_lst = []
    global chessboard
    for k in range(1, 9):
        k1 = random.randint(1, 8)
        for v in range(1, 9):
            v1 = random.randint(1, 8)
            clean_array()
            put_the_figure_and_fill_array(k1, v1)
            temp_lst.append((k1, v1))
            count = 0
            count_flag = 0
            while count < queen_num:
                count += 1
                flag = False
                for i in range(1, 9):
                    i1 = random.randint(1, 8)
                    if flag:
                        break
                    for j in range(1, 9):
                        j1 = random.randint(1, 8)
                        # print(k1,v1, i1, j1)
                        # print_array()
                        if not put_the_figure_and_fill_array(i1, j1):
                            continue
                        else:
                            flag = True
                            temp_lst.append((i1, j1))
                            # print(temp_lst)
                            break

                if flag:
                    count_flag += 1
                if count_flag < count:
                    break

                if count_flag == queen_num - 1:
                    clean_fig_path()

                    final_lst.append(temp_lst)
                    # print("final", final_lst)
                    return final_lst
                    # print_array()

            temp_lst.clear()

    return final_lst


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


def check_queens(lst1):
    lst = []
    for el in lst1:
        lst.append(is_attacking(el[0], el[1]))
        print(lst)

    if all(lst):
        return True
    return False


def generate_boards():  # test
    global board_list1
    flag = True
    count = 0  # счетчик вариантов правильной расстановки

    while flag:
        temp_lst = put_the_figures()
        # print(temp_lst)

        if len(board_list1) != 0 and len(temp_lst) != 0:
            if not operator.eq(set(temp_lst[0]), set(board_list1[count])):
                board_list1.append(temp_lst[0])
                count += 1
                # print('board list', board_list)
        elif len(temp_lst) != 0:
            board_list1.append(temp_lst[0])
            # print('board list', board_list)
        if count == 3:
            flag = False
        temp_lst.clear()
    return board_list1


def board():
    global board_list1
    lst = []
    for el in board_list1:
        clean_array()
        fill_the_borders()
        lst.append(check_queens(el))
        # print(lst)

    # if all(lst):
    #     return True
    return lst


board_list1 = []

clean_array()
fill_the_borders()
# put_the_figures()
# fill_the_borders()
# print_array()
# print(is_attacking(4,4))
# print(check_queens(queens))
# clean_fig_path()
# print_array()
board_list = generate_boards()
print(board_list,'\n', len(board_list))
# print(board_list)

