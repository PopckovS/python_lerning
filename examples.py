import math
import random

'''Различные примеры кода, сфункция и прочего...'''
start_block = "======================================================"


'''Задача на условие'''
print(start_block)
x, y, z = True, False, False

if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(1)
# Answer:3



'''Комплексное число, всегда с j - это мнимая часть'''
print(start_block)
x = 5j
print(x)
print(type(x))
# Answer:5j
# Answer:<class 'complex'>



'''divmod - эта функция явл аналогом, (x || y, x % y) тоесто, выводит
полное число делений, и остаток.'''
print(start_block)
x = divmod(10, 5)
y = divmod(11, 5)
print(x)
print(y)
# Answer:(2, 0)
# Answer:(2, 1)



'''Также нужно отметить, что целые числа в python 3,
 в отличие от многих других языков, поддерживают длинную арифметику (однако, это требует больше памяти).'''
print(start_block)
print(3 ** 150)
# Answer:369988485035126972924700782451696644186473100389722973815184405301748249



'''
    int([object], [основание системы счисления]) - преобразование к целому числу в десятичной системе счисления. 
    По умолчанию система счисления десятичная, но можно задать любое основание от 2 до 36 включительно.
    bin(x) - преобразование целого числа в двоичную строку.
    hex(х) - преобразование целого числа в шестнадцатеричную строку.
    oct(х) - преобразование целого числа в восьмеричную строку.
'''
# Строка преобразуется в число при помощи ыункции int()
def transfer_to_int(number, header_name):
    print('============ {0} ============'.format(header_name))
    try:
        resalt = int(number)
    except:
        print('вами введена переменная = {0} \n и она имеет тип {1} \n тут и возникла ошибка'.format(number, type(number)))
    else:
        print(type(resalt))
        print(resalt)

transfer_to_int('19', 'Преобразуем строку в число int')
transfer_to_int('19.5', 'Преобразуем строку(с точкой) в число int, и получаем ошибку, отловим при помощи исключений')
# Answer:



'''import math - Модуль math предоставляет более сложные математические функции.
 import random - Модуль random реализует генератор случайных чисел и функции случайного выбора.'''
print(start_block)

print(math.pi) # вывод числа Pi
print(math.sqrt(9)) # вывод корня числа
print(random.random()) # вывод случайного числа
# Answer:
#   3.141592653589793
#   3.0
#   0.7656628974416873




'''Комплексные числа (complex)
Высший уровень среди чисел, где j**2 = -1
Имеет 2 части, действительная(1) и мнимая(2j)
Сложение 2-х комп.чисел это сложение его частей
Выражение может иметь только мнимую часть(чистомнимое выражение)
'''
print(start_block)

x = complex(1, 2)
print(type(x))
print(x)
print('Реальная часть = {0}'.format(x.real))
print('Мнимая часть = {0}'.format(x.imag))
# Answer:
#   <class 'complex'>
#   (1+2j)
#   Реальная часть = 1.0
#   Мнимая часть = 2.0





''''''
print(start_block)

# Answer:




''''''
print(start_block)

# Answer:




''''''
print(start_block)

# Answer: