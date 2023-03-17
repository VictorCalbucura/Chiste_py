import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class ventana1(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chistes Informaticos")
        self.resize(100, 150)
        texto = qtw.QLabel("¡Hola! ¿Quieres ver chistes informaticos?")
        texto.setFont(qtg.QFont("Helvetica", 15))
        texto.move(50, 100)
        boton = qtw.QPushButton("Si",clicked = lambda: self.cambioVentana2)
        boton.move(90, 140)
        self.show()
            
    def cambioVentana2(self):
        from vent2 import ventana2
        self.ventana2 = ventana2()
        self.ventana2.show()
        self.hide()