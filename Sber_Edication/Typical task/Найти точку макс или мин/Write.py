import random
import openpyxl
import pandas as pd
book = openpyxl.Workbook()
sheet = book.active


def TRU(a, b):  # Функция для генерации нового набора значений
    a, b = random.randint(2, 100), (-1) ^ random.randint(1, 2) * random.randint(2, 100)  # Генерация набора значений
    return a, b

sheet['B1'].value = 0
znak = ''
for i in range(1, 100, 4):
    a, b, c = random.randint(2, 100), (-1) ^ random.randint(1, 2) * random.randint(2, 100), (-1) ^ random.randint(1, 2) * random.randint(1, 100)
    if c > 0:
        znak = '+'
    else:
        znak = '-'

    print('Пример 1, Максимум:\sqrt{c+bx+ax^2}')
    K = -b / (2 * -a)  # Ответ
    while (round(K * 100 - int(K * 100), 5) != 0):  # Пока после запятой более 1 цифры
        a, b = TRU(a, b)  # создаём новый набор
        K = -b / (2 * -a)  # Ответ выражения меняем на новое


    if (b > 0):
        # print('Вид выражения: ', u'\u221a', c, '+', b, 'x-', a, 'x^2', sep="")  # Вид
        print('Найдите точку максимума функции $$\sqrt{', c, '+', b, 'x-', a, 'x^2' '}.$$', sep="")  # LATEX
        # print('Ответ: -b/(2*-a)=', str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
        print(str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
        string = 'Найдите точку максимума функции $$\sqrt{' + str(c) + '+' + str(abs(b)) + 'x-' + str(a) + 'x^2' '}.$$'
    else:
        # print('Вид выражения: ', u'\u221a', c, '-', abs(b), 'x-', a, 'x^2', sep="")  # Вид
        print('Найдите точку максимума функции $$\sqrt{', c, '-', abs(b), 'x-', a, 'x^2' '}.$$', sep="")  # LATEX
        # print('Ответ: -b/(2*-a)=', str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
        print(str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
        string = 'Найдите точку максимума функции $$\sqrt{' + str(c) + '-' + str(abs(b)) + 'x-' + str(a) + 'x^2' '}.$$'
    sheet[i][0].value = string
    sheet[i][1].value = K

    print('Пример 2, Минимум:\sqrt[n]{ax^2+bx+c}')
    K = -b / (2 * a)  # Ответ
    while (round(K * 100 - int(K * 100), 5) != 0):  # Пока после запятой более 1 цифры
        a, b = TRU(a, b)  # создаём новый набор
        K = -b / (2 * a)  # Ответ выражения меняем на новое

    if (b > 0):
        # print('Вид выражения: ', u'\u221a', c, '+', b, 'x+', a, 'x^2', sep="")  # Вид
        print('Найдите точку минимума функции $$\sqrt{', a, 'x^2', '+', abs(b), 'x', znak, abs(c), '}.$$', sep="")  # LATEX
        # print('Ответ: -b/(2*-a)=', str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
        print(str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
        string = 'Найдите точку минимума функции $$\sqrt{' + str(a) + 'x^2' + '+' + str(abs(b)) + 'x' + znak + str(abs(c)) + '}.$$'
    else:
        # print('Вид выражения: ', u'\u221a', c, '-', abs(b), 'x+', a, 'x^2', sep="")  # Вид
        print('Найдите точку минимума функции $$\sqrt{', a, 'x^2', '-', abs(b), 'x', znak, abs(c), '}.$$', sep="")  # LATEX
        # print('Ответ: -b/(2*a)=', str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
        print(str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
        string = 'Найдите точку минимума функции $$\sqrt{' + str(a) + 'x^2' + '-' + str(abs(b)) + 'x' + znak + str(abs(c)) + '}.$$'
    sheet[i + 1][0].value = string
    sheet[i + 1][1].value = K

    print('Пример 3, Максимум:\sqrt[n]{c+bx+x^2}', 'a=-1')
    a = 1
    K = b / 2  # Ответ
    while (round(K * 100 - int(K * 100), 5) != 0):  # Пока после запятой более 1 цифры
        b = (-1) ^ random.randint(0, 1) * random.randint(2, 100)  # создаём новый набор
        K = b / 2  # Ответ выражения меняем на новое


    if (b > 0):
        # print('Вид выражения: ', u'\u221a', c, '+', b, 'x-', 'x^2', sep="")  # Вид
        print('Найдите точку максимума функции $$\sqrt{', c, '+', b, 'x-', 'x^2' '}.$$', sep="")  # LATEX
        # print('Ответ: b/2=', str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
        print(str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
        string = 'Найдите точку максимума функции $$\sqrt{' + str(c) + '+' + str(abs(b)) + 'x-' + 'x^2' '}.$$'
    else:
        # print('Вид выражения: ', u'\u221a', c, '-', abs(b), 'x-', 'x^2', sep="")  # Вид
        print('Найдите точку максимума функции $$\sqrt{', c, '-', abs(b), 'x-', 'x^2' '}.$$', sep="")  # LATEX
        # print('Ответ: b/2=', str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
        print(str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
        string = 'Найдите точку максимума функции $$\sqrt{' + str(c) + '-' + str(abs(b)) + 'x-' + 'x^2' '}.$$'
    sheet[i + 2][0].value = string
    sheet[i + 2][1].value = K

    print('Пример 4, Минимум:\sqrt[n]{x^2+bx+c}', 'a=1')
    K = -b / 2  # Ответ
    while (round(K * 100 - int(K * 100), 5) != 0):  # Пока после запятой более 1 цифры
        b = (-1) ^ random.randint(0, 1) * random.randint(2, 100)  # создаём новый набор
        K = -b / 2  # Ответ выражения меняем на новое

    # print('a, b, c=', a, b, c)  # Вид

    if (b > 0):
        # print('Вид выражения: ', u'\u221a', c, '+', b, 'x-', 'x^2', sep="")  # Вид
        print('Найдите точку минимума функции $$\sqrt{x^2', '+', b, 'x', znak, abs(c), '}.$$', sep="")  # LATEX
        # print('Ответ: -b/2=', str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
        print(str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
        string = 'Найдите точку минимума функции $$\sqrt{x^2' + '+' + str(b) + 'x' + znak + str(abs(c)) + '}.$$'
    else:
        # print('Вид выражения: ', u'\u221a', c, '-', abs(b), 'x-', 'x^2', sep="")  # Вид
        print('Найдите точку минимума функции $$\sqrt{x^2', '-', abs(b), 'x', znak, abs(c), '}.$$', sep="")  # LATEX
        # print('Ответ: -b/2=', str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
        print(str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
        string = 'Найдите точку минимума функции $$\sqrt{x^2' + '-' + str(abs(b)) + 'x' + znak + str(abs(c)) + '}.$$'
    sheet[i + 3][0].value = string
    sheet[i + 3][1].value = K

book.save("test1.xlsx")
book.close()