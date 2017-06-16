1. функциональный подход
import os

сначала пишем функцию для определения типа файла
тип файла находим по расширению (обрезаем имя файла по точке)

def extention(filename):
        test = os.path(filename)
        ext = test.split('.')
        return ext

потом пишем две функции - на чтение и запись, где, в зависимости от расширения,
будет использоваться нужный метод

def read_file(filename):
        if ext=txt:
            with open (filename, 'w') as f:
                f.read('.....')
        elif ext=pickle:
            with open (filename, 'wb') as f:
                pickle.load('.....')
        elif ext=json:
            ...
            ...
            

def write_file(filename):
        if ext=txt:
            with open (filename, 'w') as f:
                f.write('.....')
        elif ext=pickle:
            with open (filename, 'wb') as f:
                pickle.dumb('.....')
        elif ext=json:
            ...
            ...

2. ооп подход
создаем для каждого типа данных отдельный класс, в котором прописаны методы работы с ним
при добавлении нового типа файлов в нашей базе, нужно будет прописать новый класс для работы с ним

WorkWithTXT
 внутри функции для открытия и тп
WorkWithJson
...

класс в котором мы держим возможные расширения
class Extention(object):
    def __init__(filename):
        test = os.path(filename)
        ext = test.split('.')
        return ext

далее - общий класс, наслудует знания о расширении от класса Extention 
class WorkFile(Extention):
    def __init__(filename, ext):
        super().__init__(ext)
    def open_file(filename, ext):
        if ext=txt:
            WorkWithTXT.open(filename)
        ...
    def write_file(filename, ext):
        is ext=...



    

    
    


            
