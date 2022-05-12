""" Во втором массиве сохранить индексы четных элементов первого массива. Например, если
 дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1,
4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого
массива стоят четные числа."""
# постановка задачи
import random
import timeit
import cProfile

def size_n(SIZE):
    MIN_ITEM = 0
    MAX_ITEM = 100
    list_out = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    return list_out


# Версия решения for in range:


def f_1(n):
    m = []
    a = len(n)
    for i in range(a):
        if n[i] % 2 == 0:
            m.append(i)
    return m


# Версия решения с while:


def f_2(n):
    m = []
    a = len(n)
    while a > 0:
        if n[a - 1] % 2 == 0:
            m.append(a - 1)
        a -= 1
    return m


# Версия решения при помощи рекурсии:


def f_3(n, m=None):
    if m is None:
        m = []
    a = len(n)
    if a > 0 and (n[a - 1] % 2 == 0):
        m.append(a - 1)
        n.pop()
        return f_3(n, m)
    elif a > 0:
        n.pop()
        return f_3(n, m)
    else:
        return m

print(f_1([1, 2, 3, 4, 5, 6]), f_2([1, 2, 3, 4, 5, 6]), f_3([1, 2, 3, 4, 5, 6]))

# Анализ скорости и сложности версия 1:


"""
print(timeit.timeit('f_1(size_n(200))', number=1000, globals=globals()))      # 0.15490800000043237
print(timeit.timeit('f_1(size_n(400))', number=1000, globals=globals()))      # 0.3090025000019523
print(timeit.timeit('f_1(size_n(800))', number=1000, globals=globals()))      # 0.5525477000010142
print(timeit.timeit('f_1(size_n(1600))', number=1000, globals=globals()))     # 1.0474734999988868
print(timeit.timeit('f_1(size_n(3200))', number=1000, globals=globals()))     # 2.102291100000002
print(timeit.timeit('f_1(size_n(6400))', number=1000, globals=globals()))     # 4.408374200000253
print(timeit.timeit('f_1(size_n(12_800))', number=1000, globals=globals()))   # 8.15747360000023
print(timeit.timeit('f_1(size_n(25_600))', number=1000, globals=globals()))   # 16.46297429999686
print(timeit.timeit('f_1(size_n(51_200))', number=1000, globals=globals()))   # 33.262635999999475
print(timeit.timeit('f_1(size_n(102_400))', number=1000, globals=globals()))  # 66.31941349999397
print(timeit.timeit('f_1(size_n(204_800))', number=1000, globals=globals()))  # 136.09494539999287
print(timeit.timeit('f_1(size_n(409_600))', number=1000, globals=globals()))  # 273.2859224999993
print(timeit.timeit('f_1(size_n(819_200))', number=1000, globals=globals()))  # 559.4918541999941
"""


cProfile.run('f_1(size_n(6_400_000))')
"""
 56142458 function calls in 16.513 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.036    0.036   16.512   16.512 <string>:1(<module>)
        1    0.000    0.000   14.969   14.969 les_4_task_1.py:10(size_n)
        1    1.694    1.694   14.969   14.969 les_4_task_1.py:13(<listcomp>)
        1    1.220    1.220    1.507    1.507 les_4_task_1.py:32(f_2)
  6400000    3.275    0.000    4.424    0.000 random.py:239(_randbelow_with_getrandbits)
  6400000    5.616    0.000   11.393    0.000 random.py:292(randrange)
  6400000    1.883    0.000   13.275    0.000 random.py:366(randint)
 19200000    1.352    0.000    1.352    0.000 {built-in method _operator.index}
        1    0.000    0.000   16.512   16.512 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
  3231242    0.286    0.000    0.286    0.000 {method 'append' of 'list' objects}
  6400000    0.465    0.000    0.465    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  8111209    0.685    0.000    0.685    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

# Анализ скорости и сложности версия 2:

"""
print(timeit.timeit('f_2(size_n(200))', number=1000, globals=globals()))      # 0.15179169999828446
print(timeit.timeit('f_2(size_n(400))', number=1000, globals=globals()))      # 0.2896928999980446
print(timeit.timeit('f_2(size_n(800))', number=1000, globals=globals()))      # 0.5772604999983741
print(timeit.timeit('f_2(size_n(1600))', number=1000, globals=globals()))     # 1.3192389999967418
print(timeit.timeit('f_2(size_n(3200))', number=1000, globals=globals()))     # 2.255835500000103
print(timeit.timeit('f_2(size_n(6400))', number=1000, globals=globals()))     # 4.626227500000823
print(timeit.timeit('f_2(size_n(12_800))', number=1000, globals=globals()))   # 8.857322399999248
print(timeit.timeit('f_2(size_n(25_600))', number=1000, globals=globals()))   # 18.057196399997338
print(timeit.timeit('f_2(size_n(51_200))', number=1000, globals=globals()))   # 35.94849660000182
print(timeit.timeit('f_2(size_n(102_400))', number=1000, globals=globals()))  # 72.10911250000936
print(timeit.timeit('f_2(size_n(204_800))', number=1000, globals=globals()))  # 146.63921189999382
print(timeit.timeit('f_2(size_n(409_600))', number=1000, globals=globals()))  # 299.5772066000063
print(timeit.timeit('f_2(size_n(819_200))', number=1000, globals=globals()))  # 601.9676946999971
"""

cProfile.run('f_2(size_n(6_400_000))')
"""
         56145252 function calls in 16.793 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.036    0.036   16.793   16.793 <string>:1(<module>)
        1    0.000    0.000   15.251   15.251 les_4_task_1.py:10(size_n)
        1    1.808    1.808   15.251   15.251 les_4_task_1.py:13(<listcomp>)
        1    1.222    1.222    1.505    1.505 les_4_task_1.py:32(f_2)
  6400000    3.294    0.000    4.453    0.000 random.py:239(_randbelow_with_getrandbits)
  6400000    5.729    0.000   11.544    0.000 random.py:292(randrange)
  6400000    1.900    0.000   13.444    0.000 random.py:366(randint)
 19200000    1.362    0.000    1.362    0.000 {built-in method _operator.index}
        1    0.000    0.000   16.793   16.793 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
  3232183    0.283    0.000    0.283    0.000 {method 'append' of 'list' objects}
  6400000    0.471    0.000    0.471    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  8113062    0.688    0.000    0.688    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

# Анализ скорости и сложности версия 3:


print(timeit.timeit('f_3(size_n(200))', number=1000, globals=globals()))    # 0.37740529999427963, при N = 200
print(timeit.timeit('f_3(size_n(400))', number=1000, globals=globals()))    # 0.41777519999595825, при N = 400
print(timeit.timeit('f_3(size_n(800))', number=1000, globals=globals()))    # 0.692809500003932, при N = 800
# print(timeit.timeit('f_3(size_n(1600))', number=1000, globals=globals()))  Последующее увеличение N приводит
# print(timeit.timeit('f_3(size_n(3200))', number=1000, globals=globals()))  к переполнению стека
# print(timeit.timeit('f_3(size_n(6400))', number=1000, globals=globals()))
# print(timeit.timeit('f_3(size_n(12800))', number=1000, globals=globals()))

cProfile.run('f_3(size_n(800))')
""" 
9426 function calls (8626 primitive calls) in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.000    0.000    0.002    0.002 les_4_task_1.py:10(size_n)
        1    0.000    0.000    0.002    0.002 les_4_task_1.py:13(<listcomp>)
    801/1    0.001    0.000    0.001    0.001 les_4_task_1.py:45(f_3)
      800    0.001    0.000    0.001    0.000 random.py:239(_randbelow_with_getrandbits)
      800    0.001    0.000    0.002    0.000 random.py:292(randrange)
      800    0.000    0.000    0.002    0.000 random.py:366(randint)
     2400    0.000    0.000    0.000    0.000 {built-in method _operator.index}
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
      801    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      389    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
      800    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1030    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
      800    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects} 
"""

# Выводы анализа скорости и сложности:
"""
В результате проведенного анализа трех версий решения задачи, наихудшим показало решение с рекурсивным алгоритмом.
С увеличением N рекурсивная функция вызывается большое количество раз, что приводит к переполнению стека.
При сравнении решения 1 (for) и решения 2 (while) показатели timeit сравнительно одинаковые, но при большем N скорость 
выполения у решения 1 (for) выполняется несколько быстрее. При выполнении инструмента cProfile показатели сравнимы.
"""