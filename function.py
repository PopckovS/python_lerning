'''Функции в Python'''
start_block = '==================='


# ========================================================
'''Функция в Python создается с помощью ключевого слова def'''
print(start_block)

def func_1():
    print('Hello World')

func_1() # Вызов функции


# ========================================================
'''Параметры функции'''
print(start_block)

def func_2(fname):
    print('Hello ' + fname)

func_2('World')


# ========================================================
'''Значение параметра по умолчанию'''
print(start_block)

def func_3(country="Англии"):
    print('Старана '+ country)

func_3('Америка')
func_3()
func_3('Германия')


# ========================================================
'''Возвращение значения'''
print(start_block)
def func_4(x):
    return 5 * x

print(func_4(2))
print(func_4(3))
print(func_4(4))
# Answer:


# ========================================================
''''''
print(start_block)
print()
# Answer:




