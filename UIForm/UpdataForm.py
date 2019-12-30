'''
Created on 2019年12月30日

@author: Administrator
'''
import tkinter as tk

class UpdataForm(tk.Tk):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        self.title('更新数据库界面')
        label1=tk.Label(self,text='开始时间:')
        label2=tk.Label(self,text='结束时间:')
        entry1 = tk.Entry(self)
        entry2 = tk.Entry(self)
        button = tk.Button(self,text='开 始',command=self._update)
        label1.grid(row=0,column=0)
        label2.grid(row=1,column=0)
        entry1.grid(row=0,column=1)
        entry2.grid(row=1,column=1)
        button.grid(row=2,columnspan=2)
    def _update(self):
        pass
    
if __name__ == '__main__':
    form = UpdataForm()
    form.mainloop()