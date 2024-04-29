
# def is_lucky_ticket(n):
#     # Проверяем, что номер билета состоит из 6 цифр
#     if len(str(n)) != 6:
#         return "no"
    
#     # Получаем отдельно первые три цифры и последние три цифры
#     first_half = [int(x) for x in str(n)[:3]]
#     second_half = [int(x) for x in str(n)[3:]]
    
#     # Сравниваем суммы первой и второй половин билета
#     if sum(first_half) == sum(second_half):
#         return "yes"
#     else:
#         return "no"

# # Пример использования
# ticket_number = 385916
# print(is_lucky_ticket(ticket_number))






# задача питон семинар 1. задача4. автотест про шоколадки.
# def can_break_chocolate(a, b, s): 
#     # Проверяем, что количество долек s не превышает общее количество долек в шоколадке
#     if s <= a * b:
#         # Проверяем, возможно ли разломить шоколадку так, чтобы отломленное количество долек было s
#         if s % a == 0 or s % b == 0:
#             return "yes"
#         else:
#             return "no"
#     else:
#         return "no"

# # Пример использования функции с заданными параметрами
# print(can_break_chocolate(3, 2, 6))  # Выведет "yes"
# print(can_break_chocolate(2, 4, 9))   # Выведет "no"





# Задача питон семинар 2. задача 1. вывести минимально колличество монеток которые нужно будет перевернуть, чтобы все они лежали одиннаковыми сторонами вверх
# def min_flips(coins):
#     heads_count = sum(coins)
#     tails_count = len(coins) - heads_count
#     return min(heads_count, tails_count)

# # Пример использования:
# coins = [0, 1, 0, 1, 1, 0, 0,]
# print("Минимальное количество монеток, которые нужно перевернуть:", min_flips(coins))






# Задача питон семинар 2. задача 2. все числа через запятую, которые будут соответствовать указанной сумме и произведению одновременно.
# def find_numbers(S, P):
#     possible_pairs = []
#     for x in range(1, S+1):
#         if P % x == 0:
#             y = P // x
#             if x + y == S:
#                 possible_pairs.append((x, y))
#     return possible_pairs

# S = int(input("Введите сумму чисел S: "))
# P = int(input("Введите произведение чисел P: "))

# pairs = find_numbers(S, P)

# print("Возможные пары чисел X и Y:")
# for pair in pairs:
#     if pair[0] <= pair[1]:
#         print(pair[0], pair[1])





#  Задача питон семинар 2. задача 3. Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.
# def powers_of_two(N):
#     powers = []
#     power = 1
#     while power <= N:
#         powers.append(power)
#         power *= 2
#     return powers

# N = int(input("Введите число N: "))

# print("Целые степени двойки не превосходящие", N, ":")
# for i in powers_of_two(N):
#     print(i)





# питан семинар 2. доп задача по нахождению всех делителей числа 
# def find_divisors(number):
#     divisors = []
#     for i in range(1, number + 1):
#         if number % i == 0:
#             divisors.append(i)
#     return divisors

# def main():
#     numbers = [12, 24, 36, 7845298]  # Пример чисел, для которых нужно найти делители
#     for number in numbers:
#         divisors = find_divisors(number)
#         print(f"Положительные делители числа {number}: {divisors}")

# if __name__ == "__main__":
#     main()







# Семинар 3. задача 17
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# def count_unique_digits(count):
#     # Преобразуем число в строку, чтобы можно было обращаться к отдельным цифрам
#     num_str = str(count)
    
#     # Создаем словарь для подсчета количества встреченных цифр
#     digit_count = {}
    
#     # Перебираем каждую цифру в числе
#     for digit in num_str:
#         # Если цифра уже встречалась, увеличиваем счетчик на 1
#         if digit in digit_count:
#             digit_count[digit] += 1
#         # Если цифра встречается впервые, добавляем ее в словарь
#         else:
#             digit_count[digit] = 1
    
#     # Возвращаем количество различных цифр в числе
#     return len(digit_count)

# # Запрашиваем число у пользователя
# count = int(input("Введите любое число: "))

# # Подсчитываем количество различных цифр в числе
# result = count_unique_digits(count)

# # Выводим результат
# print("Количество различных цифр в числе:", result)







# задача 19
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.


# def cyclic_shift(sequence, k):
#     # Проверяем, что k - положительное число
#     if k <= 0:
#         print("K должно быть положительным числом.")
#         return
    
#     # Определяем длину последовательности
#     n = len(sequence)
    
#     # Выполняем сдвиг на k элементов вправо
#     shifted_sequence = sequence[-k % n:] + sequence[:-k % n]
    
#     return shifted_sequence

# # Пример использования функции
# sequence = [1, 2, 3, 4, 5]
# k = 2
# shifted_sequence = cyclic_shift(sequence, k)
# print("Исходная последовательность:", sequence)
# print("После циклического сдвига на", k, "элементов вправо:", shifted_sequence)




# # задача 21
# Напишите программу для печати всех уникальных
# значений в словаре.

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит
# def print_unique_values(dictionary):
#     unique_values = set()  # Создаем множество для хранения уникальных значений

#     # Перебираем значения в словаре и добавляем их в множество
#     for value in dictionary.values():
#         unique_values.add(value)

#     # Печатаем уникальные значения
#     print("Уникальные значения в словаре:")
#     for unique_value in unique_values:
#         print(unique_value)

# # Пример использования функции
# my_dict =  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# print_unique_values(my_dict)










# семинар 4. задача 1

# def count_characters(input_string):
#     # Создаем словарь для отслеживания количества повторов каждого символа
#     char_count = {}
    
#     # Проходим по каждому символу в строке
#     for char in input_string:
#         # Если символ уже встречался, увеличиваем счетчик
#         if char in char_count:
#             char_count[char] += 1
#         # Иначе добавляем символ в словарь и устанавливаем счетчик в 1
#         else:
#             char_count[char] = 1
    
#     # Формируем строку с добавленными постфиксами _n
#     result = ""
#     for char, count in char_count.items():
#         result += char + '_' + str(count) + ' '
    
#     return result

# # Ввод строки с клавиатуры
# input_string = input("Введите строку: ")

# # Подсчет и вывод результатов
# result_string = count_characters(input_string)
# print("Результат:", result_string)


# def count_characters(input_string):
    
#     # превращаем список во множество, чтобы удалить повторяющиеся символы
#     unique_chars = set(input_string)
    
#     result = ""
#     for char in unique_chars:
#         # Используем метод count() для подсчета повторений символа
#         count = input_string.count(char)
#         result += char + '_' + str(count) + '  '
    
#     return result

# # Ввод строки с клавиатуры
# input_string = input("Введите строку: ")

# # Подсчет и вывод результатов
# print("Результат:", count_characters(input_string))





# задача 2 
# def count_unique_words(text):
#     text = text.replace('.', ' ')
#     # Разделяем текст на слова с помощью метода split()
#     words = text.split()
    
#     # Создаем множество для хранения уникальных слов
#     unique_words = set(words)

#     unique_words = list(unique_words)
    
    
#     # Возвращаем количество уникальных слов
#     return len(unique_words)

# # Ввод текста с клавиатуры
# text = input("введите текст: ")

# # Подсчет и вывод количества уникальных слов

# print("Количество различных слов в тексте:", count_unique_words(text))

# def count_unique_words(text):
#     # Приводим текст к нижнему регистру
#     text = text.lower()
#     # Разбиваем текст на слова, используя пробелы в качестве разделителей
#     words = text.split()
#     # Создаем множество для хранения уникальных слов
#     unique_words = set(words)
#     # Возвращаем количество уникальных слов
#     return len(unique_words)

# # Текст
# text = """She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells"""

# # Вызываем функцию для подсчета уникальных слов
# result = count_unique_words(text)
# # Выводим результат
# # print("Количество различных слов в тексте:", result)


# print(len(set(input("Введите текст: ").lower().split())))








# семинар объяснение
# import random


# NUM_CLASSES = 10


# def show_avg_value(sp):
#     avg = sum(sp) / len(sp)
#     print(avg)

# def calc_avg_value(sp: list) -> float:
#     '''
#     Эта функция вычисляет среднее арифметическое списка
#     '''
#     # надо проверить список или нет, и если нет то будем ругаться - выдавать ошибку
#     if not isinstance(sp, list):
#         raise TypeError("На входе должен быть список")
#         # print("На входе должен быть список")
#         # return 
#     avg = sum(sp) / len(sp)
#     return avg


# sp = [1,3,5,7,10]
# # show_avg_value(sp)
# # print(calc_avg_value(sp))
# t = tuple(sp)
# try:
#     print(calc_avg_value(t))
# except TypeError as te:
#     print(te)
# # print(calc_avg_value.__doc__)








# задача 3
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. 
# Ваня:                           Петя:
# n = int(input())                 n = int(input())
# max_number = 1000                max_number = -1
# while n != 0:                    while n < 0:
#  n = int(input())                 n = int(input())
#  if max_number > n:               if max_number < n:
#  max_number = n                    n = max_number
# print(max_number)                  print(n) 


# # Код Вани
# max_number = -1  # Инициализируем переменную для хранения максимального числа
# n = int(input())  # Считываем первое число последовательности

# while n != 0:  # Пока не встретится 0
#     if n > max_number:  # Если текущее число больше максимального
#         max_number = n  # Обновляем максимальное число
#     n = int(input())  # Считываем следующее число последовательности

# print(max_number)  # Выводим наибольшее число

# # Код Пети
# max_number = -1  # Инициализируем переменную для хранения максимального числа
# n = int(input())  # Считываем первое число последовательности

# while n != 0:  # Пока не встретится 0
#     if n > max_number:  # Если текущее число больше максимального
#         max_number = n  # Обновляем максимальное число
#     n = int(input())  # Считываем следующее число последовательности

# print(max_number)  # Выводим наибольшее число






# задача4 
# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени, где все коэффициенты случайные от -10 до 10.
# например, k=2 -> -x^2 + 3*x - 8 = 0
# тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3 - 2*x = 0
# тут коэффициенты 3,0,-2,0


# import random

# def generate_polynomial(k):
#     coefficients = [random.randint(-10, 10) for _ in range(k+1)]  # Generating random coefficients
#     coefficients_str = [f"{coeff} * x^{index}" if index > 1 else f"{coeff} * x" if index == 1 else f"{coeff}" for index, coeff in enumerate(coefficients[::-1])]
#     polynomial = " + ".join(coefficients_str[::-1])  # Creating the polynomial string
#     return polynomial

# def main():
#     k = int(input("Введите натуральное число k: "))
#     if k < 1:
#         print("Ошибка: k должно быть натуральным числом.")
#         return
#     polynomial = generate_polynomial(k)
#     print(f"Сгенерированный многочлен для k = {k}: {polynomial} = 0")

# if __name__ == "__main__":
#     main()






# домашка семинар 4

# def common_elements(n, m, set1, set2):
#     # Преобразуем входные строки в множества целых чисел
#     set1 = set(map(int, set1.split()))
#     set2 = set(map(int, set2.split()))

#     # Находим пересечение множеств и сортируем его
#     intersection = sorted(set1.intersection(set2))

#     return intersection

# # Пример ввода
# n, m = map(int, input().split())
# set1 = input()
# set2 = input()

# # Вывод результата
# result = common_elements(n, m, set1, set2)
# print(*result)






# задача 2 про чернику

# def max_berry_count(arr):
#     n = len(arr)
#     max_count = 0
    
#     for i in range(n):
#         # Собираем ягоды с k-го куста
#         for k in range(i, i + 3):
#             # Обрабатываем случай, когда индекс превышает длину списка
#             idx = k % n
            
#             # Считаем количество собранных ягод
#             count = arr[idx] + arr[(idx + 1) % n] + arr[(idx + 2) % n]
            
#             # Обновляем максимальное количество ягод
#             if count > max_count:
#                 max_count = count
    
#     return max_count

# # Пример использования:
# arr = [5, 8, 6, 4, 9, 2, 7, 3]
# print(max_berry_count(arr))






# семинар рекурсия 

# задание 1

# def fib(n):

#   if (n == 0): 
#     return 0

#   if (n == 1): 
#     return 1

#   return fib(n - 1) + fib(n - 2)

# n = int(input())

# print(fib(n))






# задача 2

# def replace_grades_recursive(grades, max_grade=None, min_grade=None, index=0):
#    if max_grade is None:
#        max_grade = max(grades)
#    if min_grade is None:
#        min_grade = min(grades)
    # 
    # if index < len(grades):
        # if grades[index] == max_grade:
            # grades[index] = min_grade
        # elif grades[index] == min_grade:
            # grades[index] = max_grade
        # replace_grades_recursive(grades, max_grade, min_grade, index+1)
    # return grades

# Пример использования
# vasilys_grades = [1, 3, 3, 3, 4]
# print("Оценки до замены:", vasilys_grades)
# replaced_grades = replace_grades_recursive(vasilys_grades)
# print("Оценки после замены:", replaced_grades)






# задача 3
# def is_prime(number, divisor=None):
#     if divisor is None:
#         divisor = number - 1
    
#     if number <= 1:
#         return False
#     elif divisor == 1:
#         return True
#     elif number % divisor == 0:
#         return False
#     else:
#         return is_prime(number, divisor - 1)

# # Пример использования:
# number = int(input("Введите число: "))
# if is_prime(number):
#     print(number, "является простым числом.")
# else:
#     print(number, "не является простым числом.")





# задачае 4
    
# def reverse_sequence(n, sequence):
#     if n == 0:
#         return 
#     element = sequence.pop(0)
#     reverse_sequence(n - 1, sequence)
#     print(element)





# # Заданные параметры
# N = 2
# values = [3, 4]

# # Пример использования
# print("Последовательность в обратном порядке:")
# reverse_sequence(N, values.copy())


# def reverse_sequence():
#     num = int(input("Введите количество элементов в последовательности: "))
#     if num <= 0:
#         print("Некорректное число элементов.")
#         return
#     if num == 1:
#         print("Введите элемент последовательности: ")
#         print(input())
#     else:
#         print("Введите элемент последовательности: ")
#         print(input())
#         reverse_sequence()

# print("Введите последовательность чисел:")
# reverse_sequence()






# семинар 6. повторение списков

#Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива


# from random import randint

# l1 = int(input("Введите длину первого списка: "))
# l2 = int(input("Введите длину второго списка: "))
# list_1 = [randint(1,20) for _ in range(l1)]
# print(list_1)
# list_2 = [randint(1,20) for _ in range(l2)]
# print(list_2)
# print(*[i for i in list_1 if i not in set(list_2)])





# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:         Ввод:
# 5             5
# 1 2 3 4 5     1 5 1 5 1
# Вывод:        Вывод:
# 0             2

# решение в группах
# def find_local_max(i):
#     return list_3[i-1] < list_3[i] and list_3[(i+1) % len(list_3)] < list_3[i]

# list_3 = [15, 6, 3, 12, 9, 0, 2, 20]

# print(len([list_3[i] for i in range(len(list_3)) if find_local_max(i)]))


# решение джипити
# n = int(input("Введите количество элементов в массиве: "))
# arr = [int(input("Введите элемент массива: ")) for _ in range(n)]
# count = 0
# for i in range(1, n - 1):
#     if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
#         count += 1
    
# print("Количество элементов, у которых оба соседних элемента меньше данного:", count)





# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:       Вывод:
# 1 2 3 2 3   2


# numbers = []
# while True:
#     num = input()
#     if num == 'done':
#         break
#     numbers.append(int(num))

# print(sum(numbers.count(num) // 2 for num in set(numbers)))




# задача
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:    Вывод:
# 300      220 284

# def sum_of_divisors(n):
#     return sum(i for i in range(1, n) if n % i == 0)

# k = int(input())
# pairs = [(n, m) for n in range(1, k+1) if (m := sum_of_divisors(n)) > n and sum_of_divisors(m) == n <= k]
# for pair in pairs:
#     print(*pair)







# семинар 6 
# from random import randint

# # sp = []
# # for i in range(10):
# #     sp.append(randint(1,20))
# # print(sp)
# # print( sp := [randint(1,20) for _ in range(10)] )

# sp = [1,23,3,4,5,6,8,9]
# # print( [item for item in sp] )
# print( [item **2 for item in sp if item % 2] ) # количество элементов уменьшилось
# print( [item **2 if item % 2 else 0 for item in sp ] )  # если надо одинаковое кол-во элементов
# # возвести в квадрат каждый нечетный элемент иначе вернуть ноль для каждого элемента в списке sp
# print( {i : sp[i] for i in range(len(sp))} ) 
# print( {sp[i] for i in range(len(sp))} )






# семинар 7
# функции высшего порядка

# действия на семинаре от препода

# def hello(name):
#     return f"Hello, {name}"

# def bye(name):
#     return f"{name}, bye-bye"

# def create_phrase(func):
#     name = input("Введите свое имя ")
#     return func(name)

# # print(create_phrase(hello))
# # print(create_phrase(bye))

# def create_dialog(funcs):
#     res = ""
#     name = input("Введите свое имя ")
#     for func in funcs:
#         res += f"{func(name)}\n"
#     return res 

# funcs = (hello, bye)
# print(create_dialog(funcs))

# def calc_power(degree):
#     def power(base):
#         return base ** degree
#     return power

# print(calc_power(4)(2)  )
# square = calc_power(2)
# cube = calc_power(3)

# print(square(9))
# print(cube(4))

# square_even = lambda x: x ** 2 if x % 2 else 0
# print(square_even(9))
# print(square_even(8))


# калькулятор
# calc = {
#     '+': lambda x,y: x + y,
#     '-': lambda x,y: x - y,
#     '*': lambda x,y: x * y,
#     '/': lambda x,y: x / y
# }
# s = input("Введите математическое выражение через пробелы ")
# first, op, second = s.split()
# print(f"Ответ равен {calc[op] (int(first), int(second))  }")

# sp = list(range(11))
# print( *map(lambda x: x ** 2 ,sp) )
# print( *map(lambda x: x ** 2  if x % 2 else 0,sp) )
# print(*filter(lambda x: x % 2 ,sp))
# sp2 =['Вася', "ваня"]
# for item in zip(sp2, sp):
#     print(item)



# задача 1

#У вас есть код, который вы не можете менять:
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако нужно получить его как есть.
# Напишите такой лямбда-выражение transformation, чтобы transformed_values получился копией values.


# values = [1, 23, 42, 'asdfg']
# transformation = lambda x: x
# transformed_values = list(map(transformation, values))

# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')




# задача 2

# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# def find_farthest_orbit(orbits):
#     list_of_orbit_squares = list(map(lambda i: (i[0] != i[1]) * i[0] * i[1], orbits))
#     return orbits[list_of_orbit_squares.index(max(list_of_orbit_squares))], f'\nНомер самой удалённой планеты: {list_of_orbit_squares.index(max(list_of_orbit_squares))+1}'
    

# orbits = [(1, 3), (7, 2), (6, 6), (4, 3), (2.5, 10)]
# print("Дуги орбиты самой дальней планеты:", *find_farthest_orbit(orbits))




# задача 3

# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# def same_by_map(characteristic, objects):
#     return len(set(map(characteristic, objects))) in (0, 1)

# def same_by_all(characteristic, objects):
#     if not objects:
#         return True
#     first_characteristic = characteristic(objects[0])
#     return all(characteristic(obj) == first_characteristic for obj in objects)
    
# def same_by_filter(characteristic, objects):    
#     different_objects = list(filter(characteristic, objects))
#     return len(different_objects) == len(objects) or not len(different_objects)
# values = [0, 1, 10, 6] #

# if same_by_filter(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')





# дз
# Урок 6. Повторение списков
#  Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.
# пример:
# ввод:
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10
# вывод:
# 1
# 2
# 3
# 6
# 7
# 9
# 10
# 11
# 13
# 14
# 16
# 19

# def find_indices_in_range(input_list, min_number, max_number):
#     indices = []
#     for i, num in enumerate(input_list):
#         if min_number <= num <= max_number:
#             indices.append(i)
#     return indices

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10

# result_indices = find_indices_in_range(list_1, min_number, max_number)
# for index in result_indices:
#     print(index)




# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент a1 , разность d и количество элементов n будет задано автоматически. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# def arithmetic_progression(a1, d, n):
#     progression = []
#     for i in range(n):
#         progression.append(a1 + i * d)
#     return progression

# # Пример использования функции
# a1 = 2
# d = 3
# n = 4
# result = arithmetic_progression(a1, d, n)
# for element in result:
#     print(element)







# дз Урок 7. Функции высшего порядка
# Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. По умолчанию номер столбца и строки = 9.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы.
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# Между элементами должен быть 1 пробел, в конце строки пробел не нужен

# def print_operation_table(operation, num_rows=9, num_columns=9):
#     if num_rows < 2 or num_columns < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#         return
    
#     for i in range(1, num_rows + 1):
#         row = ""
#         for j in range(1, num_columns + 1):
#             row += str(operation(i, j)) + " "
#         print(row.rstrip())

# Пример использования
# print_operation_table(lambda x, y: x * y, 3, 3)






# дз задача 2

# Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. 
# В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!

# def count_vowels(word):
#     vowels = 'аеёиоуыэюя'  # список русских гласных букв
#     return sum(1 for letter in word if letter.lower() in vowels)

# def check_rhythm(stroka):
#     phrases = stroka.split()
#     if len(phrases) <= 1:
#         print("Количество фраз должно быть больше одной!")
#         return

#     syllable_counts = [count_vowels(phrase.replace('-', '')) for phrase in phrases]
#     if all(count == syllable_counts[0] for count in syllable_counts):
#         print("Парам пам-пам")
#     else:
#         print("Пам парам")

# # Пример использования:
# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# check_rhythm(stroka)






# Семинар 8. работа с файлами

# задача 
# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной



#                  ПОДСКАЗКА
# Функция для импорта данных из файла
# import random

# def import_contacts(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             return [dict(zip(['last_name', 'first_name', 'middle_name', 'phone_number'], line.strip().split(','))) for line in file]
#     except FileNotFoundError:
#         print("Файл не найден.")
#         return []

# def export_contacts(contacts, file_name):
#     try:
#         with open(file_name, 'w') as file:
#             for contact in contacts:
#                 file.write(','.join(contact.values()) + '\n')
#         print("Контакты успешно экспортированы.")
#     except IOError:
#         print("Ошибка при записи файла.")

# def add_contact(contacts):
#     contacts.append({
#         'last_name': input("Введите фамилию: "),
#         'first_name': input("Введите имя: "),
#         'middle_name': input("Введите отчество: "),
#         'phone_number': input("Введите номер телефона: ")
#     })
#     print("Контакт успешно добавлен.")








# # 1. До цикла загрузить данные из файла в коллекцию
# # 2. дальше while True пока не будет слова Stop
# # 3. внутри цикла постоянно спрашиваем команду и ее обрабатываем через if
# # 4. По команде save а может и плюсом после окончания цикла сохраняем коллекцию в файл.

# phonebook = {
#     "дядя Ваня" : {'phones': [1321321,1321312], 
#                    'birthday': '01.01.1960',
#                    'email': 'vanya@mail.ru'
#                    },
#     "дядя Вася": {'phones' : [1211111]} 
#              }

# print(phonebook['дядя Ваня'])
# print(phonebook['дядя Ваня'] ['phones'])
# print(phonebook['дядя Ваня'] ['phones'] [-1])



# Семинар 8. работа с файлами

# задача 
# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной


# Функция для импорта данных из файла
# import random

# def import_contacts(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             return [dict(zip(['last_name', 'first_name', 'middle_name', 'phone_number'], line.strip().split(','))) for line in file]
#     except FileNotFoundError:
#         print("Файл не найден.")
#         return []

# def export_contacts(contacts, file_name):
#     try:
#         with open(file_name, 'w') as file:
#             for contact in contacts:
#                 file.write(','.join(contact.values()) + '\n')
#         print("Контакты успешно экспортированы.")
#     except IOError:
#         print("Ошибка при записи файла.")

# def add_contact(contacts):
#     contacts.append({
#         'last_name': input("Введите фамилию: "),
#         'first_name': input("Введите имя: "),
#         'middle_name': input("Введите отчество: "),
#         'phone_number': input("Введите номер телефона: ")
#     })
#     print("Контакт успешно добавлен.")




# def main():
#     file_name = "contacts.txt"
#     # Список предварительно заполненных контактов
#     preloaded_contacts = [
#         {'last_name': 'Иванов', 'first_name': 'Иван', 'middle_name': 'Иванович', 'phone_number': '123456789'},
#         {'last_name': 'Петров', 'first_name': 'Петр', 'middle_name': 'Петрович', 'phone_number': '987654321'}
#     ]
#     contacts = preloaded_contacts + import_contacts(file_name)

#     while True:
#         print("\nМеню:")
#         print("1. Добавить контакт")
#         print("2. Экспортировать контакты в файл")
#         print("3. Выйти")

#         choice = input("Выберите действие: ")

#         if choice == '1':
#             add_contact(contacts)
#         elif choice == '2':
#             export_contacts(contacts, file_name)
#         elif choice == '3':
#             break
#         else:
#             print("Неверный выбор.")

# if __name__ == "__main__":
#     main()


# # 1. До цикла загрузить данные из файла в коллекцию
# # 2. дальше while True пока не будет слова Stop
# # 3. внутри цикла постоянно спрашиваем команду и ее обрабатываем через if
# # 4. По команде save а может и плюсом после окончания цикла сохраняем коллекцию в файл.

# phonebook = {
#     "дядя Ваня" : {'phones': [1321321,1321312], 
#                    'birthday': '01.01.1960',
#                    'email': 'vanya@mail.ru'
#                    },
#     "дядя Вася": {'phones' : [1211111]} 
#              }

# print(phonebook['дядя Ваня'])
# print(phonebook['дядя Ваня'] ['phones'])
# print(phonebook['дядя Ваня'] ['phones'] [-1])

# посмотрим всю информацию из таблицы users 
# cur.execute("SELECT * FROM users;")
# print(cur.fetchall())


# choice = choicebox("Выберите запрос", "Главная форма", 
#                    ['Все записи', "Только Ваня"])
# if choice == "Все записи":
#     msg = str(select_all())
#     msgbox(msg, "Результат запроса")
# if choice == "Только Ваня":
#     msg = str(select_ivan())
#     msgbox(msg, "Результат запроса")


# сохранить изменения
# conn.commit()
# conn.close()

# для создания базы данных. создаем пустую папку, в ней файл .py
# пишем слудующий код для создания файла lesson_7.db

# import sqlite3 as sl
# from easygui import *

# def select_all():
#     cur.execute("SELECT * FROM users;")
#     return cur.fetchall()


# def select_ivan():
#     cur.execute("SELECT * FROM users WHERE name = 'Ваня';")
#     return cur.fetchall()


# # создание подключения к БД
# conn = sl.connect("lesson_7.db")

# выполним запрос добавления информации в эту таблицу
# cur.execute("INSERT INTO users VALUES (1,'Ваня','Петров');")
# cur.execute("INSERT INTO users VALUES (2,'Сергей','Сергеев');")


# import crud as cr
# import logger as lg



import sqlite3 as sl

def menu(conn):
    while True:
        print('Меню')
        user_choice = input('1 - Импортировать данные\n2 - Найти контакт\n3 - Добавить контакт\n\
4 - Изменить контакт\n5 - Удалить контакт\n6 - Список контактов\n0 - Выход\n')
        print()
        if user_choice == '1':
            file_to_add = input('Введите название файла: ')
            import_data(file_to_add, conn)
        elif user_choice == '2':
            find(conn)
        elif user_choice == '3':
            add(conn)
        elif user_choice == '4':
            change(conn)
        elif user_choice == '5':
            delete(conn)
        elif user_choice == '6':
            show(conn)
        elif user_choice == '0':
            print('Выход')
            break
        else:
            print('Неправильно выбрана команда')
            print()
            continue
        conn.commit()


def import_data(file_to_add, conn):
    try:
        with open(file_to_add, 'r', encoding='utf-8') as new_contacts:

            contacts_to_add = new_contacts.readlines()
            for line in contacts_to_add:
                c = conn.cursor()
                c.execute(f'INSERT INTO phone(фамилия, имя, номер) VALUES(?, ?, ?);', line.split())
    except FileNotFoundError:
        print(f'{file_to_add} не найден')

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Фамилия', 'Имя', 'Номер телефона']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list




def search_parameters():
    print('Поиск')
    search_field = input('1 - фамилия\n2 - имя\n3 - телефон\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите фамилию: ')
        print()
    elif search_field == '2':
        search_value = input('Введите имя: ')
        print()
    elif search_field == '3':
        search_value = int(input('Введите номер: '))
        print()
    return search_field, search_value


def find(conn):
    search_field, search_value = search_parameters()
    search_fields_dict = {'1': 'фамилия', '2': 'имя', '3': 'номер'}
    found_contacts = []
    c = conn.cursor()
    c.execute(f'SELECT фамилия, имя, номер FROM phone WHERE {search_fields_dict[search_field]} = "{search_value}";')
    for line in c.fetchall():
        found_contacts.append({key: value for key, value in zip(['Фамилия', 'Имя', 'Номер'], line)})
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()


def get_new():
    last_name = input('Фамилия: ')
    first_name = input('Имя: ')
    phone_number = int(input('Телефон: '))
    return last_name, first_name, phone_number


def add(conn):
    c = conn.cursor()
    c.execute(f'INSERT INTO phone(фамилия, имя, номер) VALUES(?, ?, ?);', get_new())
    conn.commit()


def show(conn):
    print(f'Фамилия{" " * (20 - len("Фамилия"))}Имя{" " * (20 - len("Имя"))}Номер')
    c = conn.cursor()
    c.execute('SELECT * FROM phone ORDER BY фамилия')
    for line in c.fetchall():
        print(f'{line[0]:20}{line[1]:20}{line[2]:12}')
    print()


def search_to_modify(conn):
    search_field, search_value = search_parameters()
    search_fields_dict = {'1': 'фамилия', '2': 'имя', '3': 'номер'}
    search_result = []
    c = conn.execute(f'SELECT * FROM phone WHERE {search_fields_dict[search_field]} = "{search_value}";')
    for line in c.fetchall():
        search_result.append({key: value for key, value in zip(['Фамилия', 'Имя', 'Номер'], line)})
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Какой из контактов?')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите контакт, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден')
    print()


def change(conn):
    number_to_change = search_to_modify(conn)
    number_to_change_old = number_to_change.copy()
    print('Что изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n')
    if field == '1':
        number_to_change['Фамилия'] = input('Новая фамилия: ')
    elif field == '2':
        number_to_change['Имя'] = input('Новое имя: ')
    elif field == '3':
        number_to_change['Номер'] = input('Новый номер телефона: ')
    c = conn.cursor()
    c.execute(f'''UPDATE phone 
              SET имя = '{number_to_change['Имя']}', фамилия = '{number_to_change['Фамилия']}', номер = '{number_to_change['Номер']}'
              WHERE имя = '{number_to_change_old['Имя']}' 
                    AND фамилия = '{number_to_change_old['Фамилия']}' 
                    AND номер = '{number_to_change_old['Номер']}'
              
                    ''')



def delete(conn):
    number_to_change = search_to_modify(conn)
    c = conn.cursor()
    c.execute(f'''DELETE FROM phone WHERE
                        имя = '{number_to_change['Имя']}' AND фамилия = '{number_to_change['Фамилия']}' AND номер = '{number_to_change['Номер']}'
                ''')


def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()



if __name__ == '__main__':

    conn = sl.connect(r'C:\Users\kutlu\OneDrive\Рабочий стол\python_att\proba.db', timeout=10)
    menu(conn)