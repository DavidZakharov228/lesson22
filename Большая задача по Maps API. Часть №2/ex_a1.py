import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

SCREEN_SIZE = [600, 450]


class Example(QWidget):
    def __init__(self):
        print('Ведите координаты через пробел:')
        self.cor = input()
        if ',' in self.cor:
            print('Координаты введены не верно')
        print('Введите маштаб в %:')
        print('Чем меньше число, тем больше охват карты')
        self.mash = input()
        self.check()
        super().__init__()
        self.initUI()

    def check(self):
        self.cor = ','.join(self.cor.split())
        if 100 < float(self.mash):
            self.prov = 1
            print('Маштаб должен быть введен в диапазоне от 0 до 100!')
        self.mash = round(0.17 * int(self.mash))
        if self.mash < 0:
            self.mash = 0
        if self.mash > 17:
            self.mash = 17

    def keyPressEvent(self, event):
        scale = float(self.mash) // 0.17
        if event.key() == 16777238:
            if scale + 1 <= 100:
                scale1 = float(scale) + 10
            else:
                x = 100 - scale
                scale1 = float(scale) + x
            self.mash = round(float(scale1) * 0.17)
            if self.mash < 0:
                self.mash = 0
            if self.mash > 17:
                self.mash = 17
        if event.key() == 16777239:
            if scale - 1 >= 0:
                scale1 = float(scale) - 10
            else:
                scale1 = 0
            # 37.530887 55.703118
            # pgup 16777238 16777235
            # pgdown 16777239 16777237
            self.mash = round(float(scale1) * 0.17)
            if self.mash < 0:
                self.mash = 0
            if self.mash > 17:
                self.mash = 17
        self.getImage()

    def getImage(self):
        map_request = "http://static-maps.yandex.ru/1.x/?ll=" + self.cor + "&z=" + str(
            self.mash) + "&size=600,450&l=map"
        response = requests.get(map_request)

        if not response:
            print('Координаты введены неверно!')
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)

        self.set_image(self.map_file)

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')
        self.image = QLabel(self)
        self.getImage()

    def set_image(self, map):
        self.pixmap = QPixmap(map)
        self.image.move(0, 0)
        self.image.setPixmap(self.pixmap)

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
