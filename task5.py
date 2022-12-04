# 5'. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

from os import system
system("cls")
print("Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.")
def fib_list(a):
    if a in [1, 2]:
        return 1
    elif a == 0:
        return 0
    else:
        return (fib_list(a-1) + fib_list(a-2))

def neg_fib(a):
    return ((-1)**(a+1)+fib_list(a))

def fib(a):
    list1 = [neg_fib(i) for i in range(a+1)][::-1]
    list2 = [fib_list(i) for i in range(1, a+1)]
    return list1 + list2

a = int(input("Введите число: "))
print(fib(a))