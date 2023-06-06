import Frente_rc
import ImagensCozinha_rc
import Lazer_rc
import Sala_rc
import sys
from PyQt5 import QtWidgets, uic

# oi
class main():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.sala = uic.loadUi('sala.ui')
        self.porta = uic.loadUi('porta.ui')
        self.abrir_porta()
        app.exec()
        
    def abrir_sala(self):
        self.porta.close()
        self.sala.show()
        print('oi')
        
    def abrir_porta(self):
        self.porta.show()
        self.porta.direita.clicked.connect(self.abrir_sala)
        

    
    
    
if __name__ == '__main__':
    j = main()

