"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""

from PySide6 import QtWidgets

from a_threads import WeatherHandler


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.lat = 0
        self.lon = 0

        self.initUi()
        self.__initSignals()
        self.weatherHandler = WeatherHandler()

    def initUi(self):
        """
        Инициализация Ui
        :return: None
        """
        self.inputLat = QtWidgets.QLineEdit()
        self.inputLat.setPlaceholderText("Введите широту")
        self.inputLon = QtWidgets.QLineEdit()
        self.inputLon.setPlaceholderText("Введите долготу")
        l_Lat_Lon = QtWidgets.QHBoxLayout()
        l_Lat_Lon.addWidget(self.inputLat)
        l_Lat_Lon.addWidget(self.inputLon)

        self.inputDelay = QtWidgets.QLineEdit()
        self.inputDelay.setPlaceholderText("Введите время задержки")

        self.outputWheather = QtWidgets.QTextEdit()

        self.pushButtonHandle = QtWidgets.QPushButton("Старт")
        self.pushButtonHandle.setCheckable(True)

        layout = QtWidgets.QVBoxLayout()

        layout.addLayout(l_Lat_Lon)
        layout.addWidget(self.inputDelay)
        layout.addWidget(self.outputWheather)
        layout.addWidget(self.pushButtonHandle)

        self.setLayout(layout)
        self.setMinimumSize(300, 140)

    def __initSignals(self):
        self.pushButtonHandle.clicked.connect(self.on_started)
        # self.outputWheather.setText(self.weatherHandler.wheatherHandlerSignal())


        # self.outputWheather.setPlainText(self.weatherHandler.data)

    def on_started(self):
        self.weatherHandler = WeatherHandler(lat=int(self.inputLat.text()), lon=int(self.inputLon.text()))
        self.weatherHandler.setDelay(int(self.inputDelay.text()))
        self.weatherHandler.start()
        self.weatherHandler.sleep(self.weatherHandler.delay1)
        self.weatherHandler.wheatherHandlerSignal.connect(self.apiUpdate)



    def get_signal_from_thread(self):
        if self.pushButtonHandle.isChecked():
            self.pushButtonHandle.setText('Остановить')
            self.inputLat.setReadOnly(True)
            self.inputLon.setReadOnly(True)
            self.outputWheather.setReadOnly(True)
        elif not self.pushButtonHandle.isChecked():
            self.weatherHandler.terminate()
            self.pushButtonHandle.setText('Запустить')
            self.inputLat.setReadOnly(False)
            self.inputLon.setReadOnly(False)
            self.outputWheather.setReadOnly(False)


    def apiUpdate(self, data):
        self.outputWheather.setText("str(data)")



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()