# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'morse.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_morse(object):
    def setupUi(self, morse):
        morse.setObjectName("morse")
        morse.resize(816, 577)
        morse.setMinimumSize(QtCore.QSize(816, 577))
        morse.setMaximumSize(QtCore.QSize(816, 577))
        self.morse1 = QtWidgets.QWidget(morse)
        self.morse1.setObjectName("morse1")
        self.label = QtWidgets.QLabel(self.morse1)
        self.label.setGeometry(QtCore.QRect(0, 0, 816, 577))
        self.label.setMinimumSize(QtCore.QSize(816, 577))
        self.label.setMaximumSize(QtCore.QSize(816, 577))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/png/morse.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.voltar = QtWidgets.QPushButton(self.morse1)
        self.voltar.setGeometry(QtCore.QRect(350, 510, 120, 60))
        self.voltar.setMinimumSize(QtCore.QSize(120, 60))
        self.voltar.setStyleSheet("border-radius: 1px;\n"
"background-color: rgba(0, 0, 0, 0.7);\n"
"color: grey;\n"
"font-size: 30px;")
        self.voltar.setObjectName("voltar")
        morse.setCentralWidget(self.morse1)

        self.retranslateUi(morse)
        QtCore.QMetaObject.connectSlotsByName(morse)

    def retranslateUi(self, morse):
        _translate = QtCore.QCoreApplication.translate
        morse.setWindowTitle(_translate("morse", "MainWindow"))
        self.voltar.setText(_translate("morse", "Voltar"))
import lazer_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    morse = QtWidgets.QMainWindow()
    ui = Ui_morse()
    ui.setupUi(morse)
    morse.show()
    sys.exit(app.exec_())