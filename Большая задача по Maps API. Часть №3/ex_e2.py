import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MapWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.width = 640
        self.height = 480
        self.center = [55.755826, 37.617299] # Координаты центра карты (Москва)
        self.zoom = 10 # Масштаб карты
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, self.width, self.height)
        self.setWindowTitle('Map')
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, self.width, self.height)
        self.showMap()

    def showMap(self):
        map_url = f"https://static-maps.yandex.ru/1.x/?ll={self.center[1]},{self.center[0]}&z={self.zoom}&size={self.width},{self.height}&l=map"
        pixmap = QPixmap(map_url)
        self.label.setPixmap(pixmap)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Up:
            self.center[0] = min(self.center[0] + 0.01 * (2 ** (15 - self.zoom)), 85)
        elif key == Qt.Key_Down:
            self.center[0] = max(self.center[0] - 0.01 * (2 ** (15 - self.zoom)), -85)
        elif key == Qt.Key_Right:
            self.center[1] = min(self.center[1] + 0.01 * (2 ** (15 - self.zoom)), 180)
        elif key == Qt.Key_Left:
            self.center[1] = max(self.center[1] - 0.01 * (2 ** (15 - self.zoom)), -180)
        self.showMap()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapWidget()
    ex.show()
    sys.exit(app.exec_())