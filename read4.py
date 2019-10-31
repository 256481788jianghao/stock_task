'''
Created on 2019年10月25日

@author: Administrator
'''
import math
import porting as pt
import pandas as pd
import sqlite3 as sql
import readdb as rdb
import datetime
import matplotlib.pyplot as plt
import scipy.stats as sci_ss
#from tensorflow.python.grappler import item

pd.set_option('max_columns', 100)

sql_con = sql.connect('stock.db')
cursor = sql_con.cursor()

start_date = '20190101'
end_date = '20191113'
now_date = datetime.datetime.now().strftime('%Y%m%d')
try:
    data_stock_basic = rdb.read_stock_basic(sql_con)
    data_stock_basic = data_stock_basic[data_stock_basic.market != '科创板']
    data_stock_basic = data_stock_basic[data_stock_basic.list_date < '20190501']
    print(len(data_stock_basic))
    
    data_dailybasic = rdb.read_daily_basic_by_date(sql_con, start_date, end_date)
    print(len(data_dailybasic))
    data_daily = rdb.read_daily_by_date(sql_con, start_date, end_date)
    print(len(data_daily))
    data_merge = data_dailybasic.merge(data_daily,on=['trade_date','ts_code'])
    data_merge = data_merge.merge(data_stock_basic,on='ts_code')
    print(len(data_merge))
    data_merge_group = data_merge.groupby(by='ts_code')
    def lam_fun(item):
        item['id_index'] = range(0,len(item))
        pItem = item[(item['pct_change'] > 3)]
        sum_num = len(pItem)
        collect_num = 0
        for index in pItem.id_index:
            subitem = item[(item.id_index > index) & (item.id_index <= index+5)]
            if len(subitem) == 0:
                sum_num = sum_num -1
                continue
            curItem = item[item.id_index == index]
            #print(curItem)
            diff_p = (subitem.high - curItem.high.iloc[0])*100/curItem.high.iloc[0]
            #print(diff_p)
            if len(diff_p[diff_p > 2]) > 1:
                collect_num = collect_num + 1
            #prod_ans = (subitem['pct_change']/100+1).cumprod()
            #print(len(prod_ans[prod_ans > 1]))
            #if len(prod_ans[prod_ans > 1]) > 1:
            #    collect_num = collect_num + 1
        return pd.Series({'len':len(item),'sum_n':sum_num,'collect_n':collect_num})
    data_ans = data_merge_group.apply(lam_fun)
    all_sum = data_ans.sum_n.sum()
    all_collect = data_ans.collect_n.sum()
    print("sum="+str(all_sum)+'c='+str(all_collect)+" p="+str(all_collect/all_sum))
    data_list = []
    for i in range(0,all_sum):
        if i < all_collect:
            data_list.append(1)
        else:
            data_list.append(0)
    stats_ans = sci_ss.ttest_1samp(data_list, 0.5)
    print('=========stats_ans======')
    print(stats_ans)
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
