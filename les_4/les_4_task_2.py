# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

# Первый — с помощью алгоритма «Решето Эратосфена» .
import timeit
import cProfile


def sieve_method(n):
    sieve = list(range(n * 100))
    sieve[1] = 0
    if n == 1:
        return 2
    for i in sieve:
        if i > 1:
            for j in range(2 * i, len(sieve), i):
                sieve[j] = 0
    sieve_1 = [i for i in sieve if i != 0]
    return sieve_1[n - 1]


# Второй — без использования «Решета Эратосфена».


def prime_method(n):
    prime = [2]
    num = 1
    i = 1
    if n == 1:
        return 2
    while i != n:
        num += 2
        for j in prime:
            if num % j == 0:
                break
        else:
            i += 1
            prime.append(num)
    return num


print(prime_method(32_768), prime_method(20))
print(sieve_method(32_768), sieve_method(20))


# Тестирование скорости и сложности "решето Эратосфена"
"""
print(timeit.timeit('sieve_method(20)', number=1000, globals=globals()))       # 0.3462481000024127
print(timeit.timeit('sieve_method(40)', number=1000, globals=globals()))       # 0.62956110000232
print(timeit.timeit('sieve_method(80)', number=1000, globals=globals()))       # 1.2267232000012882
print(timeit.timeit('sieve_method(160)', number=1000, globals=globals()))      # 2.5108504000018
print(timeit.timeit('sieve_method(320)', number=1000, globals=globals()))      # 5.030628200001956
print(timeit.timeit('sieve_method(640)', number=1000, globals=globals()))      # 10.852853200001846
print(timeit.timeit('sieve_method(1_280)', number=1000, globals=globals()))    # 23.7921697999991
print(timeit.timeit('sieve_method(2_560)', number=1000, globals=globals()))    # 51.161687700001494
print(timeit.timeit('sieve_method(5_120)', number=1000, globals=globals()))    # 120.6709918000015
print(timeit.timeit('sieve_method(10_240)', number=1000, globals=globals()))   # 320.2273094999982
"""


cProfile.run('sieve_method(32_768)')

"""
    235375 function calls in 1.297 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.025    0.025    1.297    1.297 <string>:1(<module>)
        1    1.165    1.165    1.272    1.272 les_4_task_2.py:10(sieve_method)
        1    0.090    0.090    0.090    0.090 les_4_task_2.py:19(<listcomp>)
        1    0.000    0.000    1.297    1.297 {built-in method builtins.exec}
   235370    0.017    0.000    0.017    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""


# Тестирование скорости и сложности классический метод (prime_method)

"""
print(timeit.timeit('prime_method(20)', number=1000, globals=globals()))       # 0.019057400000747293
print(timeit.timeit('prime_method(40)', number=1000, globals=globals()))       # 0.04940809999970952
print(timeit.timeit('prime_method(80)', number=1000, globals=globals()))       # 0.1759703999996418
print(timeit.timeit('prime_method(160)', number=1000, globals=globals()))      # 1.2391129000025103
print(timeit.timeit('prime_method(320)', number=1000, globals=globals()))      # 2.5069302000010794
print(timeit.timeit('prime_method(640)', number=1000, globals=globals()))      # 9.83758989999842
print(timeit.timeit('prime_method(1_280)', number=1000, globals=globals()))    # 34.08751680000205
print(timeit.timeit('prime_method(2_560)', number=1000, globals=globals()))    # 148.54443560000072
print(timeit.timeit('prime_method(5_120)', number=1000, globals=globals()))    # 590.117970700001
print(timeit.timeit('prime_method(10_240)', number=1000, globals=globals()))   # 2146.4734779999962
"""

cProfile.run('prime_method(32_768)')

"""
32771 function calls in 31.081 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   31.081   31.081 <string>:1(<module>)
        1   31.070   31.070   31.081   31.081 les_4_task_2.py:26(prime_method)
        1    0.000    0.000   31.081   31.081 {built-in method builtins.exec}
    32767    0.011    0.000    0.011    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

# Вывод: При N от 20 до 640 prime  выполняется быстрее.
# Но при N более 640 prime существенно начинает замедляться. Пример при N = 10_240 prime выполняется 2146 секунд,
# sieve выполняется 320 секунд. С увеличением N sieve выполняется стабильнее чем prime.