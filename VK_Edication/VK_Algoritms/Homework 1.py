# На вход подается не отсортированный массив целых чисел и некоторое целое число «element».
# Необходимо написать функцию, которая вернет количество элементов, которые не равны данному числу «element».
# Возвращаемое значение после работы функции обозначает количество чисел не равные «element».
n = int(input())
a = map(int, input().split())
k = int(input())
suma=0
for i in a:
    if i!=k:
        suma+=1
print(suma)