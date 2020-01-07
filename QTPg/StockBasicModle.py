'''
Created on 2020年1月6日

@author: Administrator
'''

from PyQt5 import QtGui
import sqlite3 as sql
import readdb as rdb

class StockBasicModle(object):
    '''
    classdocs
    '''


    def __init__(self, tableview):
        sql_con = sql.connect('stock.db')
        self.stock_basic_data = rdb.read_stock_basic(sql_con)
        sql_con.close()
        
        stock_basic_len = len(self.stock_basic_data)
        self.model=QtGui.QStandardItemModel(stock_basic_len,2)
        self.model.setHorizontalHeaderLabels(['代码','名称'])
        for row in range(stock_basic_len):
            ts_code = self.stock_basic_data.ts_code.iloc[row]
            name = self.stock_basic_data.name.iloc[row]
            item_tscode=QtGui.QStandardItem(ts_code)
            item_name=QtGui.QStandardItem(name)
            self.model.setItem(row,0,item_tscode)
            self.model.setItem(row,1,item_name)
        
        tableview.setModel(self.model)
        