from PyQt4.QtGui import *
from PyQt4.QtCore import*

class CalisanDevirHizi(QDialog):
    def __init__(self,parent=None):
        super(CalisanDevirHizi,self).__init__(parent)

        grid = QGridLayout()

        self.dbcs  = QLineEdit()
        self.dscs  = QLineEdit()

        self.iats  = QLineEdit()
        
        self.sonuc          = QLabel("")
        self.hesapla_button = QPushButton("Hesapla")
        
        grid.addWidget(QLabel("Dönem Başı Çalışan Sayısı"), 0, 0)
        grid.addWidget(self.dbcs, 0, 1)

        grid.addWidget(QLabel("Dönem Sonu Çalışan Sayısı"), 1, 0)
        grid.addWidget(self.dscs, 1, 1)

        grid.addWidget(QLabel("İşten Ayrılanların Toplam Sayısı"), 2, 0)
        grid.addWidget(self.iats, 2, 1)

        grid.addWidget(QLabel("Sonuc"), 3, 0)
        grid.addWidget(self.sonuc, 3, 1)
        
        grid.addWidget(self.hesapla_button, 4, 1)
        
        self.connect(self.hesapla_button,SIGNAL('pressed()'),self.cdh_cmd)

        self.setLayout(grid)
        self.setWindowTitle("Çalışan Devir Hızı Hesaplama Uygulaması")

    def cdh_cmd(self):
        iats =  int(self.iats.text())
        dbcs  = int(self.dbcs.text())
        dscs  = int(self.dscs.text())

        ocs = (dbcs+dscs)/2

        sonuc = round((iats/ocs)*100,2)

        self.sonuc.setText(str(sonuc))


app =  QApplication([])
frame= CalisanDevirHizi()
frame.show()
uyg.exec__
