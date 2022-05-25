# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random
# постановка задачи


def size_n(SIZE):
    MIN_ITEM = 0
    MAX_ITEM = 49
    list_out = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(2 * SIZE + 1)]
    return list_out


arr_result = size_n(5)
print(arr_result)
# Решение


def gnome_sort(arr):
    i = 1
    j = 2
    while i < len(arr):
        if arr[i - 1] < arr[i]:
            i = j
            j = j + 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i = i - 1
            if i == 0:
                i = j
                j = j + 1
        print(arr)
    return median(arr)


def median(arr):
    mid_id = int(len(arr) / 2)
    return arr[mid_id]


ar = gnome_sort(arr_result)
print(f'Медиана списка равна: {ar}')
