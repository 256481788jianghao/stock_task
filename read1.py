import porting as pt
import pandas as pd
import sqlite3 as sql
import readdb as rdb
import datetime
import matplotlib.pyplot as plt

pd.set_option('max_columns', 100)

sql_con = sql.connect('stock.db')
cursor = sql_con.cursor()

start_date = '20180101'
end_date = '20191101'
now_date = datetime.datetime.now().strftime('%Y%m%d')
try:
    stock_basic_data = rdb.read_stock_basic(sql_con)
    stock_basic_data = stock_basic_data[stock_basic_data.market != '科创板']
    stock_basic_data = stock_basic_data[stock_basic_data.list_date < '20190501']
    data_stock_basic_sample = stock_basic_data.sample(frac=0.2)
    
    data_daily = rdb.read_daily_by_date(sql_con, start_date, end_date)
    
    def lam_fun(item):
        tscode = item.ts_code.iloc[0]
        data_daily_tscode = data_daily[data_daily.ts_code == tscode]
        data_daily_select = data_daily_tscode[data_daily_tscode.shift(-2).high > (data_daily_tscode.close*1.005)]
        return pd.Series({'all_len':len(data_daily_tscode),'s_len':len(data_daily_select)})
    data_ans = data_stock_basic_sample.groupby(by='ts_code').apply(lam_fun)
    data_ans['rate'] = data_ans.s_len/data_ans.all_len
    print(data_ans)
    print(data_ans.rate.mean())
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
