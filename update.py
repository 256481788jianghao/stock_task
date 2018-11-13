import porting as pt
import pandas as pd
import sqlite3 as sql

sql_con = sql.connect('stock.db')
try:
    print('start update stock basic')
    data = pt.stock_basic()
    if type(data) == pd.DataFrame:
        data.to_sql('stock_basic',sql_con,if_exists='replace')
    else:
        print('get stock_basic faild')
except Exception as e:
    print(e)
finally:
    print("end update")
    sql_con.close()
