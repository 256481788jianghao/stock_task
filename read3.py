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
    cmd = '''select stock_basic.ts_code,stock_basic.name,stock_basic.industry,daily_basic.trade_date,daily_basic.turnover_rate_f, daily.pct_change,stock_basic.list_date from stock_basic,daily_basic,daily 
             where stock_basic.ts_code = daily_basic.ts_code and stock_basic.ts_code = daily.ts_code and daily_basic.trade_date = "20190920" and daily.trade_date = daily_basic.trade_date and daily.pct_change >= 9
             and stock_basic.list_date < 20190101'''
    
    data = pd.read_sql_query(cmd,sql_con)
    print(data)
    
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
