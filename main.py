import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Загружаем интерфейс из сгенерированного файла
        loadUi('main.ui', self)

        # Загружаем данные из базы данных
        self.load_data()

    def load_data(self):
        try:
            conn = sqlite3.connect('coffee.sqlite')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM coffee')
            rows = cursor.fetchall()

            # Устанавливаем количество строк в таблице равное количеству записей в базе данных
            self.tableWidget.setRowCount(len(rows))

            # Заполняем таблицу данными из базы данных
            for i, row in enumerate(rows):
                for j, item in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))

            # Устанавливаем сообщение в statusBar
            self.statusbar.showMessage(f"Нашлось {len(rows)} записей")

        except sqlite3.Error as e:
            print(f"Ошибка при загрузке данных из базы данных: {e}")

        finally:
            conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    coffee_app = CoffeeApp()
    coffee_app.show()
    sys.exit(app.exec_())
