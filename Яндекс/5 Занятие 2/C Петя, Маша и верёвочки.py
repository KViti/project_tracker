# На столе лежали две одинаковые верёвочки целой положительной длины.
# Петя разрезал одну из верёвочек на N частей, каждая из которых имеет целую положительную длину, так что на столе стало N+1 верёвочек.
# Затем в комнату зашла Маша и взяла одну из лежащих на столе верёвочек.
# По длинам оставшихся на столе N верёвочек определите, какую наименьшую длину может иметь верёвочка, взятая Машей.
# Формат ввода
# Первая строка входных данных содержит одно целое число N — количество верёвочек, оставшихся на столе (2 ≤ N ≤ 1000).
# Во второй строке содержится N целых чисел li — длины верёвочек (1 ≤ li ≤ 1000).
# Формат вывода
# Выведите одно целое число — наименьшую длину, которую может иметь верёвочка, взятая Машей.

N = int(input())
stroka = input()
a = [int(x) for x in stroka.split()]
maximum=max(a)
summa=sum(a)
if 2*maximum<=summa:
    minimum=summa
else:
    minimum=abs(summa-2*maximum)
print(minimum)