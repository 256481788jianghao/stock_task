import porting as pt
import pandas as pd
import sqlite3 as sql
import readdb as rdb
import datetime
import matplotlib.pyplot as plt
import math
import scipy.stats as sci_ss
from readdb import read_daily_by_date
from _pytest.nodes import Item

pd.set_option('max_columns', 100)

sql_con = sql.connect('stock.db')
cursor = sql_con.cursor()

start_date = '20170101'
end_date = '20191113'
now_date = datetime.datetime.now().strftime('%Y%m%d')
    
try:
    income_report_str = "select ts_code,end_date,update_flag,ann_date,f_ann_date,compr_inc_attr_p,n_income_attr_p from income_report"
    def filter_fun(item):
        if len(item) > 1:
            #print(item)
            subItem = item[item.update_flag == '1']
            #print('===============')
            #print(subItem)
            return subItem.iloc[0]
        return item.iloc[0]
    data_income_report = pd.read_sql_query(income_report_str,sql_con).groupby(by=['ts_code','end_date']).apply(filter_fun)
    data_income_report = data_income_report.set_index('ts_code')
    
    data_daily = read_daily_by_date(sql_con,start_date,end_date)
    print('=======daily================')
    #data_daily_dict = dict()
    #def filter_daily(item):
        #print(item)
        #tscode = item.ts_code.iloc[0]
        #data_daily_dict[tscode] = item
        #print(item)
    #data_daily.groupby(by='ts_code').apply(filter_daily)
    #print(data_daily_dict['000001.SZ'])
    #print(data_daily[data_daily.trade_date < '20171231'])
    data_stock_basic = rdb.read_stock_basic(sql_con)
    data_stock_basic = data_stock_basic[data_stock_basic.market != '科创板']
    data_stock_basic = data_stock_basic[data_stock_basic.list_date < '20190501']
    data_stock_basic_sample = data_stock_basic.sample(frac=0.02)
    ts_code_list = data_stock_basic_sample.ts_code.tolist()
    def filter_find_p(item):
        #print(item.compr_inc_attr_p.diff(1))
        #print(item.compr_inc_attr_p.diff(1)*100/item.compr_inc_attr_p.shift(1))
        prect_change = item.compr_inc_attr_p.diff(1)*100/item.compr_inc_attr_p.shift(1)
        subItem = item[(prect_change > 0) & (prect_change < 4000)]
        tscode = item.index[0]
        if not (tscode in ts_code_list):
            return
        ans_dict = dict()
        ans_dict['code'] = tscode
        ans_dict['date'] = []
        ans_dict['tail1_len'] = []
        ans_dict['tail1'] = []
        ans_dict['tail2_len'] = []
        ans_dict['tail2'] = []
        if len(subItem) == 0:
            return
        else:
            for date in subItem.f_ann_date:
                time1 = datetime.datetime.now()
                data_daily_items = data_daily[(data_daily.ts_code == tscode)]
                data_daily_items = data_daily_items[data_daily_items.trade_date <= date]
                #data_daily_items = data_daily_dict[tscode]
                #print(data_daily_items)
                #data_daily_items = data_daily_items[data_daily_items.trade_date <= date]
                time2 = datetime.datetime.now()
                data_daily_sort = data_daily_items.sort_values(by='trade_date')
                data_daily_tail1 = data_daily_sort.tail(5)
                data_daily_tail2 = data_daily_sort.tail(150).head(30)
                ans_dict['date'].append(date)
                ans_dict['tail1_len'].append(len(data_daily_tail1))
                ans_dict['tail2_len'].append(len(data_daily_tail2))
                ans_dict['tail1'].append(data_daily_tail1.close.mean())
                ans_dict['tail2'].append(data_daily_tail2.close.mean())
                #print(time2 - time1)
        #print(ans_dict)
        return pd.DataFrame(ans_dict)
    print('=======last================')
    data_income_report_date = data_income_report.groupby(by='ts_code').apply(filter_find_p)
    print(data_income_report_date)
    all_data_len = len(data_income_report_date)
    collect_data_len = len(data_income_report_date[data_income_report_date.tail1 > data_income_report_date.tail2])
    print(collect_data_len/all_data_len)
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
