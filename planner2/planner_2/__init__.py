import sys

from planner_2 import storage
from planner_2.storage import SQL_NEW_TASK

get_connection = lambda: storage.connect('plan.sqlite')


    
# в данном файле будут храниться обработчики
def action_show_list():
    with get_connection() as conn:
        r = storage.find_all(conn)
        print (r)

def action_add_task():
    with get_connection() as conn:
        ok = False

        while not ok:
            task_name = input('введите имя')
            task_text = input('введите описание')
            task_status = input('статус задачи')


            if task_name == '' or task_text == '' or task_status == '':
                print('!!!!!')
                break # если пользователь не заполнил поле, выходим
            else:            
                cursor = conn.execute(SQL_NEW_TASK.format(task_name, task_text, task_status))
                ok = True
        

def action_redact_task():
    with get_connection() as conn:
        ok = False
    
    
        while not ok:
            print('редактирование задачи:')
            id = input('введите номер редактируемой задачи')
            if not id.isdigit():
                print('id должен быть числом')
                break

            if not storage.check_row_exists(conn, id):
                print('id не существует')
                break
        
            task_name = input('введите имя')
            task_text = input('введите описание')
            task_status = input('статус задачи')

            cursor = conn.execute(storage.SQL_REDACTION, (task_name, task_text, task_status, id))
            ok = True
        
def action_close_task():
    with get_connection() as conn:
        ok = False
        print('завершить задачу')
    

        while not ok:
            id = input('введите номер задачи')
            if not id.isdigit():
                print('id должен быть числом')
                break
            if not storage.check_row_exists(conn, id):
                print('id не существует')
                break
            cursor = conn.execute(storage.SQL_CLOSING, (id,))
            ok = True
        
def action_restart_task():
    with get_connection() as conn:
        ok = False
    
        print('начать задачу сначала')

        while not ok:
            id = input('введите номер задачи')
            if not id.isdigit():
                print('id должен быть числом')
                break
            if not storage.check_row_exists(conn, id):
                print('id не существует')
                break
            cursor = conn.execute(storage.SQL_RESTART, (id,))
            ok = True




def action_show_menu():
    '''обработчик действия показать меню'''
    print('''
URL Ежедневник v1.0

1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
6. Выход''')


def action_exit():
    '''обработчик действия выйти'''
    sys.exit(0)

def main():
    #функция, запускающая приложение
    
    with get_connection() as conn:
        storage.initialize(conn)

    action_show_menu()

    actions = {
        '1': action_show_list,
        '2': action_add_task,
        '3': action_redact_task,
        '4': action_close_task,
        '5': action_restart_task,
        '6': action_exit
        }

    while 1:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('не известная команда')












        
        







        
    
