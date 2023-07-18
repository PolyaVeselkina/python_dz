# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
"""
n = int(input("Введите кол-во монет: "))
count0 = 0
count1 = 0
for i in range(n):
    temp = int(input("Введите  0 если решка, 1 если герб: "))
    if temp == 0:
        count0 += 1
    else:
        count1 += 1
if count0 < count1:
    print(count0)
else:
    print(count1)
"""      


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""
s = int(input("Введите сумму: "))
p = int(input("Введите произведение: "))
x = 0
y = 0

import math

discr = (-s) **2 - 4 * p
if discr > 0:
    x1 = (s + math.sqrt(discr))/ 2 
    x2 = (s - math.sqrt(discr))/ 2
    y1 = s - x1
    y2 = s - x2
    print(f' {x1}, {y1}')
elif discr == 0:
    x = s / 2 
    y = s - x
    print(f'{x}, {y}')
else:
    print('Таких целых чисел нет')
"""


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
"""
n = int(input("Введите число: "))
k = 0
x = 0
while 2 ** k < n:
    x = 2 ** k
    k += 1
    print(x, end=' ')
"""