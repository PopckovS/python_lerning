'''set - Множества, не индексируемые, неизменяем, но добавлять/удалять эллементы можно.

Словари - состоят из ключей и значений, пишется в фигурных скобках.
Множества в отличии от словарей, имеют только значения, без ключей,
но тоже пишутся в скобках, также они неиндексируемые, тоесть доступ не по индексам.
'''

'''Множества не упорядочены, поэтому элементы будут отображаться в произвольном порядке.'''
set1 = {'set', 'list', 'tuple', 'dictionary'}
print(set1)
# Answer: {'set', 'dictionary', 'tuple', 'list'}


'''Доступ без индекса, доступ либо в цикле, либо згная точное значение'''
print('Вывод эллементов множества в цикле:')
for x in set1:
    print(x)


'''Проверим присутствует ли значение в последовательности'''
serach = 'dictionary'
print("Надится ли в множестве {s} зачение '{d}' Ответ = {r}".format(d=serach, s=set1, r=(serach in set1)))


'''Добавляем эллементы в множество. 
add() - добавляет один эллемент в множество.
update() - добавляет множество эллементов. '''
set1.add('dict')
print(set1)


'''Добавим список в множество'''
set1.update(["class",  "int"])
print(set1)


'''Удаляем эллементы из множества.
remove()  - Если элл-нта не существует то возвращает ошибку.
discard() - Если элл-нта не существует то ошибки вызвано не будет.
работают абсолютно одинаково, кроме возврата ошибки.
Можно удалить при помощи метода pop() но из за того что множества неупорядочены, мы
не знаем какой эллемент будет удален.
'''
set1.remove("class")
print(set1)



'''Полное удаления множества'''
del set1

