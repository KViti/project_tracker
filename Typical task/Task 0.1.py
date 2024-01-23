import math, random

def reduce_fraction_Numerator(n, m): # Функция сокращающая дробь выводит числитель
    k = math.gcd(n, m)
    return (n // k)


def reduce_fraction_Denominator(n, m): # Функция сокращающая дробь выводит знаменатель
    k = math.gcd(n, m)
    return (m // k)

def count(Decimal):  # Функция для количества знаков после запятой
    n=1
    while Decimal / 10 ** n >= 1:
        n += 1
    return n

def NEW(Numerator, Denominator): # Функция для генерации новых числителя и знаменателя (числитель < знаменатель)
    while (Numerator >= Denominator):
        Numerator, Denominator = random.randint(2, 10), random.randint(2, 10)
    return (Numerator, Denominator)

def NULL(Decimal): # Функция для генерации десятичной части числа, на конце не ноль (1)
    while Decimal % 10 ==0:
        Decimal = random.randint(1, 100)
    return Decimal

def TRU(Numerator1, Denominator1, Decimal1, Numerator2, Denominator2, Decimal2, Numerator3, Denominator3, Decimal3):  # Функция для генерации нового набора значений(использует все вышеперечисленные функции)
    Numerator1, Denominator1, Decimal1 = random.randint(1, 100), random.randint(2, 100), NULL(Decimal1)  # Генерация набора значений
    Numerator2, Denominator2, Decimal2 = random.randint(1, 100), random.randint(2, 100), NULL(Decimal2)
    Numerator3, Denominator3, Decimal3 = random.randint(1, 100), random.randint(2, 100), NULL(Decimal3)

    Numerator1, Denominator1 = reduce_fraction_Numerator(Numerator1, Denominator1), reduce_fraction_Denominator(Numerator1, Denominator1) # Сокращение дроби
    Numerator2, Denominator2 = reduce_fraction_Numerator(Numerator2, Denominator2), reduce_fraction_Denominator(Numerator2, Denominator2)
    Numerator3, Denominator3 = reduce_fraction_Numerator(Numerator3, Denominator3), reduce_fraction_Denominator(Numerator3, Denominator3)
    Numerator1 %= Denominator1 # (числитель < знаменатель) остаток от деления
    Numerator2 %= Denominator2
    Numerator3 %= Denominator3

    if (Denominator1==1 or Denominator2==1 or Denominator3==1) or (Denominator1==Denominator2 or Denominator2==Denominator3 or Denominator3==Denominator1): # Знаменатель равен 1 или равны знаменатели между собой
        Numerator1, Denominator1, Decimal1, Numerator2, Denominator2, Decimal2, Numerator3, Denominator3, Decimal3=TRU(Numerator1, Denominator1, Decimal1, Numerator2, Denominator2, Decimal2, Numerator3, Denominator3, Decimal3) # Рекурсия вызываем саму функцию
    return Numerator1, Denominator1, Decimal1, Numerator2, Denominator2, Decimal2, Numerator3, Denominator3, Decimal3


Whole1, Whole2, Whole3 = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100) # Сокращение дроби


Numerator1, Denominator1, Decimal1 = random.randint(1, 10), random.randint(2, 25), random.randint(1, 9)# Сокращение дроби
Numerator2, Denominator2, Decimal2 = random.randint(1, 10), random.randint(2, 25), random.randint(1, 9)
Numerator3, Denominator3, Decimal3 = random.randint(1, 10), random.randint(2, 25), random.randint(1, 9)

Numerator1, Denominator1 = NEW(Numerator1, Denominator1)# Сокращение дроби
Numerator2, Denominator2 = NEW(Numerator2, Denominator2)
Numerator3, Denominator3 = NEW(Numerator3, Denominator3)

# (Числитель3/Знаменатель3+Числитель2/Знаменатель2)*Целое3
print('Пример 1:Числитель3/Знаменатель3+Числитель2/Знаменатель2)*Целое3')
K=(Numerator3 / Denominator3 + Numerator2 / Denominator2) * Whole3
while (round(K *10-int(K*10), 5)!=0):# Пока после запятой более 1 цифры
    Numerator1, Denominator1, Decimal1, Numerator2, Denominator2, Decimal2, Numerator3, Denominator3, Decimal3 = TRU(Numerator1, Denominator1, Decimal1, Numerator2, Denominator2, Decimal2, Numerator3, Denominator3, Decimal3) # создаём новый набор
    K = (Numerator3 / Denominator3 + Numerator2 / Denominator2) * Whole3  # значение выражения меняем на новое
print('Вид выражения: (', Numerator3, '/', Denominator3, '+', Numerator2, '/', Denominator2, ')*', Whole3, sep="") # Вид
print('Найди значение выражения $$\Big( \\frac', '{', Numerator3, '}{',  Denominator3, '} + ', '\\frac', '{', Numerator2, '}{', Denominator2, '}\Big) \cdot ', Whole3, '.$$', sep="")# LATEX
print('Ответ: ', round(K, 5), sep="", end='\n\n')# значение выражения

# Целое1*(Числитель3/Знаменатель3+Целое2+Числитель2/Знаменатель2)
print('Пример 2:Целое1+Числитель1/Знаменатель1+Целое2+Числитель2/Знаменатель2)*Целое3')
K=(Whole1+Numerator1 / Denominator1 + Whole2 + Numerator2 / Denominator2)*Whole3
while (round(K *10-int(K*10), 5)!=0):# Пока после запятой более 1 цифры
    Numerator1, Denominator1, Decimal1, Numerator2, Denominator2, Decimal2, Numerator3, Denominator3, Decimal3 = TRU(Numerator1, Denominator1, Decimal1, Numerator2, Denominator2, Decimal2, Numerator3, Denominator3, Decimal3) # создаём новый набор
    K=(Whole1+Numerator1 / Denominator1 + Whole1 + Numerator2 / Denominator2)*Whole3 # значение выражения меняем на новое
print('Вид выражения: (', Whole1, '+', Numerator1, '/', Denominator1, '+', Whole2, '+', Numerator2, '/', Denominator2, ')*', Whole3, sep="") # Вид
print('Найди значение выражения $$\Big( ', Whole1, ' \\frac{', Numerator1, '}{',  Denominator1, '} + ', Whole2, '\\frac', '{', Numerator2, '}{', Denominator2, '}\Big) \cdot ', Whole3, '.$$', sep="")# LATEX
print('Ответ: ', round(K, 5), sep="", end='\n\n')# значение выражения

# (Числитель1/Знаменатель1+Целое2+Числитель2/Знаменатель2)*Целое3
print('Пример 3:Числитель1/Знаменатель1+Целое2+Числитель2/Знаменатель2)*Целое3')
K=(Numerator1 / Denominator1 + Whole2 + Numerator2 / Denominator2) * Whole3
while (round(K *10-int(K*10), 5)!=0):
    Numerator1, Denominator1, Decimal1, Numerator2, Denominator2, Decimal2, Numerator3, Denominator3, Decimal3 = TRU(Numerator1, Denominator1, Decimal1, Numerator2, Denominator2, Decimal2, Numerator3, Denominator3, Decimal3) # создаём новый набор
    K = (Numerator1 / Denominator1 + Whole2 + Numerator2 / Denominator2) * Whole3 # значение выражения меняем на новое
print('Вид выражения: (', Numerator1, '/', Denominator1, '+', Whole2, '+', Numerator2, '/', Denominator2, ')*', Whole3, sep="") # Вид
print('Найди значение выражения $$\Big( \\frac', '{', Numerator1, '}{',  Denominator1, '} + ', Whole2, '\\frac', '{', Numerator2, '}{', Denominator2, '}\Big) \cdot ', Whole3, '.$$', sep="")# LATEX
print('Ответ: ', round(K, 5), sep="", end='\n\n')# значение выражения