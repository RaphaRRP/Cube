# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'geladeira.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_geladeira(object):
    def setupUi(self, geladeira):
        geladeira.setObjectName("geladeira")
        geladeira.resize(816, 577)
        geladeira.setMinimumSize(QtCore.QSize(816, 577))
        geladeira.setMaximumSize(QtCore.QSize(816, 577))
        self.geladeira1 = QtWidgets.QWidget(geladeira)
        self.geladeira1.setObjectName("geladeira1")
        self.label = QtWidgets.QLabel(self.geladeira1)
        self.label.setGeometry(QtCore.QRect(0, 0, 816, 577))
        self.label.setMinimumSize(QtCore.QSize(816, 577))
        self.label.setMaximumSize(QtCore.QSize(816, 577))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/png/geladeira.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.geladeira1)
        self.label_2.setGeometry(QtCore.QRect(720, 120, 81, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Cube/imagens/Cozinha/carta3.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.voltar = QtWidgets.QPushButton(self.geladeira1)
        self.voltar.setGeometry(QtCore.QRect(350, 510, 120, 60))
        self.voltar.setMinimumSize(QtCore.QSize(120, 60))
        self.voltar.setStyleSheet("border-radius: 1px;\n"
"background-color: rgba(0, 0, 0, 0.7);\n"
"color: grey;\n"
"font-size: 30px;")
        self.voltar.setObjectName("voltar")
        self.pushButton_2 = QtWidgets.QPushButton(self.geladeira1)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 150, 61, 71))
        self.pushButton_2.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        geladeira.setCentralWidget(self.geladeira1)

        self.retranslateUi(geladeira)
        QtCore.QMetaObject.connectSlotsByName(geladeira)

    def retranslateUi(self, geladeira):
        _translate = QtCore.QCoreApplication.translate
        geladeira.setWindowTitle(_translate("geladeira", "MainWindow"))
        self.voltar.setText(_translate("geladeira", "Voltar"))
import ImagensCozinha_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    geladeira = QtWidgets.QMainWindow()
    ui = Ui_geladeira()
    ui.setupUi(geladeira)
    geladeira.show()
    sys.exit(app.exec_())