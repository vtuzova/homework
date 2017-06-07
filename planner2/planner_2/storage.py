import sqlite3
import os.path as Path



# запрос на получение данных всех
SQL_SELECT_ALL = '''
    SELECT
        id, task_name, task_text, task_status
    FROM
        plan
'''

# запрос на получение данных по ключу. добавляем условие через WHERE к старому запросу
SQL_SELECT_BY_ID = '''
    SELECT
        id, task_name, task_text, task_status
    FROM
        plan
    WHERE id=?
'''


# добавление задачи
SQL_NEW_TASK = '''
    INSERT INTO plan (task_name, task_text, task_status) 
    VALUES('{}', '{}', '{}')
    
'''

# редактирование задачи
SQL_REDACTION = '''
    UPDATE plan 
    SET task_name = ?, task_text = ?, task_status = ?
    WHERE ID = ?
'''

# завершение задачи
SQL_CLOSING = '''
    UPDATE plan 
    SET task_status = 'выполнено'
    WHERE ID = ?
'''

# начать задачу сначала
SQL_RESTART = '''
    UPDATE plan 
    SET task_status = 'не выполнено'
    WHERE ID = ?
'''



def dict_factory(cursor, row):
    d = {}
    #print ('row: ', row)
    #print ('col: ', cursor.description)
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row [idx]
    return d


# установка соединения, инициализация
def connect (db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name) # установка соединения
    conn.row_factory = dict_factory

    return conn


def initialize(conn):
    with conn:
        script_file_path = Path.join(Path.dirname(__file__), 'plan.sql')
        print(script_file_path)

        with open(script_file_path) as f:
            conn.executescript(f.read())            


def find_all(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()

def check_row_exists(conn, id):
    with conn:
        cursor = conn.execute(SQL_SELECT_BY_ID, (id,))
        obj = cursor.fetchall()
        if len(obj) == 0:
            return False
        else:
            return True







    

