import random
import openpyxl
import math

book = openpyxl.Workbook()
sheet = book.active
sheet['B1'].value = 0


def TRU_3(a, b, c):  # Функция для генерации нового набора значений
    a, b, c = random.randint(2, 100), (-1) ** random.randint(1, 2) * random.randint(2, 100), (-1) ** random.randint(1, 2) * random.randint(1, 100)  # Генерация набора значений
    return a, b, c

def TRU_2(b, c):  # Функция для генерации нового набора значений
    b, c = (-1) ** random.randint(1, 2) * random.randint(2, 100), (-1) ** random.randint(1, 2) * random.randint(1, 1000)  # Генерация набора значений
    return b, c

# def Discriminant(a, b, c):  # Функция для генерации нового набора значений
#     return b**2-4*a*c

def znak(t):  # Функция для определения знака
    if c > 0:
        return '+'
    else:
        return '-'


for i in range(1, 100, 4):
    n = random.randint(2, 10)
    t = random.randint(2, 10)
    a, b, c = random.randint(2, 100), (-1) ** random.randint(1, 2) * random.randint(2, 100), (-1) ** random.randint(1, 2) * random.randint(1, 100)

    print('Пример 1, Максимум:\log_[n]{c+bx-ax^2}')
    K = c+b*(b/(2*a))-a*(b/(2*a))**2 # Ответ
    while (K<=0 or round(math.log(K, n) * 100 - int(math.log(K, n) * 100), 5) != 0):  # Пока после запятой более 1 цифры
        a, b, c = TRU_3(a, b, c)  # создаём новый набор
        K = c + b * (b / (2 * a)) - a * (b / (2 * a)) ** 2  # Ответ выражения меняем на новое
    print('Найдите наибольшее значение функции $$ \log_', n, '(', c, znak(b), abs(b), 'x-', a, 'x^2)', '+', t, '.$$',sep="")  # LATEX
    print(str(math.log(K, n)).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
    string = 'Найдите наибольшее значение функции $$ \log_' + str(n) + '(' + str(c) + znak(b) + str(abs(b)) + 'x-' + str(a) + 'x^2)+' + str(t) + '.$$'
    sheet[i][0].value = string
    sheet[i][1].value = str(round((math.log(K, n)+t), 2)).rstrip("0").rstrip(".")

    print('Минимум:\sqrt{c+bx+ax^2}')
    K = c-b*(b/(2*a))+a*(b/(2*a))**2 # Ответ
    while (K<=0 or round(math.log(K, n) * 100 - int(math.log(K, n) * 100), 5) != 0):  # Пока после запятой более 1 цифры
        a, b, c = TRU_3(a, b, c)  # создаём новый набор
        K = c-b*(b/(2*a))+a*(b/(2*a))**2# Ответ выражения меняем на новое
    print('Найдите наименьшее значение функции $$ \log_', n, '(', a, 'x^2', znak(b), abs(b), 'x', znak(c), abs(c), ')', t,
          '.$$', sep="")  # LATEX
    print(str(math.log(K, n)).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
    string = 'Найдите наименьшее значение функции $$ \log_' + str(n) + '(' + str(a) + 'x^2' + znak(b) + str(abs(b)) + 'x' + znak(c) + str(abs(c)) + ')+' + str(t) + '.$$'
    sheet[i+1][0].value = string
    sheet[i+1][1].value = str(round((math.log(K, n)+t), 2)).rstrip("0").rstrip(".")

    print('Максимум:\sqrt{c+bx-x^2}', 'a=-1')
    a = 1
    K = c+b*(b/2)-(b/2)**2 # Ответ
    while (K<=0 or round(math.log(K, n) * 100 - int(math.log(K, n) * 100), 5) != 0): # Пока после запятой более 1 цифры
        b, c = TRU_2(b, c)
        K = c + b * (b / 2) - (b / 2) ** 2  # Ответ
    # Ответ выражения меняем на новое
    print('Найдите наибольшее значение функции $$ \log_', n, '(', c, znak(b), abs(b), 'x-', 'x^2)', '+', t, '.$$',
          sep="")  # LATEX
    print(str(math.log(K, n)).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
    string = 'Найдите наибольшее значение функции $$ \log_' + str(n) + '(' + str(c) + znak(b) + str(abs(b)) + 'x-' + 'x^2)+' + str(t) + '.$$'
    sheet[i+2][0].value = string
    sheet[i+2][1].value = str(round((math.log(K, n)+t), 2)).rstrip("0").rstrip(".")


    print('Минимум:\sqrt{c+bx+x^2}')
    K = c-b*(b/2)+(b/2)**2 # Ответ
    while (K<=0 or round(math.log(K, n) * 100 - int(math.log(K, n) * 100), 5) != 0):  # Пока после запятой более 1 цифры
        b, c = TRU_2(b, c)
        K = c-b*(b/2)+(b/2)**2  # Ответ выражения меняем на новое
    print('Найдите наименьшее значение функции $$ \log_', n, '(x^2', znak(b), abs(b), 'x', znak(c), abs(c), ')+', t, '.$$', sep="")  # LATEX
    print(str(math.log(K, n)).rstrip("0").rstrip("."), sep="", end='\n\n')  # значение выражения
    string = 'Найдите наименьшее значение функции $$ \log_' + str(n) + '(x^2' + znak(b) + str(abs(b)) + 'x' + znak(c) + str(abs(c)) + ')+' + str(t) + '.$$'
    sheet[i+3][0].value = string
    sheet[i+3][1].value = str(round((math.log(K, n)+t), 2)).rstrip("0").rstrip(".")

book.save("test4.xlsx")
book.close()