"""
Подключение формы созданной в дизайнере

Команда для конвертации формы:
PySide6-uic path_to_form.ui -o path_to_form.py
"""

from PySide6 import QtWidgets

from lab1.ui import b_login, c_ship_parameters, d_engine_settings, e_profile_card, f_book_shop, g_calculator  # Импортируем класс
# формы


class Window(QtWidgets.QWidget):  # наследуемся от того же класса, что и форма в QtDesigner
    def __init__(self, ui, parent=None):
        super().__init__(parent)

        # Создание "прокси" переменной для работы с формой
        self.ui = ui
        self.ui.setupUi(self)


def get_start_window(forma):
    """
    Запуск окна с полученными параметрами
    :param forma: вид окна
    :return:
    """
    app = QtWidgets.QApplication()
    window = Window(forma)
    window.show()
    app.exec()


def get_forma_window():
    """
    Получение от пользователя вида запрашиваемого окна:
    :return:
    """
    value_window = int(input("Введите номер окна:\n1 - Логин;"
                             "\n2-Параметры корабля\n3 - Настройки двигателя"
                             "\n4 - Профиль карты\n5 - Книжный магазин\n6 - Калькулятор\n"))
    if value_window == 1:
        forma = b_login.Ui_Form()
    elif value_window == 2:
        forma = c_ship_parameters.Ui_Form()
    elif value_window == 3:
        forma = d_engine_settings.Ui_Form()
    elif value_window == 4:
        forma = e_profile_card.Ui_Form()
    elif value_window == 5:
        forma = f_book_shop.Ui_Form()
    elif value_window == 6:
        forma = g_calculator.Ui_Form()
    return forma


if __name__ == "__main__":
    get_start_window(get_forma_window())
