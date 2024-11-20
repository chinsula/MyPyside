from PySide6 import QtWidgets

from lab1.ui.form1 import Ui_Form
class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    w = Window()
    w.show()
    app.exec()
