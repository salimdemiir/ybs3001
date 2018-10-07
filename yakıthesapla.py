import sys
from PyQt4.QtGui import *

class view:
    def __init__(self):
        app = QApplication(sys.argv)
        frame = QWidget()

        self.box_main = QHBoxLayout()
       
        self.frame1()
        
        frame.setLayout(self.box_main)
        frame.setWindowTitle("Yakıt Hesaplayıcı")

        self.signals()
        
        frame.show()

        app.exec_()

    def signals(self):
        yakithesap_return = self.calculate_button.clicked.connect(lambda: calculate.hesapla(self,self.yol.text(),self.yuzkmyakit.text(),self.yakitFiyat.text()))
        

    def frame1(self):
        self.box1 = QVBoxLayout()
        
        label1 = QLabel("Araç Marka,Model")
        label2 = QLabel("Gidilecek Yol")
        label3 = QLabel("100Km de Harcanan Yakıt")
        label4 = QLabel("Yakıt Fiyatı")
        self.calculate_button = QPushButton('Hesapla')
        self.label_result_km = QLabel("0")

    #box1............................................
         
        self.box1.addWidget(label1)
        self.box1.addWidget(label2)
        self.box1.addWidget(label3)
        self.box1.addWidget(label4)
        self.box1.addWidget(self.label_result_km)
        self.box1.addWidget(self.calculate_button)
        
        
    #box2............................................
        self.box2 = QVBoxLayout()

        self.marka = QLineEdit()
        self.yol = QLineEdit()
        self.yuzkmyakit = QLineEdit()
        self.yakitFiyat = QLineEdit()
        self.compare_button = QPushButton('Kaydet')
        label_result_text = QLabel("Km Gidilen Yakıt Tutarı")
        
        self.box2.addWidget(self.marka)
        self.box2.addWidget(self.yol)
        self.box2.addWidget(self.yuzkmyakit)
        self.box2.addWidget(self.yakitFiyat)
        self.box2.addWidget(label_result_text)
        self.box2.addWidget(self.compare_button)
        
        
    #box3.................................................
        self.box3 = QVBoxLayout()

        label1 = QLabel("  ")
        label2 = QLabel(" Km")
        label3 = QLabel(" Lt/100km")
        label4 = QLabel("Lt/Tl")
        label5 = QLabel("  ")
        self.label_result_price = QLabel("0")
       
        
        self.box3.addWidget(label1)
        self.box3.addWidget(label2)
        self.box3.addWidget(label3)
        self.box3.addWidget(label4)
        self.box3.addWidget(self.label_result_price)
        self.box3.addWidget(label5)
        
           

     #box4.................................................
        self.box4 = QVBoxLayout()

        label1 = QLabel("  ")
        label2 = QLabel(" ")
        label3 = QLabel(" ")
        label4 = QLabel(" ")
        label5 = QLabel("  ")
        label_result_text2=QLabel("Tl")
        
        self.box4.addWidget(label1)
        self.box4.addWidget(label2)
        self.box4.addWidget(label3)
        self.box4.addWidget(label4)
        self.box4.addWidget(label_result_text2)
        self.box4.addWidget(label5)
        

        self.box_main.addLayout(self.box1)
        self.box_main.addLayout(self.box2)
        self.box_main.addLayout(self.box3)
        self.box_main.addLayout(self.box4)

    def return_result(self,km,price):
        self.label_result_km.setText(km)
        self.label_result_price.setText(str(price))
        

    

        
        
class calculate:
        def __init__(self):
           pass
        def hesapla(self,gyol,yuzkm_yakit,yfiyat):
            #100 km deki yakıt hesabı
            yakilan_yakit_lt = (int(gyol)*float(yuzkm_yakit))/100
            toplam_ucret = yakilan_yakit_lt*float(yfiyat)

            return view.return_result(self,gyol,round(toplam_ucret,2))

            
view()
calculate()
