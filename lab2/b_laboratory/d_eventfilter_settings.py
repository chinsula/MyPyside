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

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QSettings

from lab2.b_laboratory.ui import d_eventfilter_settings_form



class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = d_eventfilter_settings_form.Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        self.__loadSettings()


        self.ui.comboBox.addItem('oct')
        self.ui.comboBox.addItem('hex')
        self.ui.comboBox.addItem('bin')
        self.ui.comboBox.addItem('dec')


    # 1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
    # выводить новые значения в консоль
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key.Key_Plus:
            value = self.ui.lcdNumber.value()
            self.ui.lcdNumber.display(value + 1)
            print(self.ui.lcdNumber.value())
        elif e.key() == QtCore.Qt.Key.Key_Minus:
            value = self.ui.lcdNumber.value()
            self.ui.lcdNumber.display(value - 1)
            print(self.ui.lcdNumber.value())


    def __loadSettings(self):
        settings = QSettings("MySettings")

        self.ui.comboBox.setCurrentText(settings.value('saved_value_cbox'))
        self.ui.lcdNumber.display(settings.value('saved_value_lcd'))


    def __saveSettings(self):
        settings = QSettings("MySettings")

        settings.setValue('saved_value_cbox', self.ui.comboBox.currentText())
        settings.setValue('saved_value_lcd', self.ui.lcdNumber.value())

    def closeEvent(self, event):
        self.__saveSettings()


    def initSignals(self):
        self.ui.dial.sliderMoved.connect(self.onDialClicked)
        self.ui.horizontalSlider.sliderMoved.connect(self.onHorizontalSliderClicked)
        self.ui.comboBox.currentTextChanged.connect(self.onComboBoxChanged)

    # 2. Соединить между собой QDial, QSlider, QLCDNumber
    #    (изменение значения в одном, изменяет значения в других)


    # слоты для подключения

    def onDialClicked(self):
        value = self.ui.dial.value()
        self.ui.lcdNumber.display(value)
        self.ui.horizontalSlider.setValue(value)

    def onHorizontalSliderClicked(self):
        value = self.ui.horizontalSlider.value()
        self.ui.lcdNumber.display(value)
        self.ui.dial.setValue(value)

    def onComboBoxChanged(self):
        if self.ui.comboBox.currentText() == 'hex':
            self.ui.lcdNumber.setHexMode()
            value = hex(int(self.ui.lcdNumber.value()))
            self.ui.lcdNumber.display(value)
            print(hex(int(self.ui.lcdNumber.value())))
        elif self.ui.comboBox.currentText() == 'oct':
            self.ui.lcdNumber.setOctMode()
            value = oct(int(self.ui.lcdNumber.value()))
            self.ui.lcdNumber.display(value)
            print(oct(int(self.ui.lcdNumber.value())))
        elif self.ui.comboBox.currentText() == 'bin':
            self.ui.lcdNumber.setBinMode()
            value = bin(int(self.ui.lcdNumber.value()))
            self.ui.lcdNumber.display(value)
            print(bin(int(self.ui.lcdNumber.value())))
        elif self.ui.comboBox.currentText() == 'dec':
            self.ui.lcdNumber.setDecMode()
            value = bin(int(self.ui.lcdNumber.value()))
            self.ui.lcdNumber.display(value)
            print(self.ui.lcdNumber.value())



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
