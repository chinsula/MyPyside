"""
Модуль в котором содержаться потоки Qt
"""

import time
from urllib import request

import psutil
from PySide6 import QtCore


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)  # Создайте экземпляр класса Signal и передайте ему в конструктор тип данных передаваемого значения (в текущем случае list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None  #  создайте атрибут класса self.delay = None, для управлением задержкой получения данных

    def run(self) -> None:  # переопределить метод run
        if self.delay is None:  # Если задержка не передана в поток перед его запуском
            self.delay = 1  # то устанавливайте значение 1

        while True:  # Запустите бесконечный цикл получения информации о системе
            cpu_value = psutil.cpu_percent()  # с помощью вызова функции cpu_percent() в пакете psutil получите загрузку CPU
            ram_value = psutil.virtual_memory()  # с помощью вызова функции virtual_memory().percent в пакете psutil получите загрузку RAM
            data = [cpu_value, ram_value, self.delay]
            self.systemInfoReceived.emit(data)  # с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM
            time.sleep(self.delay)  # с помощью функции .sleep() приостановите выполнение цикла на время self.delay
            print("CPU value", cpu_value, "RAM value", ram_value)

class WeatherHandler(QtCore.QThread):
    wheatherHandlerSignal = QtCore.Signal(int) # Пропишите сигналы, которые считаете нужными

    def __init__(self, lat=0, lon=0, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = None

    def setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """

        self.delay1 = delay

    def run(self, requests=None) -> None:
        # настройте метод для корректной работы
        while self.__status:
            # Примерный код ниже
            response = requests.get(self.__api_url)
            data = response.json()
            self.wheatherHandlerSignal.emit(data)
            time.sleep(self.delay)

