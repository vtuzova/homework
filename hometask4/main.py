import os
from commands import (redaction, closing, reopen, new_task)

# сначала выводим список возможных действий
print("""
Ежедневник. Выберите действие:

1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
6. Выход
""")

# задаем переменную action, которая будет соответствовать номеру команды в дальнейшем
# задаем done/undone для статуса задачи. можно было бы сделать без этого, но так можно будет в дальнейшем быстро менять формулировку при желании
action = 0


# создаем некий список дел и соответствующий им список статусов, чтобы проверить работает ли программа
task = ['проверить почту', 'записаться на курсы', 'оплатить счета']
status =['выполненo', 'выполненo', 'не выполнено']

# цикл проверки введенного значения
while action is not 6:
    action = int(input('введите число...'))
    if action > 6 or action <= 0:
        print('ошибка')
        break
    elif action == 1:
        for i in range(len(task)):
            print(i+1,' ', task[i], ' :', status[i])            
    elif action == 2:
        print('добавление задачи:')
        new_task(task, status, len(task))
    elif action == 3:
        print('редактирование задачи:')
        redaction(task, int(input('...')))
    elif action == 4:
        print('завершить задачу')
        closing(status, int(input('...')))        
    elif action == 5:
        print('начать задачу сначала')
        reopen(status, int(input('...')))
if action == 6:
    print('вы успешно вышли из программы')
