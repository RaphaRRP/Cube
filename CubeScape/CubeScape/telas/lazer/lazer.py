# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lazer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_lazer(object):
    def setupUi(self, lazer):
        lazer.setObjectName("lazer")
        lazer.resize(816, 577)
        lazer.setMinimumSize(QtCore.QSize(816, 577))
        lazer.setMaximumSize(QtCore.QSize(816, 577))
        self.lazer1 = QtWidgets.QWidget(lazer)
        self.lazer1.setObjectName("lazer1")
        self.label = QtWidgets.QLabel(self.lazer1)
        self.label.setGeometry(QtCore.QRect(0, 0, 816, 577))
        self.label.setMinimumSize(QtCore.QSize(816, 577))
        self.label.setMaximumSize(QtCore.QSize(816, 577))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/png/LazerCube.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.relogio = QtWidgets.QPushButton(self.lazer1)
        self.relogio.setGeometry(QtCore.QRect(260, 130, 141, 141))
        self.relogio.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.relogio.setText("")
        self.relogio.setObjectName("relogio")
        self.teclado = QtWidgets.QPushButton(self.lazer1)
        self.teclado.setGeometry(QtCore.QRect(210, 430, 241, 131))
        self.teclado.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.teclado.setText("")
        self.teclado.setObjectName("teclado")
        self.tv = QtWidgets.QPushButton(self.lazer1)
        self.tv.setGeometry(QtCore.QRect(450, 140, 301, 221))
        self.tv.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.tv.setText("")
        self.tv.setObjectName("tv")
        self.papel = QtWidgets.QPushButton(self.lazer1)
        self.papel.setGeometry(QtCore.QRect(590, 360, 51, 31))
        self.papel.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.papel.setText("")
        self.papel.setObjectName("papel")
        self.label_2 = QtWidgets.QLabel(self.lazer1)
        self.label_2.setGeometry(QtCore.QRect(10, 260, 50, 50))
        self.label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/png/setaE.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.lazer1)
        self.label_3.setGeometry(QtCore.QRect(760, 260, 50, 50))
        self.label_3.setMinimumSize(QtCore.QSize(50, 50))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/png/setaD.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.esquerda = QtWidgets.QPushButton(self.lazer1)
        self.esquerda.setGeometry(QtCore.QRect(10, 250, 61, 61))
        self.esquerda.setStyleSheet("background-color:rgba(0, 0, 0, 0);")
        self.esquerda.setText("")
        self.esquerda.setObjectName("esquerda")
        self.direira = QtWidgets.QPushButton(self.lazer1)
        self.direira.setGeometry(QtCore.QRect(760, 250, 51, 61))
        self.direira.setStyleSheet("background-color:rgba(0, 0, 0, 0);")
        self.direira.setText("")
        self.direira.setObjectName("direira")
        lazer.setCentralWidget(self.lazer1)

        self.retranslateUi(lazer)
        QtCore.QMetaObject.connectSlotsByName(lazer)

    def retranslateUi(self, lazer):
        _translate = QtCore.QCoreApplication.translate
        lazer.setWindowTitle(_translate("lazer", "MainWindow"))
import lazer_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    lazer = QtWidgets.QMainWindow()
    ui = Ui_lazer()
    ui.setupUi(lazer)
    lazer.show()
    sys.exit(app.exec_())
