
import os

class A():
    '''Это аннотация к классу A ее можно вызвать
    используя специальный метод __doc__'''

    def private(self):
        print('private')

    def _private(self):
        print('_private')

    def __private(self):
        print('_private')

a_1 = A()

# Вывыод названия класса, и как он был вызван
# Если он вызван тамже где и обьявлен то  = <class '__main__.A'>
# Если класс импортирован то выглядит так =
print(a_1.__class__)

# Вызов метода который выведет описание к классу
print(a_1.__doc__)

a_1.private()
a_1._private()
# a_1.__private()

