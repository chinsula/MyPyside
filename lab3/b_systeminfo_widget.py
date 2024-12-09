"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
import traceback

import psutil
from PySide6 import QtWidgets, QtCore

from a_threads import SystemInfo


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.__initSignals()
        self.systemInfo = SystemInfo()

    def initUi(self):
        """
        Инициализация Ui
        :return: None
        """
        self.inputDelay = QtWidgets.QLineEdit()
        self.inputDelay.setPlaceholderText("Введите время задержки")

        self.labelCPU = QtWidgets.QLabel("CPU usage: ")
        self.labelCPU.setText(f"CPU usage: {psutil.cpu_percent()} %")
        self.labelRAM = QtWidgets.QLabel("RAM usage: ")
        self.labelRAM.setText(f"RAM usage: {psutil.virtual_memory().percent} %")

        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(self.inputDelay)
        layout.addWidget(self.labelCPU)
        layout.addWidget(self.labelRAM)

        self.setLayout(layout)
        self.setMinimumSize(100, 100)

    def __initSignals(self):

        self.inputDelay.textChanged.connect(self.onChangeInputDelay)
        self.thread = SystemInfo()
        # self.thread.setDelay(int(self.inputDelay.text()))
        self.thread.started.connect(lambda: print("Поток запущен"))
        self.thread.finished.connect(lambda: print("Поток остановлен"))
        self.thread.start()

    def onChangeInputDelay(self):
        self.thread.setDelay(int(1 if not self.inputDelay.text() else self.inputDelay.text()))
        print(self.thread.delay)




if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec()