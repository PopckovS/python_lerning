#! /usr/bin/python3
import functools
'''
Модуль functools - сборник функций высокого уровня: 
 - взаимодействующих с другими функциями.
 - возвращающие другие функции.
 
https://coderoad.ru - сайт с хорошими примерами кода для Python
https://pythonworld.ru/moduli/modul-functools.html - примеры работы этого кеша
https://www.youtube.com/watch?v=h_B3O5jWMi4 - Видео с обьяснением того как это работает
https://codeby.net/threads/python-dlja-xakera-chast-1-nachalo.61287/
'''

@functools.lru_cache(maxsize=None)
def f(x):
    y += x
    return y


print(f(7))

# Пример кэшированной функции:
# @functools.lru_cache(maxsize=None)
# def f(x, y):
#     return x+y
#
# print(f(7, 4))

# Очистить весь кэш:
# f.cache_clear()

# def clear_cache_value(cached_function, *args, **kwargs):
#     cache = next(c.cell_contents for c in cached_function.cache_info.__closure__ if isinstance(c.cell_contents, dict))
#     del cache[functools._make_key(args, kwargs, False)]
#
# clear_cache_value(f, 7, 4)