'''
Created on 2019年10月25日

@author: Administrator
'''
import porting as pt
import pandas as pd
import sqlite3 as sql
import readdb as rdb
import datetime
import matplotlib.pyplot as plt
from tensorflow.python.grappler import item

pd.set_option('max_columns', 100)

sql_con = sql.connect('stock.db')
cursor = sql_con.cursor()

start_date = '20181001'
end_date = '20181113'
now_date = datetime.datetime.now().strftime('%Y%m%d')
try:
    '''
    stock_basic_data = rdb.read_stock_basic(sql_con)
    for ts_code in stock_basic_data.ts_code:
        print(ts_code)
        daily_basic_data = rdb.read_daily_basic_by_tscode(sql_con, ts_code)
        print(daily_basic_data.turnover_rate_f.rolling(5).mean())
        break
    '''
    data = rdb.read_stk_holdernumber(sql_con, now_date)
    data_min = data
    #print(data_min.ts_code)
    data_dailybasic = rdb.read_daily_basic_by_date(sql_con, '20191001', '20191027')
    #data_dailybasic = data_dailybasic.set_index('ts_code')
    #print(data_min)
    data_stock_basic = rdb.read_stock_basic(sql_con)
    print(len(data_stock_basic))
    for x in data_min.ts_code:
        if x not in list(data_stock_basic.ts_code):
            print(x)
    #print(data_dailybasic.merge(data_min,on='ts_code').groupby(by='ts_code').apply(lambda x:x.turnover_rate_f.mean()))
    #print(data_dailybasic[data_dailybasic.ts_code >= '688000.SH'])
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
