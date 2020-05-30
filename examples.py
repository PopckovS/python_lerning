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





'''Перевернуть строчку'''
print(start_block)

x = 'Hello World'
max_len = len(x)

print(x)
print(max_len)

# ===============================================
print("Обычный вывод:")
for i in range(0, max_len):
    print(x[i])

# ===============================================
print("Вывод в обратном порядке:")
i = -1
while i >= -max_len:
    print('Число i = {0} значение = {1}'.format(i, x[i]))
    i -= 1


# Answer:



# ===============================================
'''Перевернуть строчку рекурсией №1'''
print('{0} Перевернуть строчку рекурсией №1 {0}'.format('==========='))

x = 'Hello World'
max_len = len(x)

def revers_string(str, char):
    try:
        print(str[char])
    except:
        return
    else:
        revers_string(x, char - 1)

revers_string(x, -1) # Запустить функцию
# Answer:



# ===============================================
'''Перевернуть строчку рекурсией №2'''
x = 'Hello World'
max_len = len(x)

def revers_string(str, flag='standart', char=0):
        try: # Вывод символа из строки
            print(str[char])
        except: # Закончить вывод
            return
        else:
            if flag == 'standart': # Обычный вывод
                revers_string(x, 'standart', char + 1)
            elif flag == 'revers': # выводв в обратном порядке
                revers_string(x, 'revers', char - 1)


print('{0} Перевернуть строчку рекурсией №2 {0}'.format('==========='))
revers_string(x, 'standart', 0) # Запустить функцию

print('{0} Перевернуть строчку рекурсией №3 {0}'.format('==========='))
revers_string(x, 'revers', -1) # Запустить функцию




# ===============================================
'''Вывод елочки'''
print("{0} Вывод елочки {0}".format('=========='))

def tree_function(max):
    number = 1
    fuss = 1
    start = 0
    while number <= max:
        print(number, end=' ')
        number += 1
        start  += 1
        if start == fuss:
            fuss += 1
            start = 0
            print('\n', end='')
    print('\n')

tree_function(57)
# Answer:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31 32 33 34 35 36
# 37 38 39 40 41 42 43 44 45
# 46 47 48 49 50 51 52 53 54 55
# 56 57


# ===============================================
'''Вывод елочки с переломом'''
print("{0} Вывод елочки с переломом {0}".format('=========='))

def tree_function_revers(max, switch=5):
    number = 1 # Число которое будет выводится до нашего максимального числа
    fuss   = 1 # Позиция на которой будет переброс строки
    start  = 0 # Позиция числа до fuss увеличивается до него и как только становится ему равно, сбрасывается до 0
    limit  = 1 # Это флаг указывает, на увелич или уменьш идет алгоритм, 1 это увеличение. -1 это уменьшение

    while number <= max: # Начало цикла, сполнение пока не будет выведены все числа

        if switch == fuss: # Если позиция переключения == текущей, то переключ алгоритм на сниженеи
            limit = -1
        elif fuss == 1: # Если позиция переноса строки == 1, то переключ алгоритм на увеличение
            limit =  1

        print(number, end=' ') # Вывод текущего числа
        number += 1 # Вывод текущего числа
        start += 1  # Позиция до переноса строки увеличивается
        if start == fuss:  # Если позиция (ДоПереноса == Переноса)
            start = 0  # Сбросить позицию до переноса
            print('\n', end='') # Перенести строчку
            if limit == 1: # Если флаг Увелич/Уменьш == 1 то увеличить Переноса строки на +1
                fuss += 1
            elif limit == -1: # Если флаг УвеличУменьш == -1 то уменьшить Перенос строки на -1
                fuss -= 1


    print('\n')

tree_function_revers(63, 4)



# ===============================================
'''Вывод елочки с переломом и возрастающей амплитудой'''
print("{0} Вывод елочки с переломом и возрастающей амплитудой {0}".format('=========='))

def tree_function_revers(max, switch=5):
    number, fuss, limit, start = 1, 1, 1, 0

    while number <= max:
        if switch == fuss:
            switch+= 1 # Вот этот кусочек, с каждым циклом мы увелич след амплитуду на +1
            limit = -1
        elif fuss == 1:
            limit =  1

        print(number, end=' ')
        number += 1
        start += 1

        if start == fuss:
            start = 0
            print('\n', end='')
            if limit == 1:
                fuss += 1
            elif limit == -1:
                fuss -= 1
    print('\n')

tree_function_revers(130, 4)



# ===============================================
''''''
print(start_block)
# Answer:



# ===============================================
''''''
print(start_block)
# Answer: