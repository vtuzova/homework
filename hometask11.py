import random
import string
import time

'''
Задача №1.
Реализовать генератор чисел Фибоначчи.
Генератор принимает один обязательный аргумент - количество элементов последовательности.
fibonacci(10)
'''


def fibonacci(n):
    if n<1: 
        print('укажите большее число')
        lst = []
    if n == 1:
        lst = [0]
    if n>=2:
        lst = [0, 1]
        for i in range(n-2):
            lst.append(lst[i]+lst[i+1])
    yield lst



n = int(input('введите целое число'))
print('последовательность из {}'.format(n), 'чисел: ', next(fibonacci(n)))


'''
Задача №2.
Реализовать генератор случайных паролей указанной длины.
'''


def password(n):
    while 1:
        s = str(string.ascii_letters + string.digits + string.punctuation)
        pswd = str('')
        n = int(n)
        
        if n<1: 
            print('укажите большее число')
        else:
            for i in range(n):
                pswd+=random.choice(s) 
        yield pswd
        
gen = password(15)

print('Случайный пароль №1: {}'.format(next(gen)))
print('Случайный пароль №2: {}'.format(next(gen)))
print('Случайный пароль №3: {}'.format(next(gen)))




'''
Задача №3.
Реализовать декоратор с параметрами pause, который приостанавливает выполнение функции
на указанное количество секунд.
'''

def pause(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('Подождите {}'.format(n),' секунд')
            time.sleep(n)
            return func (*args, **kwargs)

        return wrapper
    return decorator
        

@pause(5)
def cup_of_coffee(price, name='Чашка кофе'):
    print('Вы заказали: {}'.format(name))
    print('Стоимость заказа: {}'.format(price))

cup_of_coffee(60)








    
    












