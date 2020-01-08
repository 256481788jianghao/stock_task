'''
Created on 2020年1月6日

@author: Administrator
'''

from PyQt5 import QtGui
import sqlite3 as sql
import readdb as rdb
import pandas as pd

class StockBasicModle(object):
    '''
    classdocs
    '''


    def __init__(self, tableview):
        sql_con = sql.connect('stock.db')
        self.stock_basic_data = rdb.read_stock_basic(sql_con)
        self.subData = self.stock_basic_data
        self.concept_info = rdb.read_concept_info(sql_con)
        self.concept_detail = rdb.read_concept_detail(sql_con)
        sql_con.close()
        
        stock_basic_len = len(self.stock_basic_data)
        self.model=QtGui.QStandardItemModel(stock_basic_len,2)
        self.UpdateFilter()
        
        tableview.setModel(self.model)
        
    def Init_Concept_ComboBox(self,ui_comboBox):
        length = len(self.concept_info)
        ui_comboBox.addItem('all')
        for row in range(length):
            concept_item = self.concept_info.iloc[row]
            #print(type(concept_item['name']))
            ui_comboBox.addItem(concept_item['name'])
    
    def ResetStockBasic(self):
        self.subData = self.stock_basic_data
        
    def FilterByConcept(self,concept_name):
        print('FilterByConcept '+concept_name)
        if concept_name == 'all':
            return
        concept_list = self.concept_detail[self.concept_detail['concept_name'] == concept_name]
        #print(concept_list)
        if len(concept_list) >0 and type(self.subData) == pd.DataFrame:
            self.subData = self.subData[self.subData.ts_code.isin(concept_list.ts_code)]
            
    def FilterByIndustry(self,patten):
        if type(self.subData) == pd.DataFrame:
            print('FilterByIndustry '+patten)
            if len(patten) > 0:
                def subfun(item):
                    if item is not None:
                        return item.find(patten) >= 0
                    else:
                        return False
                self.subData = self.subData[self.subData.industry.apply(subfun)]
            
    def FilterByName(self,patten):
        if type(self.subData) == pd.DataFrame:
            print('FilterByName '+patten)
            if len(patten) > 0:
                def subfun(item):
                    return item.find(patten) >= 0
                self.subData = self.subData[self.subData.name.apply(subfun)]
            else:
                pass
        
    def UpdateFilter(self,hasKechuangban=True,listdate='20200101'):
        if type(self.subData) == pd.DataFrame:
            self.model.clear()
            self.model.setHorizontalHeaderLabels(['代码','名称','行业'])
            if hasKechuangban:
                pass
            else:
                self.subData = self.subData[self.subData.market != '科创板']
                
            self.subData = self.subData[self.subData.list_date <= listdate]
            
            
            stock_basic_len = len(self.subData)
            #print(self.subData)
            #print(stock_basic_len)
            for row in range(stock_basic_len):
                ts_code = self.subData.ts_code.iloc[row]
                name = self.subData.name.iloc[row]
                industry = self.subData.industry.iloc[row]
                item_tscode=QtGui.QStandardItem(ts_code)
                item_name=QtGui.QStandardItem(name)
                item_industry=QtGui.QStandardItem(industry)
                self.model.setItem(row,0,item_tscode)
                self.model.setItem(row,1,item_name)
                self.model.setItem(row,2,item_industry)
            
    def GetData(self,row):
        return self.subData.iloc[row]