import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from chistes import Chiste
    


class ventana2(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chistes Informaticos")
        self.setLayout(qtw.QVBoxLayout())
        self.arrayChistes = [Chiste("¿Cómo se llama el mejor programador de la historia?\nCtrl+C, Ctrl+V.", "chiste\imagenesCodigo\chiste1.jpg"),
                Chiste("Un programador que no duerme tiene un bug en la cama.", "chiste\imagenesCodigo\chiste2.jpg"),
                Chiste("¿Cuál es la diferencia entre un programador y un cirujano?\nUn cirujano siempre sabe qué está haciendo.", "chiste\imagenesCodigo\chiste3.jpg"),
                Chiste("¿Cómo se llama un grupo de programadores? Un array.", "chiste\imagenesCodigo\chiste4.jpeg"),
                Chiste("¿Por qué los programadores son buenos para el poker?\nPorque son expertos en ocultar errores.", "chiste\imagenesCodigo\chiste5.jpg"),
                Chiste("¿Por qué los programadores no pueden cocinar?\nPorque siempre confunden las tazas con los bits.", "chiste\imagenesCodigo\chiste6.jpg"),
                Chiste("La solución más rápida a cualquier problema de programación es eliminar el código.", "chiste\imagenesCodigo\chiste7.jpg"),
                Chiste("Las computadoras son como el aire acondicionado\nDejan de funcionar cuando abres ventanas.", "chiste\imagenesCodigo\chiste8.jpg"),
                Chiste("¿Por qué los programadores no pueden escribir poesía?\nPorque siempre quieren poner punto y coma al final de cada verso.", "chiste\imagenesCodigo\chiste9.jpg")]
        self.i = 0
        chisteActual = self.arrayChistes[0]
        self.texto = qtw.QLabel(chisteActual.texto)
        self.texto.setFont(qtg.QFont("Helvetica", 15))
        self.layout().addWidget(self.texto)
        self.boton = qtw.QPushButton("Ver otro chiste",clicked = lambda: self.cambioChiste())
        self.img = qtg.QPixmap(chisteActual.imagen)
        self.etq = qtw.QLabel(self)
        self.etq.setPixmap(self.img)
        self.layout().addWidget(self.etq)
        self.layout().addWidget(self.boton)
        self.show()
        
    def cambioChiste(self):
        if self.i < 8:
            self.i += 1
        else:
            self.i = 0
        chisteActual = self.arrayChistes[self.i]
        self.texto.setText(chisteActual.texto)
        self.img = qtg.QPixmap(chisteActual.imagen)
        self.etq.setPixmap(self.img)
            
            
 
