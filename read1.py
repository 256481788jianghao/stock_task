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
    sql_str='select * from daily where ts_code = "601878.SH" order by trade_date '
    data_daily = pd.read_sql_query(sql_str,sql_con,index_col='index')
    print(data_daily)
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
