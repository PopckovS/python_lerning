#! /usr/bin/python3

import json

'''Модуль JSON - Python имеет встроенный модуль для работы с форматом json'''
strat_block = '========'

'''Конвертация из JSON в Python. Если у вас есть строка JSON, вы можете провести над ней парсинг с помощью метода json.loads ().
Как результат, будет словарь python.'''

x = '{"name":"Vanila Ace", "age":"32", "city":"Egipeth"}'
resalt = json.load(x)
print(type(resalt))
print(resalt)
