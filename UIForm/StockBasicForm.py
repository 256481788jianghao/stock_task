'''
Created on 2019年12月30日

@author: Administrator
'''
from tkinter import ttk

class StockBasicFrom(object):
    '''
    classdocs
    '''


    def __init__(self, root):
        self.tree=ttk.Treeview(root)#表格
        self.tree["columns"]=("姓名","年龄","身高")
        self.tree.column("姓名")
        self.tree.column("年龄")
        self.tree.column("身高")
         
        self.tree.heading("姓名",text="姓名-name")  #显示表头
        self.tree.heading("年龄",text="年龄-age")
        self.tree.heading("身高",text="身高-tall")
         
        self.tree.insert("",0,text="line1" ,values=("1","2","3")) #插入数据，
        self.tree.insert("",1,text="line1" ,values=("1","2","3"))
        self.tree.insert("",2,text="line1" ,values=("1","2","3"))
        self.tree.insert("",3,text="line1" ,values=("1","2","3"))
    def pack(self):
        self.tree.pack()
    def grid(self):
        self.tree.grid()