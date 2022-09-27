# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81

# n = int(input('Enter any number: '))

# element = -3

# for i in range(0, n):
#     print(element**i, end=" ")


# 2. Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.
    
#     *Пример:*
    
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input("Enter a natural number: "))

# element = 1

# for i in range(1, n+1):
#     element = 3 * i + 1
#     print(element, end=" ")

# n = int(input("Enter a natural number: "))

# element = 1

# for i in range(1, n+1):
#     element = 3 * i + 1
#     print(i, ":", element, ",", end=" ")

# x = int(input('введите число: '))
# count = 0
# array = []
# a = 1
# print(type(array))
# while count < x:
#     array.append(a) 
#     a = a* (-3)
#     count += 1

# print (f'{x} = {array}')

# x = int(input('введите число: '))
# dic = {}
# for i in range(1,x+1):
#     dic[i] = 3 * i + 1
#     i += 1

# print(dic)


# def PrintList (spisok):
#     for i in range(len(spisok)):
#         print(f'{i+1}: {spisok[i]}', end='    ')

# n=int(input('Введите число: '))
# spisok=[]

# for i in range (1,n+1):
#     spisok.append(3*i+1) 

# PrintList(spisok)





# 3. Напишите программу, в которой пользователь будет задавать две строки,
#  а программа - определять количество вхождений одной строки в другой.


# s = input('Введите первую строку: ')
# s_1 = input('Введите вторую строку: ')

# if len(s) > len(s_1):
#     n = len(s_1)
# else:
#     n = len(s)


# count = 0
# for i in s:
#     for j in s_1:
#         if i == j:
#             count += 1

# print(count)

# word = input('Введите слово: ')
# sub = input('Введите второе слово: ')

# print(f'Слово "{sub}" встерчается {word.count(sub)} раз.')

# st1 = input("Введите 1 строку").split()
# st2 = input("Введите 2 строку").split()
# total = 0
# for i in range(len(st1)):
#     for j in range(len(st2)):
#         if st1[i] == st2[j]:
#             total += 1
# print(total)

# s = input('Введите первую строку: ')
# s_1 = input('Введите вторую строку: ')

# if len(s) < len(s_1):
#     s,s_1 = s_1,s

# count = 0
# for i in s:
#     for j in s_1:
#         if i == j:
#             count += 1

# print(count)








# Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ (в том числе пробел) стоит 
# 60
# 60 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести стоимость строки.




# text=input('Введите текст')
# price_cop=len(text)*60
# print(f'Цена будет {price_cop/100}руб {price_cop%100}коп')

# Тестовые данные 
# Sample Input 1:
# Привет, как дела?!
# Sample Output 1:
# 10 р. 80 коп.
# Sample Input 2:
# Тимур - лучший математик на свете!!
# Sample Output 2:
# 21 р. 0 коп.












# Количество слов

# Дана строка, состоящая из слов, разделенных пробелами. Напишите программу, которая подсчитывает количество слов в этой строке.

# Формат входных данных
# На вход программе подается строка.

# Формат выходных данных
# Программа должна вывести количество слов в строке.

# Примечание 1. Кроме слов в тексте могут присутствовать только пробелы (один или несколько).

# Примечание 2. Решите задачу в одну строчку кода.

# Тестовые данные 
# Sample Input 1:
# Hello world
# Sample Output 1:
# 2
# Sample Input 2:
# Timur forever young
# Sample Output 2:
# 3
# print(len(input("enter string:\r\n").split()))
from cgitb import text

# print(len(input("Введите несколько слов через пробелы: ").split(" ")))

# text = input('Введите текст: ')
# words = text.count(' ')+1
# print(f'Всего {words} слов')



# a=input()
# c=a.split()
# print(len(c))
