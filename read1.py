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
end_date = '20200409'
now_date = datetime.datetime.now().strftime('%Y%m%d')
try:
    print("start")
    market_names = ['CFFEX','DCE','CZCE','SHFE','INE']
    
    fut_basic_data = rdb.read_fut_basic(sql_con,'豆一2005')
    
    for symbol in fut_basic_data.symbol:
        #fut_daily_data = rdb.read_fut_daily_by_tscode(sql_con,ts_code)
        #print(fut_daily_data)
        fut_holding_data = rdb.read_fut_holding_by_symbol(sql_con,symbol)
        print(fut_holding_data)
        #plt.plot(fut_daily_data.trade_date,fut_daily_data.close)
        #plt.show()
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
