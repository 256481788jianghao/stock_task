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
    daily_data = rdb.read_daily_by_date(sql_con,'20180101','20181224')
    daily_group = daily_data.groupby(by='ts_code')
    def func(item):
        #print(item)
        sublist = item[item['pct_change'] > 2]
        sublist2 = item[item['pct_change'] < -2]
        item['rhp'] = (item.high - item.open)/item.open*100
        item['rlp'] = (item.low - item.open)/item.open*100
        sublist3 = item[item.rhp > 5]
        sublist4 = item[item.rlp < -5]
        return pd.Series({'rh5':len(sublist3),'rl5':len(sublist4),'b5':len(sublist),'rb5':len(sublist)/len(item)*100,'s5':len(sublist2),'b5s5':len(sublist)/(len(sublist2)+0.0001)*100})
    ans = daily_group.apply(func)
    ans2 = stock_basic_data.set_index('ts_code').loc[:,['name','list_date']]
    ans2['b5'] = ans.b5
    ans2['rb5'] = ans.rb5
    ans2['s5'] = ans.s5
    ans2['b5s5'] = ans.b5s5
    ans2['rh5'] = ans.rh5
    ans2['rl5'] = ans.rl5
    print(ans2[ans2.rb5 > 0].sort_values(by='b5'))
    print(ans2.rh5.median())
    print(ans2.rh5.mean())
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
