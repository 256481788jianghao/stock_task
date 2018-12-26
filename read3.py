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
    stock_basic_data = pd.read_sql_query('select * from stock_basic where list_date < 20180901',sql_con)
    daily_data = rdb.read_daily_by_date(sql_con,'20180101','20181225')
    dailybasic_data = rdb.read_daily_basic_by_date(sql_con,'20180101','20181225')
    print(dailybasic_data)
    daily_group = daily_data.groupby(by='ts_code')
    def func(item):
        pass
    ans = daily_group.apply(func)
    
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
