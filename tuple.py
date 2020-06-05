
class tuple_lerning():

    '''Кортеж - упорядоченная неизменяемая последовательность.

    Пишутся как в скобках, так и без, неизменяем, если создан изменить уже нельзя.
    Доступ как и к обычному списку, в работе с циклом ничем не отличается.
    Удалять эллементы по отдельности невозможно, но можно удалить весть кортеж полностью.
    var_tuple = (1, 2, 3, 4, 5) # создание кортежа
    var_tuple_2 = tuple(("помидор",  "огурец",  "лук")) # второй способ создания кортежа
    del var_tuple # полное удаление кортежа
    '''

    # our_tuple = ('hello', 'world', 1, 2, 5)
    our_tuple = 'hello', 'world', 1, 2, 5

    @staticmethod
    def static_get_tuple(x):
        # return self.our_tuple
        return x
        # pass

    def dinamic_for_static(self):
        return self.static_get_tuple(self.our_tuple)

    def dinamic_get_tuple(self):
        return self.our_tuple


obj = tuple_lerning()
print('Получаем сво-во из обьекта на прямую: \n', obj.our_tuple, '\n', type(obj.our_tuple), end='\n=============\n')
print('Получаем сво-во из: \n', obj.our_tuple, '\n', type(obj.our_tuple), end='\n=============\n')

print('Получаем значение кортежа через динамический метод:\n', obj.dinamic_get_tuple(), type(obj.our_tuple), end='\n===========\n')
print('Получаем значение кортежа через статический метод:\n', obj.dinamic_for_static(), '\n', type(obj.dinamic_for_static()), end='\n===========\n')








