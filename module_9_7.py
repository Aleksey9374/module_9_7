'''Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом
и "Составное" в противном случае.'''

''' использование синтаксиса «@» для декорирования'''
# def is_prime(func):
#     def wrapper(*args):
#         result = func(*args)
#         for i in range(2, (result // 2) + 1):
#             if result % i == 0:
#                 prime = 'Составное' # Если при переборе встретится делитель удовлетворяющий условию записываем результат
#                 break # и прерываем цикл
#             else: prime = 'Простое'
#         print(prime)
#         return result
#     return wrapper
#
# @is_prime
# def sum_three(x, y, z):
#     return x + y + z
#
# result = sum_three(2, 3, 6)
# print(result)


def is_prime(sum_three):
    prime = 'Простое'
    for i in range(2, (sum_three // 2) + 1):
        if sum_three % i == 0:
            prime = 'Составное' # Если при переборе встретится делитель удовлетворяющий условию записываем результат
            break # и прерываем цикл
    print(prime)
    return sum_three

def sum_three(x, y, z):
    return x + y + z

result = is_prime(sum_three(2, 3, 6))
print(result)