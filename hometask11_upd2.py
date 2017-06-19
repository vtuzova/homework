import random
import string
import time

'''
Задача №1.
Реализовать генератор чисел Фибоначчи.
Генератор принимает один обязательный аргумент - количество элементов последовательности.
fibonacci(10)
'''


def fibonacci():
    f=0
    f2=1
    i=0
    while 1:
        if i==0:
            i +=1
            yield f
        elif i==1:
            i +=1
            yield f2
        elif i>=2:
            fib = f + f2
            f, f2 = f2, fib
            yield fib

gen=fibonacci()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
















    
    












