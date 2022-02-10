# Напишите программу Python, которая принимает слово от пользователя и переворачивает его Пример: input - Hello Worlds output - sdlroW olleH

var = input("Input a word: ")
for i in range(len(var) -1, -1, -1):
    print(var[i], end='')
print("\n")

# Напишите программу Python для построения следующего шаблона, используя вложенный цикл for.
# Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке убывания если A > B

a = int(input())
b = int(input())

if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, - 1):
        print(i)

# Даны два целых числа A и B (при этом A < B). Выведите все числа от A до B включительно.

a = int(input())
b = int(input())

if a < b:
    for i in range(a, b + 1):
        print(i)

# Напишите программу, которая удаляет дубликаты элементов из списка.

a = [1,2,2,3,1,4,5,4,4,6,8,10,8]
duplicates = set()
uniqs = []
for x in a:
    if x not in duplicates:
        uniqs.append(x)
        duplicates.add(x)
print(duplicates)

# Напишите программу, которая копирует список
#
list1 = [3, 2, 3, 4, 5, 4, 6]
list2 = list(list1)
print(list1)
print(list2)

# Напишите программу, которая находит разницу между двумя списками и сохраняет ее в новый список. Вывести результат на экран.

list_1 = [1, 2, 10, 20, 4, 40]
list_2 = [5, 10, 20, 25, 40, 50]

list3 = []
for element in list_1:
    if element not in list_2:
        list3.append(element)

print(list3)

# Напишите программу для объединения следующих словарей для создания нового

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)

# Напишите программу, которая выводит словарь, в котором ключи представляют собой числа от 1 до 15 (оба включены),
# а значения представляют собой квадраты ключей. Генерация ключей и значений должна быть выполнена через цикл.

d = dict()
for x in range(1,16):
    d[x] = x ** 2
print(d)
