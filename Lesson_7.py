#Лямбда функции
# def hello_world(x):
#     return x * x
# print(hello_world(10))
#
# hello = lambda x: x * x
# print(hello(10))
#
# print((lambda x: x * x)(10))

###############################

# def mult(num1 : int = 2, num2 : int = 2) -> int:
#     return num1 * num2
# print(mult(10, 5))
# print(mult())
#
# lambda_mult = lambda num1, num2: num1 * num2
# print(lambda_mult(10, 5))
#
# print((lambda num1, num2: num1 * num2)(10, 5))

###############################

# number = [10, 20, 1, 2, 4, 111, 9090]
# chet = []
# def chet_func(num : list) -> list:
#     for n in num:
#         if n %2 == 0:
#             chet.append(n)
#     return chet
# print(chet_func(number))
# ################################
# number = [10, 20, 1, 2, 4, 111, 9090]
# chet = list(filter(lambda num: num %2 == 0,number))
# print(chet)
# ################################
# number = [10, 20, 1, 2, 4, 111, 9090]
# print(list(filter(lambda num: num %2 == 0,number)))
# ################################
# print(list(filter(lambda num: num %2 == 0, [10, 20, 1, 2, 4, 111, 9090])))

#################################
# num = [10, 20, 30, 40, 50]
# lst = []
# def mult_two(num_list : list) -> list:
#     for i in num_list:
#         lst.append(i * 2)
#     return lst
# print(mult_two(num))
# ################################
# num = [10, 20, 30, 40, 50]
# lst = list(map(lambda num_list: num_list * 2, num))
# print(lst)
# ###################################
# num = [10, 20, 30, 40, 50]
# print(list(map(lambda num_list: num_list * 2, num)))
# ##############################################
# print(list(map(lambda num_list: num_list * 2, [10, 20, 30, 40, 50])))


###########Модули###################
# import time
#
# def get_time():
#     return time.ctime()
#
# def hello():
#     return "Hello World"
#
# it = "GeekTech"

# print(get_time())

numbers = [1, 2, 3, 4, 5]
chet = []