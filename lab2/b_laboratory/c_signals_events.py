"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""
import time

from PySide6 import QtWidgets, QtCore, QtGui

from lab2.b_laboratory.ui import c_signals_events_form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = c_signals_events_form.Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()  # Вызвать метод с инициализацией сигналов

    def initSignals(self):
        # self.ui.pushButtonMoveCoords.clicked.connect(self.onPuchButtonMoveWindowClicked)
        self.ui.pushButtonMoveCoords.installEventFilter(self)
    # слоты для подключения

    # слот перемещения окна по заданным координатам
    def onPuchButtonMoveWindowClicked(self):
        x = int(self.ui.spinBoxX.text())
        y = int(self.ui.spinBoxY.text())
        window.move(x, y)

    def eventFilter(self, watched, event):
        if event.type() == QtCore.QEvent.Type.MouseButtonPress:
            self.onPuchButtonMoveWindowClicked()

        return super().eventFilter(watched, event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
