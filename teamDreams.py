###################
import os
import random as rd
random_number = rd.randint(0,10)
print(random_number)
###################
# С помощью функции:
#    my_number = int(input("Введите число: "))
# спрашивайте число от пользователя.
# Запустите бесконечный цикл!
# И пытайтесь спрашивать у пользователя какое-то число каждый раз.
# Если пользователь угадал число которое сгенерировал компьютер остановите цикл и скажите пользователю - "Вы угадали!"
# Если пользователь не угадал вы снова спросите у него число.
# Если пользователь 3 раза подряд не угадал число, вы останавливаете цикл и говорите: "Вы проиграли..."
#######################################################################

def game_numbers():
    counter = 0
    my_number = int(input("Введите число: \n"))
    while True:
        if my_number == random_number:
            print("вы угадали")
            break
        else:
            print("не угадали, го еще разок: \n")
            my_number = int(input("Введите число: \n"))
            counter += 1
            if counter >= 3:
                print('вы проиграли')
                break

#game_numbers()



# Задание 2:
        # Напишите программу, которая циклично запрашивает у пользователя номера символов по таблице Unicode и выводит соответствующие им символы.
        # Завершает работу при вводе нуля.
###################################################################


# делала по таблице из Вики,графа "Decimal" https://en.wikipedia.org/wiki/List_of_Unicode_characters
def get_symbols():
    while True:
        symbol = int(input('введите '))
        if symbol == 0:
            break
        else:
            return chr(symbol)


#print(get_symbols())


# Задание 3:
        # Напишите программу, которая измеряет длину введенной строки.
        # Если строка длиннее десяти символов, то выносится предупреждение.
        # Если короче, то к строке добавляется столько символов *, чтобы ее длина составляла десять символов, после чего новая строка должна выводиться на экран.
###################################################################

def len_sequence(a):
    myLen = len(a)
    if myLen > 10:
        print("WARNING")
    else:
        ostatok = 10 - myLen
        a += ('*'*ostatok)
    return a

#print(len_sequence(input('введите ')))


# Задание 4:
        # Напишите программу, которая запрашивает у пользователя шесть вещественных чисел.
        # На экран выводит минимальное и максимальное из них, округленные до двух знаков после запятой.
        # Выполните задание без использования встроенных функций min() и max().
def min_max():
    v_ch = []
    for i in range(6):
        v_ch.append(float(input("Введите вещественные числа -> ")))

    naibolwee = v_ch[0]
    naimenwee = v_ch[0]

    for i in v_ch:
        if naibolwee > i:
            naibolwee = i
        else:
            naimenwee = i
    result = f"Max: {round(naibolwee, 2)} | Min: {round(naimenwee, 2)}"
    return result

#print(min_max())


# Задание 5:
        # Напишите программу которая принимает число любой длины и вытаскивает из него самое большое и самое маленькое число.
####################################################################

def GetNumber(a:int):
    list=[]
    for i in range(len(str(a))):
        list.append(str(a)[i])
    return f'минимальное: {min(list)} и максимальное: {max(list)}'


print(GetNumber(int(input('введите число'))))



# Задание 6:
#     Функция
#     Напишите функцию, которая берет текст, и возвращает строковое значение, состоящее из заглавных букв.
#     Используйте текст, данный выше (The Zen of Python).
#     Подсказка: используйте метод строчных значений, который проверяет, “заглавность” буквы.
##################################################################

def my_text():
    text = """
    The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
    Simple is better than complex.Complex is better than complicated.
    Flat is better than nested.Sparse is better than dense.
    Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
    Errors should never pass silently.Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one--and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea --let's do more of those!
    """
    text2 = text.title()
    return text2

print(my_text())

# Задание 7:
#     Чтение из файла.
#     Создайте файл с текстом The Zen of Python.
#     Напишите функцию, которая считайте его и возвратит список из слов, которые начинаются на букву “c” или “C”.
#     Подсказка: используйте метод строчных значений, который проверяет, начинается ли слово на переданную букву.
####################################################################

def reading():
    list = []
    with open('zen.txt', "w") as f:
        f.write('The Zen city of Python')
    with open("zen.txt", "r") as rd:
        data = rd.read().split()
        for i in data:
            if i.lower().startswith('c'):
                list.append(i)
    return list


#print(reading())


# Задание 8:
#     Банкомат
#     Напишите код банкомата, который принимает цифру, выдает деньги с номиналом 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1.
#     Подсказка: напишите функцию, используйте divmod()
##################################################################
def Bankomat():
    list = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1]
    a = input("введтие цифру в банкомате")
    for i in list:
        print(i)


Bankomat()






# Задание 9:
#     Напишите функцию которая принимает два аргумента (числа), умножает их друг на друга,
#         и возвращает функцию, которая также берет два аргумента (числа),
#             и возвращает результат умножения аргументов внешней функции плюс результат деления
#                 аргументов внутренней функции.
#     Подсказка: (outer_arg1 * outer_arg2) + (inner_arg1 / inner_arg2)
####################################################################

# сформулировано коряво, я не поняла
def myFunc(a,b):
    c = a*b
    return myFunc2(a,b)


def myFunc2(x,y):
    return f'результат умножения {x*y} и деления {x/y}'

# aa = int(input('число 1: '))
# bb = int(input('число 2: '))
#print(myFunc(aa, bb))



#заданеи 10
text = """
    The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
    Simple is better than complex.Complex is better than complicated.
    Flat is better than nested.Sparse is better than dense.
    Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
    Errors should never pass silently.Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one--and preferably only onUP,BROADCAST,RUNNING,MULTICASTe --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea --let's do more of those!
    """
myList = ''
def myFilter():

    list = []
    # x = text.replace('\n', ' ')
    list.append(text.split())
    for i in list:
        if i == 'p':
            return list;
        else:
            return  False

print(myFilter())
filt = filter(myFilter, text)

for x in filt:
    myList += x



# Задание 11:
#     Дано
    # dict_one = {'a':1, 'b':2, 'c':3}
    # dict_two = {'d':4, 'e':5, 'f':6}
    # dict_three = {'g':7, 'h':8, 'i':9}
    # dict_four = {}
#     С помощью цикла for необходимо собрать три первых словаря в словарь dict_four

#     Подсказка: Для удобства итерации, первые три словаря можно записать в кортеж (dict_one, dict_two, dict_three

def SetDictionary():
    dict_one = {'a':1, 'b':2, 'c':3}
    dict_two = {'d':4, 'e':5, 'f':6}
    dict_three = {'g':7, 'h':8, 'i':9}
    dict_four = {}

    t = tuple(dict_one)
    t2 = tuple(dict_two)
    t3 = tuple(dict_three)
    common = t+t2+t3

    for i in range(1, len(common)):
        dict_four[i] = common[i]
    return dict_four

print(SetDictionary())

# Задание 12:
#     Аналог шифра цезаря ". Программа должна запрашивать элементы
#     списка через пробел. После чего пользователь должен ввести значение
#     для сдвига элементов списка. Значение может быть как положительным,
#     так и отрицательным. Если значение положительное, элементы списка
#     должны сдвигаться вправо, если отрицательное - влево. Результат
#     необходимо вывести на экран:

#     Пример:
#     [1, 2, 3, 4, 5], сдвиг 2
#     [3, 4, 5, 1, 2]
#####################################################################
def Cezar():
    newStr = ''
    el = input('сиферки черех пробел: ').split(' ')
    a = int(input('введеит сиферку для сдвига: '))
    l = []
    for i in el:
        i = a+int(i)
        l.append(str(i))
    res = f'''{el} со сдвигом {a}
    {l}
    '''
    return res

#print(Cezar())

# Задание 13:
#     Напишите программу, где исходный список содержит положительные и отрицательные числа.
#     Требуется положительные поместить в один список, а отрицательные - в другой.
###################################################################

#так как про НОЛЬ ничего не сказано, то я его игнориурю
def positive_negative():
    postive =[]
    negative = []
    randomlist = []
    for i in range(0, 5):
        n = rd.randint(-10, 10)
        randomlist.append(n)
    for i in randomlist:
        if i > 0:
            postive.append(i)
        elif i < 0:
            negative.append(i)
    return f'из исходного лисат {randomlist} положительные: {postive} , отрицательные: {negative}'

#print(positive_negative())

# Задание 14:
#     Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
#####################################################################
def season(n:int):
    if n > 12:
        print('нет такого числа ')
    else:
        if n == 12 or n < 3:
            return "Зима"
        elif n == 3 or n < 6:
            return "Весна"
        elif n == 6 or n < 9:
            return "Лето"
        else:
            return "Осень"

a= int(input('введите число: '))
#print(season(a))

