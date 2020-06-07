#! /usr/bin/python3

# from form import Ui_MainWindow  # Импорт главной сгенерированной формы
# from secondForm import Ui_Form      # Импорт вторичной формы
# from ModelBase import ModelBase
# import pymysql

from PyQt5 import QtWidgets, QtGui, QtCore
import sys

# Вывод версии текущей PQ5
# print(QtCore.PYQT_VERSION_STR)

# Запуск приложения
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Первая программа на PyQt")
window.resize(300, 70)
label = QtWidgets.QLabel("<center>Hello world!</center>")
btnQduit = QtWidgets.QPushButton("Закрыть окно")

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQduit)
window.setLayout(vbox)
btnQduit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec())














