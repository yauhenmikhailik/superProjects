
# file = open('names.txt', 'r')
# res = file.read()
# name = 'Maya'

# print(file.read())
# print(res)

# for i in file:
#     print(i)
# file.write(name)
# print(file.readline())
# print(file.readline())
# print(file.readlines())
#
# with open('names.txt', 'r+') as file:
#     arr_string_from = file.readlines()
#     print(arr_string_from)
#     for i  in arr_string_from:
#         if i == 'hello\n' or i == 'hello':
#             print('pop')
#             arr_string_from.

with open('names.txt', 'r+') as file:
    arr = file.readlines()
    arr1 =[]
    for i in arr:
       arr1.append(int(i.strip()))
    #удаление символов переноса строки и добавление в новый массив
#функция для вычесления среднеего значения
def summarr(list):
    return sum(list)/len(list)

summa = summarr(arr1)
summa = str(summa)
with open('sumarr.txt', 'w') as file:

    file.write(summa)

#Напишите программу, которая находит минимальное и
# максимальное среди чётных положительных чисел,
# записанных в файле, и выводит результат в другой файл.
# Учтите, что таких чисел может вообще не быть

with open('les-s.txt', 'r') as file:
    arr = file.readlines()
    arr2 = []
    for i in arr:
        if int(i) >0:
            arr2.append(int(i.strip()))
    if len(arr2) == 0:
        print('Положительных чисел нет')
    # print(arr2)

def max_number(list):
    list.sort()
    a = str(list[0])
    b = str(list[-1])
    with open('max_number.txt', 'a+') as file:
        file.write("Min number =" + a + "\n" + "Max number =" + b + "\n")


max_number(arr2)

# 3. В файле в столбик записаны целые числа, сколько их –
# неизвестно. Напишите программу, которая определяет
# длину самой длинной цепочки идущих подряд одинаковых
# чисел и выводит результат в другой файл.

with open('3.txt', 'r') as file:
    arr = file.readlines()
    arr3 = []
    for i in arr:
        arr3.append(i.strip())
    # print(arr3)

def chain(list):
    chain_list = []
    print(list)
    for i in list:
        a = ""
        b = ""
        for el in i:
            a = el
            if el == b:
                chain_list.append(i)
            b = el

    print(chain_list)


chain(arr3)