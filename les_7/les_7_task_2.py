# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы

import random
# постановка задачи


def size_n(SIZE):
    MIN_ITEM = 0
    MAX_ITEM = 49
    list_out = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    return list_out


# Решение
arr_list = size_n(10)
print(arr_list)


def merge_ssort(arr):

    if len(arr) <= 1:
        return arr

    mid_arr = int(len(arr) / 2)
    left, right = merge_ssort(arr[mid_arr:]), merge_ssort(arr[:mid_arr])

    return merge(left, right)


def merge(left, right):
    result = []
    left_id = right_id = 0

    while left_id < len(left) and right_id < len(right):

        if left[left_id] < right[right_id]:
            result.append(left[left_id])
            left_id += 1
        else:
            result.append(right[right_id])
            right_id += 1

    result.extend(left[left_id:])
    result.extend(right[right_id:])
    
    return result


arr_result = merge_ssort(arr_list)
print(arr_result)
