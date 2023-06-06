import Frente_rc
import ImagensCozinha_rc
import Lazer_rc
import Sala_rc
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class main():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.porta = uic.loadUi('porta.ui')
        self.lazer = uic.loadUi('lazer.ui')
        self.sala = uic.loadUi('sala.ui')
        self.cozinha = uic.loadUi('cozinha.ui')
        self.sofa = uic.loadUi('sofa.ui')
        self.quadro = uic.loadUi('quadro.ui')
        self.mesa = uic.loadUi('mesa.ui')
        self.pia = uic.loadUi('pia.ui')
        self.geladeira = uic.loadUi('geladeira.ui')
        self.armario = uic.loadUi('armario.ui')
        self.carta = uic.loadUi('carta.ui')
        self.tv = uic.loadUi('tv.ui')
        self.relogio = uic.loadUi('relogio.ui')
        self.teclado = uic.loadUi('teclado.ui')
        self.morse = uic.loadUi('morse.ui')

        self.porta.direita.clicked.connect(self.abrir_sala)
        self.porta.esquerda.clicked.connect(self.abrir_lazer)

        self.sala.direita.clicked.connect(self.abrir_cozinha)
        self.sala.esquerda.clicked.connect(self.abrir_porta) 
        self.sala.sofa.clicked.connect(self.abrir_sofa)
        self.sala.quadro.clicked.connect(self.abrir_quadro)
        self.sala.mesa.clicked.connect(self.abrir_mesa)
        self.sofa.voltar.clicked.connect(self.abrir_sala)
        self.quadro.voltar.clicked.connect(self.abrir_sala)
        self.mesa.voltar.clicked.connect(self.abrir_sala)
    
        self.cozinha.direita.clicked.connect(self.abrir_lazer)
        self.cozinha.esquerda.clicked.connect(self.abrir_sala)
        self.cozinha.pia.clicked.connect(self.abrir_pia)
        self.cozinha.geladeira.clicked.connect(self.abrir_geladeira)
        self.cozinha.armario.clicked.connect(self.abrir_armario)
        self.pia.voltar.clicked.connect(self.abrir_cozinha)
        self.geladeira.voltar.clicked.connect(self.abrir_cozinha)
        self.armario.voltar.clicked.connect(self.abrir_cozinha)
        self.geladeira.carta.clicked.connect(self.abrir_carta)
        self.carta.voltar.clicked.connect(self.abrir_geladeira)

        self.lazer.direita.clicked.connect(self.abrir_porta)
        self.lazer.esquerda.clicked.connect(self.abrir_cozinha)
        self.lazer.tv.clicked.connect(self.abrir_tv)
        self.lazer.relogio.clicked.connect(self.abrir_relogio)
        self.lazer.teclado.clicked.connect(self.abrir_teclado)
        self.lazer.morse.clicked.connect(self.abrir_morse)
        self.tv.voltar.clicked.connect(self.abrir_lazer)
        self.relogio.voltar.clicked.connect(self.abrir_lazer)
        self.teclado.voltar.clicked.connect(self.abrir_lazer)
        self.morse.voltar.clicked.connect(self.abrir_lazer)

        self.abrir_porta()
        app.exec()
        

    def abrir_porta(self):
        QApplication.closeAllWindows()
        self.porta.show()

    def abrir_cozinha(self):
        QApplication.closeAllWindows()
        self.cozinha.show()
    
    def abrir_sala(self):
        QApplication.closeAllWindows()
        self.sala.show()
    
    def abrir_lazer(self):
        QApplication.closeAllWindows()
        self.lazer.show()

    def abrir_sofa(self):
        QApplication.closeAllWindows()
        self.sofa.show()   

    def abrir_quadro(self):
        QApplication.closeAllWindows()
        self.quadro.show()      

    def abrir_mesa(self):
        QApplication.closeAllWindows()
        self.mesa.show()        

    def abrir_pia(self):
        QApplication.closeAllWindows()
        self.pia.show()   

    def abrir_geladeira(self):
        QApplication.closeAllWindows()
        self.geladeira.show()      

    def abrir_armario(self):
        QApplication.closeAllWindows()
        self.armario.show()    

    def abrir_carta(self):
         QApplication.closeAllWindows()
         self.carta.show()   

    def abrir_tv(self):
        QApplication.closeAllWindows()
        self.tv.show()   

    def abrir_relogio(self):
        QApplication.closeAllWindows()
        self.relogio.show()      

    def abrir_teclado(self):
        QApplication.closeAllWindows()
        self.teclado.show()    

    def abrir_morse(self):
         QApplication.closeAllWindows()
         self.morse.show()   

    
if __name__ == '__main__':
    j = main()
