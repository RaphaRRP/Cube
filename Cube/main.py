import sys
import typing
from PyQt5 import QtCore

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit,
                               QPushButton, QWidget, QToolTip, QLabel)
from PyQt5 import QtGui

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.esquerda = 100
        self.topo = 100 
        self.largura = 800
        self.altura = 600
        self.titulo = "primeira janela"

        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(25, 20)
        self.caixa_texto.resize(220, 40)
        


        botao1 = QPushButton('Botao 1', self)
        botao1.move(100, 200)
        botao1.resize(150, 80)
        botao1.setStyleSheet('QPushButton {background-color:#0FB328;font-size:20px}')
        botao1.clicked.connect(self.botao1_click)

        botao2 = QPushButton('Botao 2', self)
        botao2.move(325, 200)
        botao2.resize(150, 80)
        botao2.setStyleSheet('QPushButton {background-color:#0FB328;font-size:20px}')
        botao2.clicked.connect(self.botao2_click)



        botao_texto = QPushButton('Enviar texto', self)
        botao_texto.move(550, 200)
        botao_texto.resize(150, 80)
        botao_texto.setStyleSheet('QPushButton {background-color:green;font-size:20px}')
        botao_texto.clicked.connect(self.mostra_texto)

        self.label_texto = QLabel(self)
        self.label_texto.setText("Digitou: ")
        self.label_texto.move(500, 100)
        self.label_texto.setStyleSheet('QLabel {font:bold;font-size:20px;color:green}')
        self.label_texto.resize(300, 25)




        self.label_1 = QLabel(self)
        self.label_1.setText("aperte um botao")
        self.label_1.move(100, 100)
        self.label_1.setStyleSheet('QLabel {font:bold;font-size:20px;color:green}')
        self.label_1.resize(300, 25)

        self.carro1 = QLabel(self)
        self.carro1.move(50, 400)
        self.carro1.setPixmap(QtGui.QPixmap('imagens/carro1.png'))
        self.carro1.resize(450, 100)

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        self.label_1.setText("Carro 1 seleciondado")
        self.label_1.setStyleSheet('QLabel {font:bold;font-size:20px;color:blue}')
        self.carro1.setPixmap(QtGui.QPixmap('imagens/carro1.png'))

    def botao2_click(self):
        self.label_1.setText("Carro 2 selecionado")
        self.label_1.setStyleSheet('QLabel {font:bold;font-size:20px;color:red}')
        self.carro1.setPixmap(QtGui.QPixmap('imagens/carro2.png'))

    def mostra_texto(self):
        conteudo = self.caixa_texto.text()
        self.label_texto.setText("Digitou: "+ conteudo)



aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())