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
from QTPg.ChartView import ChartView

import sqlite3 as sql
import readdb as rdb
import pandas as pd

class MainWidow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._MakeStockBasicTableView()
        self._MakeChartView()
        self.hasKechuangban = True
    
    def testPrint(self):
        print('test')
        
    def slot_cur_draw(self):
        cur_start_time = self.ui.dateEdit_cur_start_time.text().replace('/','')
        cur_end_time = self.ui.dateEdit_cur_end_time.text().replace('/','')
        ts_code = self.ui.lineEdit_cur_tscode.text()
        print('start:'+cur_start_time+' end:'+cur_end_time)
        sql_con = sql.connect('stock.db')
        data_daily = rdb.read_daily_by_date_and_tscode(sql_con, ts_code, cur_start_time, cur_end_time)
        self.ChartView.SetLineSeriesData([data_daily.close])
        print(data_daily)
        sql_con.close()
        self.ChartView.Show()
    
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
        
    def _MakeChartView(self):
        self.ChartView = ChartView(self.ui.widget_chartview)
        '''
        list_x = [1,2,3,4,5,6,7]
        list_y = [3,4,5,6,7,8,11]
        self.ChartView.SetLineSeries(list_x, list_y,'测试线')
        self.ChartView.Show()
        '''
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWidow();
    
    window.show()
    sys.exit(app.exec_())