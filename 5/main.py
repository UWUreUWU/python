# x = 7
# #if -если
# #else - иначе
# if x <= 10:
#     print("Икс не больше 10 или 15")
# else:
#     print("Икс больше 10")
# x = 10
# print(x == 10)
# print(x == 5)
# x = int(input("Ввеите число:"))
# if x < 0:
#     print("ОТрицательное")
# elif x > 0:
#     print("Положительное")
# else:
#     print("Равно нулю")
# year = int(input("Введи год:"))
#
# if year % 4 == 0 and (year % 400 == 0  or year % 100 !== 0):
#     print("Високосный")
# else:
#     print("Не високосный :(")
# number_1 = int(input("Введи первое число"))
# operation = input("Введи операцию(+, -, *, /):")
# number_2 = int(input("Введи второе число:"))
#
# lst = ["+", "-", "/", "*"]
# if operation in lst:
#     print(number_1 + number_2)
# elif opertion == "-":
#     print(number_1 - number_2)
# elif opertion == "/":
#     print(number_1 / number_2)
# if operation == "*":
#     print(number_1 * number_2)
# counter_plus = 0
# counter_minus = 0
# if number_1 > 0:
#     couner_plus += 1
# else:
#     couner_minus += 1
#
# if number_2 > 0:
#     counter_plus += 1
# else:
#     counter_minus += 1
# if number_3 > 0:
#     counter_plus += 1
# else:
#     counter_minus +=1
#
# print("Положительных:", counter_plus)
# print("Отрицательые:", counter_minus)
# number_1 = int(input("Введи первое число: "))
# number_2 = int(input("Введи второе число: "))
# number_3 = int(input("Введи второе число: "))
#
# lst = [number_1, number_2, number_3]
# mini = min(lst)
# maxi = max(lst)
#
# print("Минимальное: ", mini)
# print("Максимальное: ", maxi)
# ticket = int(input("Введи номер билета:"))
# if len(ticket) == 6:
#     first_half = ticket[:3]
#     second_half = ticket[-3:]
#
#     first_sum = int(first_half[0] + first_half[1] + first_half[2])
#     second_sum = int(second_half[0]) + int(second_half[1]) + int(second_half[2])
#
#     if first_sum == second_sum:
#         print("Твой билет счастливый!")
#     else:
#         print("Не повезло(")
# else:
#     print("Не то ты ввёл!")