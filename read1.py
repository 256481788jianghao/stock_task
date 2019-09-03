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
    data =rdb.read_daily_basic_by_date(sql_con,'20190719','20190719')
    datal5 = data[data.turnover_rate_f < 2]
    data5 = data[(data.turnover_rate_f >= 2) & (data.turnover_rate_f < 5)]
    data10 = data[(data.turnover_rate_f >= 5) & (data.turnover_rate_f < 20)]
    data20 = data[(data.turnover_rate_f >= 20) & (data.turnover_rate_f < 30)]
    data30 = data[(data.turnover_rate_f >= 30) ]
    print('dl5 len:'+str(len(datal5))+' mean_circ:'+str(datal5.circ_mv.sum()/len(datal5)))
    print('d5 len:'+str(len(data5))+' mean_circ:'+str(data5.circ_mv.sum()/len(data5)))
    print('d10 len:'+str(len(data10))+' mean_circ:'+str(data10.circ_mv.sum()/len(data10)))
    print('d20 len:'+str(len(data20))+' mean_circ:'+str(data20.circ_mv.sum()/len(data20)))
    print('d30 len:'+str(len(data30))+' mean_circ:'+str(data30.circ_mv.sum()/len(data30)))
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
