from abc import ABCMeta, abstractmethod
import os
import json
import pickle
import sys


source = './params.pickle'

class ParamHandlerException(Exception):
    pass

        
class ParamHandler(metaclass=ABCMeta):
    types = {
    
        }
    

    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def get_all_params(self):
        return self.params

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass
    
    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')
        if not issubclass(klass, ParamHandler):
            print('Class "{}" is not ParamHandler!'.format(klass))
            raise ParamHandlerException

        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):
     # Шаблон "Factory Method"
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)
        print('-------------', klass)
        print(cls.types.get(ext))
        print('!!!!!!!!', ext)

    
        if klass is None:
            print ('Type "{}" not found!'.format(ext))
            raise ParamHandlerException
                                        
        return klass(source, *args, **kwargs)


        
class TextParamHandler(ParamHandler):
    def read(self):
        with open(source, 'r') as f:
            f.read()

    def write(self):
        with open(source, 'w') as f:
            for key, value in self.params.items():
                f.write(str(key)+ ":" + str(value) + '\n')
            


class PickleParamHandler(ParamHandler):
    def read(self):
        with open (source, 'rb') as f:
                self.params = pickle.load(f)
                return self.params 
    def write(self):
        with open (source, 'wb') as f:
            pickle.dump(self.params, f)

                
class JsonParamHandler(ParamHandler):
    def read(self):
        with open (source, 'r') as f:
            self.params = json.load(f)
    def write(self):
        with open (source, 'w') as f:
            json.dump(self.params, f)
        


ParamHandler.add_type('json', JsonParamHandler)
ParamHandler.add_type('pickle', PickleParamHandler)
ParamHandler.add_type('txt', TextParamHandler)

config = ParamHandler.get_instance(source)

config.add_param('key1', 'val1')
config.add_param('key2', 'val2')
config.add_param('key3', 'val3')
config.write() # запись файла 


config = ParamHandler.get_instance(source)
config.read() # читаем данные 
