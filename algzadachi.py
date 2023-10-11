# 1) Проверка числа
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# numbercheck = int(input("Введите число от 0 до 10000: "))
#
# if 0 <= numbercheck <= 10000:
#     result = is_prime(numbercheck)
#     print(f"Число {numbercheck} является ли простым ?: {result}")
# else:
#     print("Число вне допустимого диапазона.")

# 2) Сортировка масива
# def sortirovka(arr):
#     dlinamasiva = len(arr)
#     for i in range(dlinamasiva):
#         for f in range(0, dlinamasiva - i - 1):
#             if arr[f] > arr[f + 1]:
#                 arr[f], arr[f + 1] = arr[f + 1], arr[f]
#
# numbers = input("Введите числа, разделенные пробелом: ").split()
# sortirovka(numbers)
# print("Отсортированный массив ↑:", numbers)

# 3 ) Поиск наибольшего значения из массива
# def bigelementmassiv(masiv):
#     if not masiv:
#         return None
#     max_value = masiv[0]
#     for element in masiv:
#         if element > max_value:
#             max_value = element
#     return max_value
#
# numbers = input("Введите числа, разделенные пробелом: ").split()
# max_value = bigelementmassiv(numbers)
# print("Наибольший элемент: ", max_value)

# 4) Число Фибоначчи
# n = int(input("Укажите число: "))
# def fib(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
# result = fib(n)
# print(f"Число Фибоначчи под номером {n} равно {result}")

# 5) Хэш-Таблицы
# def tablhech(arr):
#     return max(set(arr), key=arr.count)
#
# input_array = input("Введите список слов через пробел: ").split()
# result = tablhech(input_array)
# print("Больше всего используется: ", result)