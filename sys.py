import sys
import os
'''Модуль sys обеспечивает доступ к некоторым переменным и функциям,
 взаимодействующим с интерпретатором python.'''
print('Модуль sys')

x = sys.argv
print(x)
print(type(x))
print('==========')


x = sys.builtin_module_names
print(x)
print(type(x))
print('==========')



x = sys.exec_prefix
print(x)
print(type(x))
print('==========')


x = sys.executable
print(x)
print(type(x))
print('==========')

# x =
# print(x)
# print(type(x))
# print('==========')


'''Модуль os предоставляет множество функций для работы с операционной системой,
 причём их поведение, как правило, не зависит от ОС'''
print('Модуль os', end='\n\n')


x = os.name
print('Имя операц системы')
print(x)
print(type(x))
print('==========')


x = os.environ
print('Переманные окружения')
print(x)
print(type(x))
print('==========')



x = os.getlogin()
print('Имя пользователя вошедшего в терминал')
print(x)
print(type(x))
print('==========')


x = os.getpid()
print('текущий id процесса.')
print(x)
print(type(x))
print('==========')


x = os.uname()
print('Информация об ОС. возвращает объект с атрибутами')
print(x)
print(type(x))
print('==========')


x = os.getcwd()
print('Текущая рабочая директория.')
print(x)
print(type(x))
print('==========')
