# прописываем список функций, на которые программа будет ссылаться в зависимости от введенного пользователем числа

def redaction(task, a):
    task[a-1] = (input('...'))
def closing(status, b):
    status[b-1] = 'выполненo'
def reopen(status, c):
    status[c-1] = 'не выполнено'
def new_task(task, status, d):
    task.append(input('...'))
    status.append('не выполнено')
