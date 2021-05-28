from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt, QPropertyAnimation

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 900)

        self.Port = QtWidgets.QComboBox(Form)
        self.Port.setGeometry(QtCore.QRect(10, 10, 380, 35))
        self.Port.setObjectName("Port")

        self.Speed = QtWidgets.QComboBox(Form)
        self.Speed.setGeometry(QtCore.QRect(410, 10, 380, 35))
        self.Speed.setObjectName("Speed")

        self.Country = QtWidgets.QComboBox(Form)
        self.Country.setGeometry(QtCore.QRect(10, 55, 380, 35))
        self.Country.setObjectName("Country")

        self.Sity = QtWidgets.QComboBox(Form)
        self.Sity.setGeometry(QtCore.QRect(410, 55, 380, 35))
        self.Sity.setObjectName("Sity")

        self.ConnectButton = QtWidgets.QPushButton(Form)
        self.ConnectButton.setGeometry(QtCore.QRect(10, 100, 780, 35))
        self.ConnectButton.setObjectName("ConnectButton")

        font = QtGui.QFont()
        font.setPointSize(11)

        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(370, 600, 60, 30))
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(230, 640, 340, 30))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        font = QtGui.QFont()
        font.setPointSize(17)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(300, 690, 200, 50))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_time_1 = QtWidgets.QLabel(Form)
        self.label_time_1.setGeometry(QtCore.QRect(360, 750, 100, 50))
        self.label_time_1.setFont(font)
        self.label_time_1.setObjectName("label_time_1")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(100, 720, 150, 50))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_time_2 = QtWidgets.QLabel(Form)
        self.label_time_2.setGeometry(QtCore.QRect(110, 780, 100, 50))
        self.label_time_2.setFont(font)
        self.label_time_2.setObjectName("label_time_2")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(650, 720, 150, 50))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_time_3 = QtWidgets.QLabel(Form)
        self.label_time_3.setGeometry(QtCore.QRect(650, 780, 100, 50))
        self.label_time_3.setFont(font)
        self.label_time_3.setObjectName("label_time_3")

        self.scene = QtWidgets.QGraphicsScene(0, 0, 770, 430, Form)
        self.scene.setObjectName("scene")

        self.yellowBrush = QBrush(Qt.yellow)
        self.blackBrush = QBrush(Qt.black)
        self.yellowPen = QPen(Qt.black)
        self.bluePen = QPen(Qt.blue)
        self.yellowPen.setWidth(1)
        self.bluePen.setWidth(10)
        self.blackPen = QPen(Qt.black)
        self.blackPen.setWidth(10)

        self.view = QGraphicsView(self.scene, Form)
        self.view.setGeometry(10, 150, 780, 440)
        self.view.setObjectName("view")
        self.sun = self.scene.addEllipse(0, 0, 70, 70, self.yellowPen, self.yellowBrush)
        self.line1 = self.scene.addLine(0, 0, 75, 0, self.bluePen)
        self.line2 = self.scene.addLine(0, 0, 75, 0, self.bluePen)
        self.rect = self.scene.addRect(0, 0, 10, 100, self.blackPen, self.blackBrush)
        self.line1.setRotation(180)
        self.line1.setPos(355, 335)
        self.line1.setRotation(0)

        self.line2.setPos(355, 335)
        self.line2.setRotation(180)
        self.rect.setPos(350, 340)
        self.sun.setPos(self.x, self.y)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Солнечная батарея"))
        self.label_1.setText(_translate("Form", "Статус"))
        self.label_2.setText(_translate("Form", "Поверните потенциометра на х градусов"))
        self.label_3.setText(_translate("Form", "Световой день"))
        self.label_time_1.setText(_translate("Form", "XX:XX"))
        self.label_4.setText(_translate("Form", "Восход"))
        self.label_time_2.setText(_translate("Form", "XX:XX"))
        self.label_5.setText(_translate("Form", "Закат"))
        self.label_time_3.setText(_translate("Form", "XX:XX"))
        self.ConnectButton.setText(_translate("Form", "Пpодключиться"))
