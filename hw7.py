"""

Задание 1. Новые списки

Даны три списка:
1. floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
2. names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
3. numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

Напишите код, который создаёт три новых списка. Вот их содержимое:
1. Каждое число из списка floats возводится в третью степень и округляется
до трёх знаков после запятой.
2. Из списка names берутся только имена минимум из пяти букв.
3. Из списка numbers берётся произведение всех чисел.

"""

floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]

new_floats = list(map(lambda num: round(num ** 3, 3), floats))
print (new_floats)


names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]

new_names = list(filter(lambda name: len(name) >= 5, names))
print (new_names)

numbers = [22, 33, 10, 6894, 11, 2, 1]

from math import prod
product_numbers = prod(numbers)

print(product_numbers)

from functools import reduce
new_numbers = reduce(lambda x, y: x * y, numbers)

print(new_numbers)


"""
Задача 2. Zip
Даны список букв (letters) и список цифр (numbers). Каждый список состоит из N элементов. Создайте кортежи из пар элементов списков и запишите их в список
results. Не используйте функцию zip. Решите задачу в одну строку (не считая print(results)).

Примеры списков:
letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

Результат работы программы:
[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

"""

letters = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

results = list(zip(letters, numbers))

print(results)

"""
Задача 3. Палиндром

Используя модуль collections, реализуйте функцию can_be_poly, которая принимает на вход строку и проверяет, можно ли получить из неё палиндром.

Пример кода:
print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))

Результат:
True
False

"""

from collections import Counter

def can_be_poly(s: str) -> bool:
    counts = Counter(s)
    odd_count = len(list(filter(lambda count: count % 2 != 0, counts.values())))
    return odd_count <= 1

print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))