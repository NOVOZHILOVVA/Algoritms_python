# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.

import random


# постановка задачи


def size_n(SIZE):
    MIN_ITEM = -100
    MAX_ITEM = 99
    list_out = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    return list_out


# Решение

arr_list = size_n(10)
print(arr_list)


def bubble_sort(arr):

    flag = True
    while flag:
        flag = False
        for i in range(len(arr) - 1):
            if arr_list[i] > arr_list[i + 1]:
                arr_list[i], arr_list[i + 1] = arr_list[i + 1], arr_list[i]
                flag = True

        print(arr)
    return arr_list


print(bubble_sort(arr_list))
