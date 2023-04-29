import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap
import requests


class MapWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Map App')
        self.setGeometry(100, 100, 800, 600)

        # Создаем поля ввода координат и масштаба
        self.lat_edit = QLineEdit(self)
        self.lat_edit.move(20, 20)
        self.lon_edit = QLineEdit(self)
        self.lon_edit.move(20, 50)
        self.scale_edit = QLineEdit(self)
        self.scale_edit.move(20, 80)

        # Создаем кнопку для загрузки карты
        self.map_button = QPushButton('Load Map', self)
        self.map_button.move(20, 110)
        self.map_button.clicked.connect(self.load_map)

        # Создаем метку для отображения карты
        self.map_label = QLabel(self)
        self.map_label.setGeometry(150, 20, 620, 560)

    def load_map(self):
        # Получаем значения координат и масштаба из полей ввода
        lat = self.lat_edit.text()
        lon = self.lon_edit.text()
        scale = self.scale_edit.text()

        # Формируем запрос к API Яндекс карт
        api_key = '40d1649f-0493-4b70-98ba-98533de7710b'
        map_type = 'map'
        response = requests.get(
            f'https://static-maps.yandex.ru/1.x/?ll={lon},{lat}&size=620,560&z={scale}&l={map_type}&apikey={api_key}')

        # Загружаем карту в метку
        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        self.map_label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    map_window = MapWindow()
    map_window.show()
    sys.exit(app.exec_())