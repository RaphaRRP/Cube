# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pia.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pia(object):
    def setupUi(self, pia):
        pia.setObjectName("pia")
        pia.resize(816, 577)
        pia.setMinimumSize(QtCore.QSize(816, 577))
        pia.setMaximumSize(QtCore.QSize(816, 577))
        self.pia1 = QtWidgets.QWidget(pia)
        self.pia1.setObjectName("pia1")
        self.label = QtWidgets.QLabel(self.pia1)
        self.label.setGeometry(QtCore.QRect(0, 0, 816, 577))
        self.label.setMinimumSize(QtCore.QSize(816, 577))
        self.label.setMaximumSize(QtCore.QSize(816, 577))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/png/pia.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.voltar = QtWidgets.QPushButton(self.pia1)
        self.voltar.setGeometry(QtCore.QRect(350, 510, 120, 60))
        self.voltar.setMinimumSize(QtCore.QSize(120, 60))
        self.voltar.setStyleSheet("border-radius: 1px;\n"
"background-color: rgba(0, 0, 0, 0.7);\n"
"color: grey;\n"
"font-size: 30px;")
        self.voltar.setObjectName("voltar")
        pia.setCentralWidget(self.pia1)

        self.retranslateUi(pia)
        QtCore.QMetaObject.connectSlotsByName(pia)

    def retranslateUi(self, pia):
        _translate = QtCore.QCoreApplication.translate
        pia.setWindowTitle(_translate("pia", "MainWindow"))
        self.voltar.setText(_translate("pia", "Voltar"))
import ImagensCozinha_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pia = QtWidgets.QMainWindow()
    ui = Ui_pia()
    ui.setupUi(pia)
    pia.show()
    sys.exit(app.exec_())
