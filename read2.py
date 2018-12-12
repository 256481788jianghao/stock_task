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

def smrate(data,n):
    if len(data) < n:
        return 0
    else:
        subdata = data
        return (subdata.iloc[-1] - subdata.mean())/subdata.std()
        
def smrate_l(data_list,n):
    data_len = len(data_list)
    ans_list = []
    for i in range(0,data_len - n + 1):
        #print(data_list[i:i+n])
        ans_list.append(smrate(data_list[i:i+n],n))
    return pd.DataFrame({'smrate':ans_list})

def smrate_with_other(data,n):
    smrate_list = smrate_l(data.vol,n)
    subdata = data[n-1:len(data)+1]
    print(smrate_list.smrate)
    print(subdata)
    print(pd.concat([subdata,smrate_list],axis=1))
    
try:
    stock_basic_data = rdb.read_stock_basic_by_name(sql_con,'中信建投')
    ts_code = stock_basic_data.ts_code.iloc[0]
    sql_str='select trade_date,vol from daily where ts_code="'+ts_code+'"'
    data_daily = pd.read_sql_query(sql_str,sql_con)
    data_sort = data_daily.sort_values(by='trade_date')
    smrate_with_other(data_sort,7)
    
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
