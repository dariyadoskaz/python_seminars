"""

Задание 1. Три списка
Даны три списка.
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

Нужно выполнить две задачи:
1. найти элементы, которые есть в каждом списке;
2. найти элементы из первого списка, которых нет во втором и третьем списках.

Каждую задачу нужно выполнить двумя способами:
1. без использования множеств;
2. с использованием множеств.

Пример выполнения на других данных:
array_1 = [1, 2, 3, 4]
array_2 = [2, 4]
array_3 = [2, 3]
Вывод:
Задача 1:
Решение без множеств: 2
Решение с множествами: 2
Задача 2:
Решение без множеств: 1
Решение с множествами: 1

"""

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Решение без использования множеств
common_elements = []

for element in array_1:
    if element in array_2 and element in array_3:
        common_elements.append(element)

print("Задача 1 (без множеств):", common_elements)


# Решение без использования множеств
unique_elements = []

for element in array_1:
    if element not in array_2 and element not in array_3:
        unique_elements.append(element)

print("Задача 2 (без множеств):", unique_elements)


# Решение задачи 2
# Решение с использованием множеств
common_elements_set = set(array_1) & set(array_2) & set(array_3)

print("Задача 1 (с множествами):", list(common_elements_set))


unique_elements_set = set(array_1) - set(array_2) - set(array_3)

print("Задача 2 (с множествами):", list(unique_elements_set))


"""
Задача Расстояние необязательная

Надо вычислить расстояние между 2 точками в пространстве любой размерности. 
На входе два списка с координатами точек, на выходе одно число.

"""

import math


point1 = [1, 2, 3]
point2 = [4, 5, 6]

def calculate_distance(point1, point2):
    # Проверка, что точки имеют одинаковую размерность
    if len(point1) != len(point2):
        raise ValueError("Точки должны иметь одинаковую размерность.")

    # Вычисление суммы квадратов разностей соответствующих координат
    sum_of_squares = sum((coord2 - coord1) ** 2 for coord1, coord2 in zip(point1, point2))

    # Вычисление корня из суммы квадратов
    distance = math.sqrt(sum_of_squares)

    return distance

result = calculate_distance(point1, point2)
print("Расстояние между точками:", result)
