import porting as pt
import pandas as pd
import sqlite3 as sql
import readdb as rdb
import datetime
import matplotlib.pyplot as plt
import math
import scipy.stats as sci_ss

pd.set_option('max_columns', 100)

sql_con = sql.connect('stock.db')
cursor = sql_con.cursor()

start_date = '20181001'
end_date = '20181113'
now_date = datetime.datetime.now().strftime('%Y%m%d')
    
try:
    '''
    sum=68808 p=0.5381060341820718
    '''
    
    print((0.5381060341820718 - 0.5)/math.sqrt(0.5*0.5/68808))
    
    #ans = sci_ss.tt
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
