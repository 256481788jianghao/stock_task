'''
Created on 2019年12月30日

@author: Administrator
'''
import tkinter as tk
import tkinter.messagebox
import update as up
import threading 

class UpdataForm(tk.Tk):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        self.title('更新数据库界面')
        label1=tk.Label(self,text='开始时间:')
        label2=tk.Label(self,text='结束时间:')
        self.entry1 = tk.Entry(self)
        self.entry2 = tk.Entry(self)
        button = tk.Button(self,text='开 始',command=self._update)
        label1.grid(row=0,column=0)
        label2.grid(row=1,column=0)
        self.entry1.grid(row=0,column=1)
        self.entry2.grid(row=1,column=1)
        button.grid(row=2,columnspan=2)
    def _update(self):
        stime = self.entry1.get()
        etime = self.entry2.get()
        if len(stime) == 0 or len(etime) == 0:
            tk.messagebox.askokcancel('温馨提示', "stime etime is null")
            return
        t = threading.Thread(target=self._updateThreadFun,args=(stime,etime))
        t.daemon = True
        t.start()
    def _updateThreadFun(self,starttime,endtime):
        print('update s='+starttime+' e='+endtime)
        up.UpdateFunction(starttime, endtime)
    
if __name__ == '__main__':
    form = UpdataForm()
    form.mainloop()