'''Примеры №2 Различные примеры кода, сфункция и прочее.
Задачи с сайта - https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/'''
start_block = "==============="

# Task:
# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5
''''''
print(start_block)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print('Число {0} меньше чем 5'.format(i))
# Answer:



# Task:
# Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
''''''
print(start_block)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Циклом в Цикле сравниваем каждыйц эллемент одного массива, скаждым эллементом другова массива.
# тоесть количество шагов будет O(n1 * n2).
def func_first(a, b):
    result = [] # Результирующий массив
    counter_all, counter_yes = 0, 0 # Переменные для счета шагов
    for i in a: # Цикл для 1-го списка
        for j in b: # Цикл для 2-го списка
            counter_all += 1
            if i == j:  # Условие если эллементы равны
                counter_yes += 1
                result.append(i) # Добавляем в результ список новый эллемент

    return [result, counter_all, counter_yes]

result_array, counter_all, counter_yes =  func_first(a, b)
print('Массив = {0} \nКоличество шагов всего {1} * {2} = {3}\nКоличество шагов на результирующий массив = {4}'
      .format(result_array, len(a), len(b), counter_all, counter_yes) )
# Answer:



# Task:
# Отсортируйте словарь по значению в порядке возрастания и убывания.
''''''
print(start_block)

# Функция сортировки словаря, либо по возрастанию либо по убыванию
# в зависимости от второго аргумента
def func_dict_sort(dct, how_sort='ask'):
    import operator

    # Первый аргумент должен быть словарем, для сортировки
    if not isinstance(dct, dict):
        return 'Первый аргумент должен быть словарем'

    # Второй аргумент должен быть одним из разрешенных значений
    if how_sort != 'ask':
        if how_sort != 'desk':
            return 'Второй аргумент должен быть либо "ask" либо "desk"'

    # В зависимости от второго параметра, сортировка по возрастанию, или убыванию
    if how_sort == 'ask':
        result = sorted(dct.items(), key=operator.itemgetter(1))
        print('Сортировка по возрастанию = {0}'.format(dict(result)))
    elif how_sort == 'desk':
        result = sorted(dct.items(), key=operator.itemgetter(1), reverse=True)
        print('Сортировка по в обратном  = {0}'.format(dict(result)))


dct = {'John':35, 'Alex':27, "Ben":42, "Knut":1}

print('Данный пример выполнен с использованием модуля "import operator"')
func_dict_sort(dct, 'ask')
func_dict_sort(dct, 'desk')
# Answer:



# Task:
# Напишите программу для слияния нескольких словарей в один.
''''''
print(start_block)

# Функция принимает неогранич колич аргументов, сливает их в один, и возвращает
# Принимает только словари, или возвращает ошибку
def func_dist_update(*args):
    result = {} # результирующий словарьс

    # Проверка чтобы все аргументы были типа dict
    for element in args:
        if not isinstance(element, dict):
            return 'Каждый переданный аргумент должен быть типа dict'

    # Сливаем все массивы в один
    for element in args:
        result.update(element)

    # Возвращаем результирующий словарь, слитый из аргументов
    return result


dict1 = {'A':1, 'B':2, 'C':3}
dict2 = {'D':4, 'G':5, 'S':6}
dict3 = {'A':10, 'B':20, 'C':30}

print(func_dist_update(dict1, dict2))
print(func_dist_update(dict1, dict2, dict3))
# Answer:



# Task:
# Найдите три ключа с самыми высокими значениями в словаре
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.
''''''
print(start_block)

# Функция принимает словарь, сортирует его и возращает указанное количество эллементов из отсортированного
def func_find_three_max(dict_1, count_max):
    import operator # Импортируем модуль operator - множество функций для сортировки

    result = {}

    # Проверка чтобы аргумент был словарем и только
    if not isinstance(dict_1, dict):
        return 'Аргумент должен быть типом dict'
    # Проверка чтобы второй аргумент был числов
    if not isinstance(count_max, int):
        return 'Второй аргумент должен быть числом'

    # Сортируем словарь при помощи модуля operator
    result = sorted(dict_1.items(), key=operator.itemgetter(1),  reverse=True)

    return result[0:count_max]

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
print(func_find_three_max(my_dict, 3))
# Answer:



# Task:
# Напишите код, который переводит целое число в строку,
# при том что его можно применить в любой системе счисления
''''''
print(start_block)
# Answer:



# Task:
# Напишите проверку на то, является ли строка палиндромом.Палиндром — это слово или
# фраза, которые одинаково читаются слева направо и справа налево.
''''''
print(start_block)

# Переворачиваем строчку и сравниваем ее с оригиналом
def func_polindrom(string):
    # Проверка явл ли аргумент строкой
    if not isinstance(string, str):
        return 'Аргумент должен быть строкой'

    # if string == ''.join(reversed(string)): # Правильный вариант
    if string == string[::-1]: # Тоже правильный вариант
        return 'Строка "{0}" это полиндром'.format(string)
    else:
        return 'Строка "{0}" не полиндром'.format(string)


print(func_polindrom('qwerty'))
print(func_polindrom('abcddcba'))
print(func_polindrom('abcdfdcba'))
# Answer:
# for elem in reversed('TURBO'):
#     print(elem)
# ''.join(reversed(string)) ПОЧЕМУ ТАК ? reversed(string)




# Task:
# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды
print(start_block)

def convert_1(seconds):
    days = seconds // (24 * 3600)
    seconds = seconds % (24 * 3600)
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    print(f'{days}:{hours}:{minutes}:{seconds}')

def convert_2(value):
    day     = round(value/86400) # Делю секунды/количюсек в дне
    hours   = int((value % 86400) / 3600) # Получаю остаток от деления на 24 часа и делю на колич сек в часе
    minutes = round(((value % 86400) % 3600) / 60) # Остаток от часов делю на колич секунд в минуте
    seconds = round(((value % 86400) % 3600) % 60) # Остаток секунд

    print('Дни = {0}: Часы = {1}: Минуты = {2}: Секунды = {3}'.format(day, hours, minutes, seconds))

print('Первая версия')
convert_2(90063)
convert_2(1234565)

print('Вторая версия')
convert_1(90063)
convert_1(1234565)
# Answer:
# Почему так ?
# print(f'{days}:{hours}:{minutes}:{seconds}')




# Task:
# Вы принимаете от пользователя последовательность чисел, разделённых запятой.
# Составьте список и кортеж с этими числами.
print(start_block)

def func_give():
    values = input('Введите числа через запятую: ')
    ints_as_strings = values.split(',')
    ints = map(int, ints_as_strings)

    print(values)
    print(ints_as_strings)
    print(ints)

    lst = list(ints)
    tup = tuple(lst)

    print('Результат:')
    print('Список:', lst)
    print('Кортеж:', tup)

# func_give()
# Answer:




# Task:
# Выведите первый и последний элемент списка.
print(start_block)

def func_first_last(array):

    if isinstance(array, list):
        print('Первый эллемент списка = ', array[0])
        print('Послений эллемент списка =', array[-1])

x = [1,2,3,4,5]
func_first_last(x)
# Answer:




# Task:
# При заданном целом числе n посчитайте n + nn + nnn.
print(start_block)

# Функция принимает 2 аргумента
# 1 - целое число
# 2 - количество повторений
def counter_of_n(n, counter):
    if isinstance(n, int): # Если первый аргумент это целое число
        if isinstance(counter, int) and counter > 0: # Второе должно быть целым числом и больше чем ноль
            result = 0 # Результирующая переменная
            x = n      # Содержит резуьтат превыд вычисление
            while counter > 0: # До тех пор пока количество повторений больше чем ноль
                counter -= 1   # Уменьшаем колич повторений до нуля
                result  += x   # Результат равен превыдущему вычеслению, для начала это только 1 первый аргумент
                x += n         # Превыд.выч с каждым шагом увеличивается на 1 единственный первый аргумент
            print('Результата = {0}'.format(result)) # Вывод результата
        else:
            print('Второй аргумент должен быть целым числом, и больше чем 0 ')
    else:
        print('Первый аргумент должен быть целым числом')

counter_of_n(1, 3)
counter_of_n(2, 3)
counter_of_n(3, 3)
# Answer:




# Task:
# Напишите программу, которая выводит чётные числа из заданного списка и останавливается,
# если встречает число 237.
print(start_block)

def fenc_even(array, stop):

    if isinstance(array, list):
        if isinstance(stop, int):

            # Цикл вывода
            for element in array:
                # Если это наше стоп число то остановка цикла и вывод
                if element == stop:
                    print('Ваше стоп число = {0} вы на него попали, конец цикла'.format(stop))
                    break
                # Если число делится на 2 без остатка то вывод его
                if (element % 2) == 0:
                    print('Четный эллемент = ', element)

        else:
            print('Второй аргумент должен быть целым числом')
    else:
        print('Первый аргумент должен быть списком')


x = [1,2,3,4,5,6,7,8,9,10,34,35,237,1,2,3,4,5,6,7,8,9,10]
fenc_even(x, 237)
# Answer:




# Task:
# Напишите программу, которая принимает два списка и выводит все элементы первого,
# которых нет во втором.
print(start_block)

def func_search_in_list(first, second):
    if not isinstance(first, list) or not isinstance(second, list):
        return print('Оба аргумента должны быть списками.')
    else:
        result = []
        # Сверяю есть ли во втором списке эллемент из первого списка,
        # если нету то заношу его в результат
        for i in first:
            if not i in second:
                result.append(i)
        return print(result)


def func_search_in_list_two(first, second):
    set_1 = set(first)
    set_2 = set(second)
    return print(set_1 - set_2)

# Списки для работы
first  = [1,1,2,3,4,5,6,7,8,9,0]
second = [1,1,4,6,8,0]
set_1 = ['White', 'Black', 'Red']
set_2 = ['Red', 'Green']

print('--- Первый метод ---')
func_search_in_list(first, second)
func_search_in_list(set_1, set_2)
print('--- Второй метод ---')
func_search_in_list_two(first, second)
func_search_in_list_two(set_1, set_2)
# Answer:




# Task:
# Сложите цифры целого числа
print(start_block)

# Функция принимает целое число и только, число разбивается на эллементы
# эллементы складываются в целое число
def plus_int_first(x):
    # Проверка чтобы аргумент был числом
    if not isinstance(x, int):
        return print('Аргумент должен быть целым числом.')
    else:
        # Инициализация переменных:
        # result - результирующая сумма.
        # elements - строка с описанием эллементов из кот-х складывается число
        # string_int - аргумет.число превращается в строчку, чтобы ее можно было разделять на эллементы
        # max - максимальное количество эллементов из строки, которое надо будет сложить
        result, elements, string_int, max = 0, '', str(x), len(str(x))

        # Цикл складывания эллементов в число
        for i in string_int:
            max -= 1 # С каждым шагом уменьшаю максим колич к нулю
            if max != 0: # Если еще есть шаги в цикле то добавляем  строчку плюса
                elements += i + ' + '
            else: # Если это последний эллемент то просто добавляю число, без строчки плюс
                elements += i
            result += int(i) # Складываю все эллементы в результирующий

        return print('Результат сложения эллементов из числа {0} : {1} = {2}'.format(x, elements, result))


def plus_int_second(num):
    # Проверка чтобы аргумент был числом
    if not isinstance(num, int):
        return print('Аргумент должен быть целым числом.')
    else:
        # Цикл for проходит по каждому эллементу строки и возвращает его переведенным в число
        # Все возвращенные числа становятся списком чисел, кторые потом складываются
        digits = [int(d) for d in str(num)]
        # Используем метод summ который складывает все эллементы спска в одно число
        return print(sum(digits))


plus_int_first(12345)
plus_int_second(12345)
# Answer:




# Task:
# Посчитайте, сколько раз символ встречается в строке.
print(start_block)

# Метод считает количество определенных эллементов в строчке
def counter_string(string, char):
    if not isinstance(string, str) or not isinstance(char, str):
        return print('Аргументы должены быть строчками')
    else:
        counter = 0
        for i in string:
            if i == char:
                counter += 1
        return print('Количество повторений символа "{0}" в строке "{1}" = {2}'.format(char, string, counter))

search = 's'
counter_string('string g s', search)

# Тип данных str имеет специальный метод .count() который может посчитать
# Сколько раз символ встречается в строчке
string = 'Python Software Foundation'
print(type(string))
print(string.count('o'))
# Answer:




# Task:
# С помощью анонимной функции извлеките из списка числа, делимые на 15
print(start_block)

nums = [45, 55, 60, 37, 100, 105, 220]
result = list(filter(lambda x: not x % 15, nums))
print(result)
# Answer:
# Функция filter - ?



# Task:
''''''
print(start_block)
# Answer:




# Task:
''''''
print(start_block)
# Answer: