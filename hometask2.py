# Задание_1
'''
Задача №1.
Написать функцию, которая проверяет, является ли переданное число или строка палиндромом и возвраащет True.
В противном случаи возвращает False.
Палиндром - это число или текст, который читается одинаково и слева, и справа: 939; 49094; 11311.
'''

def find_palindrome(args):
    args = str(args) 
    args = args.lower() #добавляем преобразование строки на случай, если проверяемое слово пишется с большой буквы - 
                        #например, как имя Анна, но при этом читается одинаково и слева, и справа
    n = 0               
    x = False
    
    for i in range(len(args)):
        if args[i] == args[-i-1]:
            n += 1
    if n == len(args):
        x = True
    return x
        

print(find_palindrome(12321))
print(find_palindrome(68745354))
print(find_palindrome('Anna'))
print(find_palindrome('cosinus'))


# Задание_2
'''
Задача №2.
Написать функцию, которая принимает координаты точки (x, y) и возвращает номер четверти, которой эта точка принадлежит.
'''

def point_quarter(x, y):
    # сначала опишем исключения - когда точка лежит на оси
    if x == 0 and y == 0:
        return 'точка лежит в начале координат' # прерываем функцию, чтобы в таком случае не вывелось еще про оси X и Y
    if x == 0:
        return 'точка принадлежит оси X'
    if y == 0:
        return 'точка принадлежит оси Y'
    
    answ = 2 # зададим четверть, в которой лежит точка по умолчанию
    if x < 0 and y < 0:
        answ = 3
    if x > 0:
        if y < 0:
            answ = 4
        else:
            answ = 1
    return answ
        


print(point_quarter(0, 0))
print(point_quarter(0, 5))
print(point_quarter(-5, -1)) #3
print(point_quarter(-5, 1))  #2
print(point_quarter(5, -1))  #4
print(point_quarter(5, 1))   #1


# Задание_3
'''
Задача №3.
Написать функцию, которая принимает список из целых чисел, например - [1, 2, 3, 8, 14, 89, 45],
выполняет сортировку списка по возрастанию методом пузырька и возвращает получившийся список.
(!) Запрещено использовать встроенные возможности языка для сортировки.
* https://ru.wikipedia.org/wiki/Сортировка_пузырьком#.D..
(!) Т.к. готовый код данной задачи легко нагуглить, то необходимо пояснить каждую строчку в коде с помощью комментариев!
'''

def bubble(*args):
    
    if type(args) is not list:
        args = list(args) # кладем в список все, что передает аргумент функции
                          # нужно, чтобы функция работала как с переданным набором чисел, так и при
                          # обращении к имени уже существующего списка

    checker = len(args) -1 # задаем счетчик для внутреннего цикла. это будет порядковый номер элементов списка при переборе

    bell = True # еще один счетчик. это "колокольчик", который срабатывает, если была хоть одна перестановка чисел при проходе по циклу
                # запускает повторную проверку всего ряда

    while checker >= 0 or bell == True: # цикл работает пока не проверенны все числа в списке и пока за проверку ряда не будет ни одной перестановки чисел
        bell = False # обнуляем счетчик 
        for i in range(checker): # начинаем перебор соседних элементов
            if args[i] > args[i+1]:
                args [i+1], args[i] = args[i], args[i+1] # если элементы не по порядку, производим замену
                bell = True # если элементы не по порядку, добавляем срабатывание "колокольчика"
        checker -= 1
    return args # возврат нового списка


lst = [0, 5, 2, 6, 1, 11]
print(bubble(*lst))
print(bubble(1, 7, 9, 0, 3))





















    
