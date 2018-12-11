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
    sql_str='select a.ts_code,a.trade_date,a.low,b.turnover_rate_f,b.free_share from daily a,daily_basic b \
             where a.ts_code = "'+ts_code+'"\
             and a.ts_code = b.ts_code and a.trade_date = b.trade_date'
    #sql_str = 'select * from daily'
    data_daily = pd.read_sql_query(sql_str,sql_con)
    #print(data_daily)
    p_mean = []
    p_mean.append(1)
    def func(item):
        print(item.free_share)
        p_mean.append(p_mean[-1]*(1-item.turnover_rate_f/100)+item.low*item.turnover_rate_f/100)
    data_daily.apply(func,axis=1)
    del p_mean[0]
    data_daily['p_mean'] = p_mean
    print(data_daily)
    data_daily.plot(y=['low','p_mean'])
    plt.show()
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
