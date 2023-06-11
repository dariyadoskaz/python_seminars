'''
Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''


def arithmetic_progression(a1, d, n):
    progression = []
    for i in range(n):
        progression.append(a1 + i * d)
    return progression

a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите шаг прогрессии: "))
n = int(input("Введите количество элементов: "))

print(arithmetic_progression(a1, d, n))


'''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)

Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
'''


def find_indexes(arr, min_val, max_val):
    indexes = []
    for i, num in enumerate(arr):
        if min_val <= num <= max_val:
            indexes.append(i)
    return indexes

arr = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_val = 5
max_val = 10


print(find_indexes(arr, min_val, max_val))



