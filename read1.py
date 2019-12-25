import porting as pt
import pandas as pd
import sqlite3 as sql
import readdb as rdb
import datetime
import matplotlib.pyplot as plt

pd.set_option('max_columns', 100)

sql_con = sql.connect('stock.db')
cursor = sql_con.cursor()

start_date = '20190101'
end_date = '20191220'
now_date = datetime.datetime.now().strftime('%Y%m%d')
try:
    print("start")
    stock_basic_data = rdb.read_stock_basic(sql_con)
    stock_basic_data = stock_basic_data[stock_basic_data.market != '科创板']
    stock_basic_data = stock_basic_data[stock_basic_data.list_date < '20190501']
    #data_stock_basic_sample = stock_basic_data.sample(frac=0.2)
    
    data_daily = rdb.read_daily_by_date(sql_con, start_date, end_date)
    data_daily_basic = rdb.read_daily_basic_by_date(sql_con, start_date, end_date)
    data_all = pd.merge(data_daily,data_daily_basic,on=['ts_code','trade_date'])
    #print(data_all)
    data_daily_10 = data_all #[data_all['pct_change'] >= 10]
    def lambda_fun(item):
        item_filter = pd.merge(item,stock_basic_data,on='ts_code')
        #median_total_share = item_filter.total_share.median();
        #item_filter = item_filter[item_filter.total_share < median_total_share*0.8]
        sub_item_10 = item_filter[item_filter['pct_change'] > 9]
        #print(sub_item_10)
        return pd.Series({'Len_r':len(sub_item_10)/len(item_filter),'Len_filter':len(item_filter),'p10_mean':sub_item_10.total_share.mean(),'p10_std':sub_item_10.total_share.std(),'p10_median':sub_item_10.total_share.median(),'p_median':item_filter.total_share.median()})
    data_ans = data_daily_10.groupby(by='trade_date').apply(lambda_fun)
    data_ans['r'] = data_ans.p10_median/data_ans.p_median
    print(data_ans)
    print(data_ans.r.mean())
    print(data_ans.r.median())
    plt.bar(data_ans.index,data_ans.Len_r)
    plt.show()
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
