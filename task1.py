#1'. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#*Пример:*
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from os import system
import random
system("cls")
b = int(input("Введите длину списка: "))
a = int(input("Введите максимальную рзмерность числа в списке: "))
mass = []
for i in range(b):
    mass.append(random.randint(1, a))
print(f"Список: {mass}")
new_list = list(map(int, mass))
summa = 0
for i in range(1, len(new_list), 2):
        summa += new_list[i]
print(f"Сумма элементов с нечетными индексами равна {summa}")