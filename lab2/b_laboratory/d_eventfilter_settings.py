"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets

from lab2.b_laboratory.ui import d_eventfilter_settings_form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = d_eventfilter_settings_form.Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

        self.ui.dial.setRange(0, 100)
        self.ui.dial.setSingleStep(1)

    def initSignals(self):
        self.ui.btnPlus.clicked.connect(self.onDialClicked)
        self.ui.dial.valueChanged.connect(self.onDialClicked)


    # слоты для подключения

    def onDialClicked(self, position=None):
        print(position)






if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
