#Задание 5
def p_or_s(num1:int , num2:int) ->int:
    operator = input("P or S:") 
    if operator == "P": 
        print ((2*num1) + (2*num2)) 
    elif operator == "S": 
        print(num1*num2) 
    else: 
        print("Неправильный оператор!!!")

#Задание 6
lst = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]
def a():
    return lst[::-1]

#Задание 7
def time():
    hours = 10
    minute = 1
    second = 60
    def ask(hours, minute,second):
        return {hours * 3600 + minute * 60 + second}
    print(ask(hours,minute,second))

#Задание 8
def chatbot():
   while True:
        word = input("Введите сообщение: ")
        if len(word) > 2 and "?" in word:
            print("Конечно!")
        elif word == word.upper() and len(word) > 1:
            print("Успокойся")
        elif "" in word and len(word) == 0:
            print("Как классно, когда ты молчишь. Продолжай в том же духе")
        else:
            print("Ну и что")

#Задание 9
def nur4(b):
    c = b.title().split()
    for i in range(len(c)):
        print(c[i][0], end='')

#Задание 10
menu = {
'Beef Stroganoff': 350,
'Burger': 200,
'Meatloaf': 500,
'Chicken Pot Pie': 400,
'Beefshteks': 650}
new_menu = {k: v + 50 for k, v in menu.items()}
