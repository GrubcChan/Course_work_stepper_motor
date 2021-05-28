import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsPixmapItem
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt, QPropertyAnimation, QIODevice, QTimer, QObject
import design
import requests
from bs4 import BeautifulSoup
import serial
import math
from datetime import datetime
import csv
import glob
import serial
from  port import serial_ports, speeds

class LedApp(QMainWindow, design.Ui_Form):
    x = 360
    y = 10
    const_x = 350
    const_y = 360

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Port.addItems(serial_ports())
        self.Speed.addItems(speeds)
        self.realport = None
        self.ConnectButton.clicked.connect(self.connectB)

    def connectB(self):
        try:
            self.realport = serial.Serial(self.Port.currentText(), int(self.Speed.currentText()))
            data = self.realport.read()
            self.rotate_solar_battery(int(data))
            self.ConnectButton.setStyleSheet("background-color: green")
            self.ConnectButton.setText('Обновить')
        except Exception as e:
            print(e)

    def rotate_sun(self, a):

        x = self.x
        y = self.y
        self.sun.setPos(x, y)
        self.x = self.const_x + ((x - self.const_x) * math.cos(a)) - ((y - self.const_y) * math.sin(a))
        self.y = self.const_y + ((y - self.const_y) * math.cos(a)) + ((x - self.const_x) * math.sin(a))
        if self.y > 360:
            self.x = 0
            self.y = 360

    def rotate_solar_battery(self, a):
        a = -a
        self.line1.setRotation(a)
        self.line2.setRotation(a-180)

    def send(self):
        if self.realport:
            self.realport.write(b'b')

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()

    def drawBrushes(self, qp):
        qp.setPen(QPen(Qt.gray, 1, Qt.SolidLine))
        qp.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        qp.drawRect(0, 0, 800, 900)
        qp.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        qp.setBrush(QBrush(QColor.fromCmyk(123, 123, 123, 1), Qt.SolidPattern))
        qp.drawRect(10, 150, 780, 440)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LedApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
