#1 Импортировать сам модуль
# import Lesson_7
# print(Lesson_7.get_time())
# print(Lesson_7.hello())

#2 Импортировать отдельные определения из модуля
# from Lesson_7 import get_time, hello
# print(get_time())
# print(hello())

#3 Импортировать всё содержимое модуля сразу
# from Lesson_7 import *
# print(get_time())
# print(hello())
# print(it)

###########################################3
from Lesson_7 import numbers, chet

def chet_nechet(num : list) -> list:
    for i in num:
        if i %2 == 0:
            chet.append(i)
    return chet
# print(chet_nechet(numbers))
