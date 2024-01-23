import random
import openpyxl

book = openpyxl.Workbook()
sheet = book.active
sheet['B1'].value = 0
def TRU(a, b):  # Функция для генерации нового набора значений
    a, b = random.randint(2, 100), (-1) ^ random.randint(1, 2) * random.randint(2, 100)  # Генерация набора значений
    return a, b

def znak(t):  # Функция для определения знака
    if c > 0:
        return '+'
    else:
        return '-'

for i in range(1, 100, 4):
    n = random.randint(2, 10)
    a, b, c = random.randint(2, 100), (-1) ^ random.randint(1, 2) * random.randint(2, 100), (-1) ^ random.randint(0,1) * random.randint(1, 100)

    print('Пример 1, Максимум:')
    K = b / (2 * a)  # Ответ
    while (round(K * 100 - int(K * 100), 5) != 0):  # Пока после запятой более 1 цифры
        a, b = TRU(a, b)  # создаём новый набор
        K = -b / (2 * -a)  # Ответ выражения меняем на новое
    print('Найдите точку максимума функции $$', n, '^{', c, znak(b), abs(b), 'x', '-', a, 'x^2}.$$', sep="")  # LATEX
    print(str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
    string = 'Найдите точку максимума функции $$' + str(n) + '^{' + str(c) + znak(b) + str(abs(b)) + 'x' + '-' + str(a) + 'x^2}.$$'
    sheet[i][0].value = string
    sheet[i][1].value = K

    print('Пример 2, Минимум:')
    K = -b / (2 * a)  # Ответ
    print('Найдите точку минимума функции $$', n, '^{', a, 'x^2', znak(b), abs(b), 'x', znak(c), abs(c), '}.$$', sep="")  # LATEX
    print(str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
    string = 'Найдите точку минимума функции $$' + str(n) + '^{' + str(a) + 'x^2' + znak(b) + str(abs(b)) + 'x' + znak(c) + str(abs(c)) + '}.$$'
    sheet[i + 1][0].value = string
    sheet[i + 1][1].value = K

    print('Пример 3, Максимум:a=-1')
    a = 1
    K = b / 2  # Ответ
    print('Найдите точку максимума функции $$', n, '^{', c, znak(b), abs(b), 'x', '-', 'x^2}.$$',sep="")  # LATEX
    print(str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
    string = 'Найдите точку максимума функции $$' + str(n) + '^{' + str(c) + znak(b) + str(abs(b)) + 'x' + '-' + 'x^2}.$$'
    sheet[i + 2][0].value = string
    sheet[i + 2][1].value = K


    print('Пример 4, Минимум:a=1')
    K = -b / 2  # Ответ
    print('Найдите точку минимума функции $$', n, '^{x^2', znak(b), abs(b), 'x', znak(c), abs(c), '}.$$', sep="")  # LATEX
    print(str(K).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
    string = 'Найдите точку минимума функции $$' + str(n) + '^{x^2' + znak(b) + str(abs(b)) + 'x' + znak(c) + str(abs(c)) + '}.$$'
    sheet[i + 3][0].value = string
    sheet[i + 3][1].value = K

book.save("test5.xlsx")
book.close()
