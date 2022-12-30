#Задание 1
# it_company = ('Google', 'Amazon', 'Microsoft')
            #012
# lst_it_company = list(it_company)
# lst_it_company.append("Tesla")
# print(lst_it_company)

#Задание 2
# lst_it_company.remove('Amazon')
# print(lst_it_company)

#Задание 3
# lst_it_company[0] = 'Apple'
# print(lst_it_company)

#Задание 4
# print(lst_it_company[0:3])

#Задание 5
# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
# 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean',
# 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite',
# 'with', 'our', 'python', '3', 'overview')
# print(" Слово << Python >> : ", text_tuple.count("Python"))

#Задание 6
# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_3 = dictionary_1.copy()
# dictionary_3.update(dictionary_2)
# print(dictionary_3)

#Задание 7
# numbers = {'num_1' : 1 * 5, 'num_2' : 2 * 5, 'num_3': 3 * 5, 'num_100' : 100 * 5}
# result = 1
# for key in numbers:
#     result = result * numbers[key]
# print(result)

#Задание 8
# student = {'name' : 'Askhat', 'age' : 17 * 2}
# print(student)

#Задание 9
# student.pop('age')
# print(student)

#Задание 10
# student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
# student['age'] = '16'
# print(student)

#Задание 11
# student = {'name' : 'Askhat'}
# student['address'] = 'ЗападныйАнар'
# print(student)

#Дополнительное задание 12
# print("Введите пароль:")
# password = input()
# print("Подтвердите:")
# password2 = input()
# while len(password) < 8:
#     print("Короткий!")
#     password = input()
#     password2 = input()
# while "123" in password:
#     print("Простой!")
#     password = input()
#     password2 = input()
# while password2 != password:
#     print("Различаются.")
#     password = input()
#     password2 = input()
# else:
#     print("OK\nПароль создан!")

#Дополнительное задание 13
# contact = {"Askhat" : "0778909091"}
# while True:
#     command = input("1 - получить все контакты, 2 - добавить контакт, 3 - удалить контакт, 4 - обновить контакт: ")
#     if command == "1":
#         print(contact)
#     elif command == "2":
#         add_name = input("Введите имя: ")
#         add_number = input("Введите номер: ")
#         if add_name not in contact.keys():
#             contact.setdefault(add_name, add_number)
#             print("Успешно добавлено")
#         else:
#             print("Такой контакт уже существует")
#     elif command == "3":
#         delete_contact = input("Кого удалить?: ")
#         if delete_contact in contact:
#             contact.pop(delete_contact)
#             print("Успешно удалено")
#         else:
#             print("Такого контакта нет")
#     elif command == "4":
#         update_contact = input("Кого хотите oбновить: ")
#         if update_contact in contact:
#             number_update = input("Введите номер контакта: ")
#             contact[update_contact] = number_update
#             print("Контакт обновлен.")
#         else:
#             print("Контакт не найден.")