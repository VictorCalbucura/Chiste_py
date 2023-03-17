import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from vent1 import ventana1

if __name__ == "__main__":
    app = qtw.QApplication([])
    ventanaMain = ventana1()
    ventanaMain.show()          
    app.exec_()