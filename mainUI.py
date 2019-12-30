'''
Created on 2019年12月30日

@author: Administrator
'''

import tkinter as tk
from tkinter import ttk
from UIForm.UpdataForm import UpdataForm

class MainUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.menubar=tk.Menu(self)
        self.fmenu1=tk.Menu(self,tearoff=0)
        for item in ['更新数据库']:
            # 如果该菜单时顶层菜单的一个菜单项，则它添加的是下拉菜单的菜单项。
            self.fmenu1.add_command(label=item,command=self._show_updateform)
         
        # add_cascade 的一个很重要的属性就是 menu 属性，它指明了要把那个菜单级联到该菜单项上，
        # 当然，还必不可少的就是 label 属性，用于指定该菜单项的名称
        self.menubar.add_cascade(label="命令",menu=self.fmenu1)
        self['menu']=self.menubar
    
    def _show_updateform(self):
        form = UpdataForm()
        form.mainloop()

if __name__ == '__main__':
    mainui = MainUI()
    mainui.mainloop()