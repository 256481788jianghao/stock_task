import porting as pt
import pandas as pd
import sqlite3 as sql
import readdb as rdb
import datetime
import matplotlib.pyplot as plt

pd.set_option('max_columns', 100)

sql_con = sql.connect('stock.db')
cursor = sql_con.cursor()

start_date = '20200301'
end_date = '20200305'
now_date = datetime.datetime.now().strftime('%Y%m%d')
try:
    print("start")
    stock_basic_data = rdb.read_stock_basic(sql_con)
    stock_basic_data = stock_basic_data[stock_basic_data.market != '科创板']
    stock_basic_data = stock_basic_data[stock_basic_data.list_date < '20190501']
    #data_stock_basic_sample = stock_basic_data.sample(frac=0.2)
    
    data_daily = rdb.read_daily_by_date(sql_con, start_date, end_date)
    data_daily_basic = rdb.read_daily_basic_by_date(sql_con, start_date, end_date)
    data_hk_hold = rdb.read_hk_hold_by_date(sql_con, start_date, end_date)
    data_hk_hold = data_hk_hold[data_hk_hold.exchange != 'HK']
    data_margin_detail = rdb.read_margin_detail_by_date(sql_con, start_date, end_date)
    
    #data_ans = pd.merge(data_hk_hold,stock_basic_data,on=)
    print(data_hk_hold)
    
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
