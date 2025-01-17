import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("slider.ui",self)

        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(50)
        self.horizontalSlider.valueChanged.connect(self.getValueHorizontal)

    def getValueHorizontal(self):
        value=self.horizontalSlider.value()
        self.labelHorizontal.setText(str(value))

app= QApplication(sys.argv)
dialogo= Dialogo()
dialogo.show()
app.exec_()
