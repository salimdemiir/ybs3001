from PyQt4.QtGui import *
from PyQt4.QtCore import *

class scalableTable_view(QDialog):
    def __init__(self,parent=None):
        super(scalableTable_view,self).__init__(parent)
        
        grid=QGridLayout()

        self.table =QTableWidget()
        #self.table.resize(400,250)

        grid.addWidget(self.table)
        self.setLayout(grid)

class scalableTable_create(QDialog):
    def __init__(self,arry,parent=None):
        super(scalableTable_create,self).__init__(parent)

        dialog = scalableTable_view()
        
        dialog.table.setRowCount(len(arry))
        maxCol_count = 0
        for x in arry:
            count = len(arry[x]) 
            if ( count > maxCol_count):
                maxCol_count = count
                
        dialog.table.setColumnCount(maxCol_count)

        counter_x = 0
        for x in arry:
            counter_y=0
            for y in arry[x]:
                #tabloya ekleme
                dialog.table.setItem(counter_x, counter_y,QTableWidgetItem(y))
                counter_y += 1
            counter_x += 1
                

        dialog.exec_()
        
        

        
data = {0:["Can","Aydın","YBS"],1:["Semih","Yarar","YBS"],2:["Büşra","Demirgüreşçi","İktisat"]}
app   = QApplication([])
frame = scalableTable_create(data)
frame.show()
app.exec_
