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
''''''
print(start_block)
# Answer:


# Task:
''''''
print(start_block)
# Answer:


# Task:
''''''
print(start_block)
# Answer:
