"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets, QtGui

import c_weatherapi_widget
import b_systeminfo_widget



class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("practice_3")
        window1 = c_weatherapi_widget.Window()
        window2 = b_systeminfo_widget.Window()

        layout = QtWidgets.QHBoxLayout()

        layout.addWidget(window1)
        layout.addWidget(window2)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()