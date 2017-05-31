import sqlite3
import os.path as Path
conn = sqlite3.connect('plan.db')

c = conn.cursor()

sql = '''
    CREATE TABLE IF NOT EXISTS plan (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT NOT NULL DEFAULT '',
        task_text TEXT NOT NULL DEFAULT '',
        task_status TEXT NOT NULL DEFAULT ''     
    )
'''

c.execute(sql)

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

# запрос на получение данных всех
SQL_SELECT_ALL = '''
    SELECT
        id, task_name, task_text, task_status
    FROM
        plan
'''

#получение по id
SQL_SELECT_BY_ID = '''
    SELECT
        id, task_name, task_text, task_status
    FROM
        plan
    WHERE id = %s
'''

# добавление задачи
SQL_NEW_TASK = '''
    INSERT INTO plan (task_name, task_text, task_status)
    VALUES('%s', '%s', '%s')
    
'''

# редактирование задачи
SQL_REDACTION = '''
    UPDATE plan 
    SET task_name = '%s', task_text = '%s', task_status = '%s'
    WHERE ID = %s
'''

# завершение задачи
SQL_CLOSING = '''
    UPDATE plan 
    SET task_status = 'выполнено'
    WHERE ID = %s
'''

# начать задачу сначала
SQL_RESTART = '''
    UPDATE plan 
    SET task_status = 'не выполнено'
    WHERE ID = %s
'''


def find_all(conn):
    with conn:
        c = conn.execute(SQL_SELECT_ALL)
        return c.fetchall()

def add_task(conn, task_name, task_text, task_status):
    with conn:
        c = conn.execute(SQL_NEW_TASK % (task_name, task_text, task_status))

def redact_task(conn, id, task_name, task_text, task_status):
    with conn:
        c = conn.execute(SQL_REDACTION % (task_name, task_text, task_status, id))

def close_task(conn, id):
    with conn:
        c = conn.execute(SQL_CLOSING % id)
        
def restart_task(conn, id):
    with conn:
        c = conn.execute(SQL_RESTART % id)                         

def check_row_exists(conn, id):
    with conn:
        c = conn.execute(SQL_SELECT_BY_ID % id)
        obj = c.fetchall()
        if len(obj) == 0:
            return False
        else:
            return True

# цикл проверки введенного значения
while action is not 6:
    action_string = input('введите число...')
    if not action_string.isdigit():
        print('ошибка')
        break
    action = int(action_string)
    if action > 6 or action <= 0:
        print('ошибка')
        break
    elif action == 1: #вывод списка
        r = find_all(conn)
        print(r)
        
    elif action == 2:
        print('добавление задачи:')
        task_name = input('введите имя')
        task_text = input('введите описание')
        task_status = input('статус задачи')
        add_task(conn, task_name, task_text, task_status)
        print('задача добавлена')
        
    elif action == 3:
        print('редактирование задачи:')
        id = input('введите номер редактируемой задачи')
        if not id.isdigit():
            print('id должен быть числом')
            break
        if not check_row_exists(conn, id):
            print('id не существует')
            break
        task_name = input('введите имя')
        task_text = input('введите описание')
        task_status = input('статус задачи')
        redact_task(conn, id, task_name, task_text, task_status)
        
    elif action == 4:
        print('завершить задачу')
        id = input('введите номер задачи')
        if not id.isdigit():
            print('id должен быть числом')
            break
        if not check_row_exists(conn, id):
            print('id не существует')
            break
        close_task(conn, id)
        
    elif action == 5:
        print('начать задачу сначала')
        id = input('введите номер задачи')
        if not id.isdigit():
            print('id должен быть числом')
            break
        if not check_row_exists(conn, id):
            print('id не существует')
            break
        restart_task(conn, id)
        
if action == 6:
    print('вы успешно вышли из программы')

    

