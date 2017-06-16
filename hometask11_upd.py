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
    lst = [0, 1]
    n=3
    i=0
    while 1:
        lst.append(lst[i]+lst[i+1])
        i +=1
        n +=1
        yield lst[n-3]

gen=fibonacci()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
















    
    












