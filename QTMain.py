'''
Created on 2020年1月2日

@author: Administrator
'''

from PyQt5 import QtWidgets, QtGui, QtCore
from QTUI import Ui_MainWindow
import sys
from update import UpdateFunction
import threading

from QTPg.StockBasicModle import StockBasicModle

class MainWidow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._MakeStockBasicTableView()
        self.hasKechuangban = True
    
    def testPrint(self):
        print('test')
    def slot_reset_stockbasic(self):
        self.ui.lineEdit_filer_industry.setText('')
        self.ui.lineEdit_sharename_filter.setText('')
        self.ui.checkBox_kechuangban.setChecked(True)
        self.ui.comboBox_concept.setCurrentIndex(0)
        self.StockBasicModle.ResetStockBasic()
    
    def slot_filer_stockbasic(self):
        patten_name = self.ui.lineEdit_sharename_filter.text()
        self.StockBasicModle.FilterByName(patten_name)
        patten_industry = self.ui.lineEdit_filer_industry.text()
        self.StockBasicModle.FilterByIndustry(patten_industry)
        patten_concept = self.ui.comboBox_concept.currentText()
        self.StockBasicModle.FilterByConcept(patten_concept)
        listdate = self.ui.dateEdit_listdate.text().replace('/','')
        self.StockBasicModle.UpdateFilter(self.hasKechuangban, listdate)
        
    def slot_KechuangbanClick(self,checked):
        if checked:
            self.hasKechuangban = True
        else:
            self.hasKechuangban = False
    
    def slot_StockBasicClick(self,index):
        data = self.StockBasicModle.GetData(index.row())
        #print(data['name'])
        self.ui.lineEdit_cur_tscode.setText(data.ts_code)
        self.ui.lineEdit_cur_name.setText(data['name'])
    
    def slot_UpdateDataBase(self):
        def subfun():
            startTime = self.ui.dateTimeEdit_Update_StartTime.text().replace('/','')
            endTime = self.ui.dateTimeEdit_Update_EndTime.text().replace('/','')
            print('updateDateBase:'+startTime+" "+endTime)
            UpdateFunction(startTime, endTime)
        
        t = threading.Thread(target=subfun)
        t.start()
        
    def _MakeStockBasicTableView(self):
        self.StockBasicModle = StockBasicModle(self.ui.tableView_stockbasic)
        self.StockBasicModle.Init_Concept_ComboBox(self.ui.comboBox_concept)
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWidow();
    
    window.show()
    sys.exit(app.exec_())