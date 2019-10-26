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
    stock_basic_data = rdb.read_stock_basic(sql_con)
    for ts_code in stock_basic_data.ts_code:
        print(ts_code)
        money_flow_data = rdb.read_money_flow(sql_con, ts_code)
        daily_data = rdb.read_daily_by_tscode(sql_con, ts_code)
        #print(daily_data[daily_data.trade_date == '20170124'])
        data_merge = money_flow_data.merge(daily_data,on='trade_date').set_index('trade_date')
        #data_all_amount = (data.buy_sm_amount+data.sell_sm_amount+data.buy_md_amount+data.sell_md_amount+data.buy_lg_amount+data.sell_lg_amount+data.buy_elg_amount+data.sell_elg_amount)
        #data_all_amount = (data.buy_sm_vol+data.buy_md_vol+data.buy_lg_vol+data.buy_elg_vol)
        #data_ans = (data_all_amount/data.vol)
        #print(data_ans[data_ans<0.95])
        def lam_fun(data):
            #ans_dict = dict()
            data_all_amount = (data.buy_sm_vol+data.buy_md_vol+data.buy_lg_vol+data.buy_elg_vol)
            data_k_vol = (data.buy_sm_vol+data.buy_md_vol+data.buy_lg_vol+data.buy_elg_vol)-(data.sell_sm_vol+data.sell_md_vol+data.sell_lg_vol+data.sell_elg_vol)
            data_k_vol2 = (data.buy_elg_vol)-(data.sell_elg_vol)
            #ans_dict['rate']=(data_all_amount/data.vol)
            #ans_dict['trade_date'] = data.trade_date
            #return pd.DataFrame(ans_dict)
            return pd.Series({'rate':(data_all_amount/data.vol),'be':data.buy_elg_vol,'bl':data.buy_lg_vol,'bm':data.buy_md_vol,'bs':data.buy_sm_vol,'vol':data.vol,'net':data.net_mf_vol,'mynet':data_k_vol,'mynet2':data_k_vol2})
        data_ans = data_merge.apply(lam_fun,axis=1)
        print(data_ans[data_ans.rate < 0.9])
        break
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end execute")
    cursor.close()
    sql_con.close()
