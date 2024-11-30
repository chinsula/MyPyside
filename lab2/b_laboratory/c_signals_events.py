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

from PySide6 import QtWidgets, QtCore

from lab2.b_laboratory.ui import c_signals_events_form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = c_signals_events_form.Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()  # Вызвать метод с инициализацией сигналов
        self.installEventFilter(self)

    def eventFilter(self, watched, event):
        # начальное положение (координаты) окна
        if event.type() == QtCore.QEvent.Type.NonClientAreaMouseButtonPress:
            x = window.geometry().x()
            y = window.geometry().y()
            print(f"{time.ctime()} начальное положение окна {x} пикселей на {y} пикселей")  # конечное положение (координаты) окна
        if event.type() == QtCore.QEvent.Type.NonClientAreaMouseButtonRelease:
            x = window.geometry().x()
            y = window.geometry().y()
            print(f"{time.ctime()} конечное положение окна {x} пикселей на {y} пикселей")

        # При изменении размера окна выводить его новый размер
        if event.type() == (QtCore.QEvent.Type.Resize and QtCore.QEvent.Type.NonClientAreaMouseButtonPress):
            w, h = window.size().toTuple()

            print(f"Новый размер окна: {w} пикселей на {h} пикселей")

        return super().eventFilter(watched, event)

    def initSignals(self):
        self.ui.pushButtonMoveCoords.clicked.connect(self.onPuchButtonMoveWindowClicked)
        # self.ui.pushButtonMoveCoords.installEventFilter(self)
        self.ui.pushButtonGetData.clicked.connect(self.onPuchButtonGetLogClicked)

    # слоты для подключения

    # слот перемещения окна по заданным координатам
    def onPuchButtonMoveWindowClicked(self):
        x = int(self.ui.spinBoxX.text())
        y = int(self.ui.spinBoxY.text())
        window.move(x, y)

    # слот для получения лога
    def onPuchButtonGetLogClicked(self):
        # получение разрешения экрана
        width, height = app.primaryScreen().size().toTuple()
        # получение активного окна
        title = window.windowTitle()
        # получение каком экране окно находится
        screen = window.screen().name()[-1:]
        # получение размера окна
        w, h = window.size().toTuple()
        # Минимальные размеры окна
        w1, h1 = window.minimumSize().toTuple()
        # Текущее положение (координаты) окна
        w2 = window.geometry().x()
        h2 = window.geometry().y()
        # Координаты центра приложения
        w3, h3 = window.geometry().center().toTuple()
        # Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
        collaps_window = "развернуто" if window.isVisible() else "свернуто"
        activ_window = "активно" if window.isActiveWindow() else "отображено"

        self.ui.plainTextEdit.setPlainText(f"Время: {time.ctime()}\n"
                                           f"Количество экранов: {len(app.screens())}\n"
                                           f"Текущее основное окно: {title}\n"
                                           f"Разрешение основного экрана: {width} пикселей на {height} пикселей\n"
                                           f"Окно находиться на экране: {screen}\n"
                                           f"Размер окна: {w} пикселей на {h} пикселей\n"
                                           f"Минимальный размер окна: {w1} пикселей на {h1} пикселей\n"
                                           f"Текущее положение (координаты) окна: {w2} пикселей на {h2} "
                                           f"пикселей\n"
                                           f"Координаты центра приложения: {w3} пикселей на {h3} пикселей\n"
                                           f"Окно: {collaps_window}, {activ_window}")
        return collaps_window, activ_window


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    print(window.onPuchButtonGetLogClicked())
    window.show()
    app.exec()
