'''
Created on 2019年12月30日

@author: Administrator
'''

import tkinter as tk
from tkinter import ttk
from UIForm.UpdataForm import UpdataForm
from UIForm.StockBasicForm import  StockBasicFrom

class MainUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_w = 600
        self.window_h = 480
        self.geometry(str(self.window_w)+'x'+str(self.window_h))
        
        #菜单
        self.menubar=tk.Menu(self)
        self.fmenu1=tk.Menu(self,tearoff=0)
        for item in ['更新数据库']:
            self.fmenu1.add_command(label=item,command=self._show_updateform)
        self.menubar.add_cascade(label="命令",menu=self.fmenu1)
        self['menu']=self.menubar
        
        #基本数据
        self.stock_basic_frame = tk.Frame(self)
        stock_basic_form = StockBasicFrom(self.stock_basic_frame)
        stock_basic_form.grid()
        self.stock_basic_frame.pack(side='left')
    
    def _show_updateform(self):
        form = UpdataForm()
        form.mainloop()

if __name__ == '__main__':
    mainui = MainUI()
    mainui.mainloop()