import porting as pt
import pandas as pd
import sqlite3 as sql

sql_con = sql.connect('stock.db')
try:
    data = pt.stock_basic()
    print(data)
except e:
    print(e)
finally:
    print("end update")
    sql_con.close()
