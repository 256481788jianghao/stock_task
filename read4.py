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

pd.set_option('max_columns', 100)

sql_con = sql.connect('stock.db')
cursor = sql_con.cursor()

start_date = '20181001'
end_date = '20181113'
now_date = datetime.datetime.now().strftime('%Y%m%d')
try:
    stock_basic_data = rdb.read_stock_basic(sql_con)
    for ts_code in stock_basic_data.ts_code:
        print(ts_code)
        daily_basic_data = rdb.read_daily_basic_by_tscode(sql_con, ts_code)
        print(daily_basic_data.turnover_rate_f.rolling(5).min())
        break
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
