#3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#*Пример:*
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from os import system
system("cls")
print("Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.")
import random
def separate(num:float):
    mass_num = str(num).split('.')
    return float('0.' + mass_num[1])

def definition_max_min(mass_num:list[float]):
    new_mass = [separate(i) for i in mass_num if int(i) != float(i)]
    return max(new_mass) - min(new_mass)

b = int(input("Введите длину списка: "))
mass = []
for i in range(b):
    mass.append((round(random.random(), 2)) + random.randint(1, 11))
print(f"Список: {mass}")

print(definition_max_min(mass))