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
    stock_basic_data = rdb.read_stock_basic_by_name(sql_con,'浙商证券')
    ts_code = stock_basic_data.ts_code.iloc[0]
    sql_str='select * from daily where ts_code="'+ts_code+'"'
    data_daily = pd.read_sql_query(sql_str,sql_con)
    print(data_daily.sort_values(by='trade_date'))
    
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
