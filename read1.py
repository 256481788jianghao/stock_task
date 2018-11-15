import porting as pt
import pandas as pd
import sqlite3 as sql
import readdb as rdb
import datetime

sql_con = sql.connect('stock.db')
cursor = sql_con.cursor()

start_date = '20181001'
end_date = '20181113'
now_date = datetime.datetime.now().strftime('%Y%m%d')
try:
    print(rdb.read_stock_basic_by_name(sql_con,'中信建投'))
    sql_str='select ts_code,pct_change from daily where trade_date >="20181112" and pct_change > 9.9'
    data_daily = pd.read_sql_query(sql_str,sql_con)
    print(data_daily)
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
