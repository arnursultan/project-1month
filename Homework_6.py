#Задание 1
# def shorter(phrase):
#     phrase_dict = phrase.split()
#     for n in range(len(phrase_dict)):
#         print(phrase_dict[n][0], end = "" )
# shorter("Российская Федерация , Detective Comics , Lionel Messi 1 0")

#Задание 2
# from re import findall
# from collections import Counter
#
# text = "I don’t care what you think about me. I don’t think about you at all."
# print(Counter(findall('\S*\w', text.lower())))

# #Задание 3
# def isogramm(word):
#     no_duplicate = set(word)
#     if len(word) == len(no_duplicate):
#         return True
#     else:
#         return False

# result = isogramm(input("Введите слово: "))
# print(result)

#Задание 4
# n1 = int(input("Введите целое число: "))
# n2 = 0
# while n1 > 0:
#     digit = n1 % 10
#     n1 = n1 // 10
#     n2 = n2 * 10
#     n2 = n2 + digit
#
# print('"Обратное" ему число:"', n2)

#Дополнительное задание 5
# def chat_bot():
#     while True:
#         word = input("Введите сообщение: ")
#         if len(word) > 2 and "?" in word:
#             print("Конечно!")
#         elif word == word.upper() and len(word) > 1:
#             print("Успокойся")
#         elif "" in word and len(word) == 0:
#             print("Как классно, когда ты молчишь. Продолжай в том же духе")
#         else:
#             print("Ну и что")
# chat_bot()
