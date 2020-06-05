'''Работа с файлами в Python'''

# Функция open:
# 1 - Путь к файлу, как относительный так и абсолютный
# 2 - Режим в котором идет работа с файлом
#
# --------------------------------------------------------------------------------------
#   r | Открыть и читать из файла, (является значением по умолчанию).
# --------------------------------------------------------------------------------------
#   + | Чтение и запись
# --------------------------------------------------------------------------------------
#   t | Открытие в текстовом режиме, (является значением по умолчанию).
# --------------------------------------------------------------------------------------
#   b | Открытие в двоичном режиме
# --------------------------------------------------------------------------------------
#   a | Открытие на запись, информация добавляется в конец файла
# --------------------------------------------------------------------------------------
#   x | Открытие на запись, если файла нету то ошибка
# --------------------------------------------------------------------------------------
#   w | Откр-е на запись, содержимое файла удаляется, если файла нету то будет создан
# --------------------------------------------------------------------------------------
#  По умолчания работает в режиме 'rt'

# Открываем файл
file_1 = open('text.txt', 'r')

# Читаем информацию из файла, есть 2 способа это сделать.
# Аргумент должен быть числом, и указывает с какой строчки получить информация
print('Вывод данных из файла, методом read:')
print(file_1.read(1))
# Если Аргумента нету вабще, то читает все строки из файла
print(file_1.read())
file_1.close()

# Другой способ чтения из файла,по строчно, при помощи цикла for
print('Вывод данных из файла при помощи цикла for:')
file_2 = open('text.txt', 'r')
for line in file_2:
    print(line, end='')


# Запись в файл:
# Запишем в файл список
x = ['0-1', '10', '21', '32', '43', '54', '65', '76', '87', '98', '109',
 '1110', '1211', '1312', '1413', '1514', '1615', '1716', '1817', '1918']

# Удаляем из файла все что там было до этого, при помощи символа w
# И запишем туда новое содержимое, при помощи символа +
file_2 = open('text.txt', 'w+')

for index in x:
    file_2.write(index + '\n')

print('\nМы записали в файл, теперь прочитаем что туда записали:\n')

for line in file_2:
    print(line, end='')

# Закрываем дескриптор файла,
file_2.close()

