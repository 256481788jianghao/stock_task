import porting as pt
import pandas as pd
import sqlite3 as sql
import readdb as rdb
import datetime

pd.set_option('max_columns', 100)

sql_con = sql.connect('stock.db')
cursor = sql_con.cursor()

start_date = '20170101'
end_date = '20190119'
now_date = datetime.datetime.now().strftime('%Y%m%d')

tables_info = None

try:
    if rdb.is_table_exists(cursor,'tables_info'):
        tables_info = rdb.read_tables_info(sql_con)
    else:
        tables_info = pd.DataFrame()
        tables_info['stock_basic_info'] = [start_date]
        tables_info['trade_cal_info'] = [start_date]

    if tables_info['stock_basic_info'].iloc[0] != now_date:
        print('start update stock basic')
        data_stock_basic = pt.stock_basic()
        if type(data_stock_basic) == pd.DataFrame:
            data_stock_basic.to_sql('stock_basic',sql_con,if_exists='replace')
            tables_info['stock_basic_info'] = [now_date]
        else:
            print('get stock_basic faild')

    if tables_info['trade_cal_info'].iloc[0] != now_date:
        print('start update trade cal')
        data_trade_cal = pt.trade_cal()
        if type(data_trade_cal) == pd.DataFrame:
            data_trade_cal.to_sql('trade_cal',sql_con,if_exists='replace')
            tables_info['trade_cal_info'] = [now_date]
        else:
            print('get trade_cal faild')
    
    tables_info.to_sql('tables_info',sql_con,if_exists='replace')
    #print(tables_info)
    
    print('start update daily')
    trade_cal_need_update = None
    if rdb.is_table_exists(cursor,'daily'):
        print('append daily table')
        trade_cal_need_update_daily = rdb.find_date_need_update_daily(sql_con,start_date,end_date)
        trade_cal_need_update_daily_basic = rdb.find_date_need_update_daily_basic(sql_con,start_date,end_date)
        trade_cal_need_update_adj_factor = rdb.find_date_need_update_adj_factor(sql_con,start_date,end_date)
        trade_cal_need_update_block_trade = rdb.find_date_need_update_block_trade(sql_con,start_date,end_date)
        print('need update:')
        print(trade_cal_need_update)
        
    else:
        print('create daily table')
        trade_cal_db = rdb.read_trade_cal(sql_con)
        trade_cal_open = trade_cal_db[(trade_cal_db.is_open == 1) & (trade_cal_db.cal_date <= end_date) & (trade_cal_db.cal_date >= start_date)]
        #print(trade_cal_open)
        trade_cal_need_update_daily = trade_cal_open
        trade_cal_need_update_daily_basic = trade_cal_open
        trade_cal_need_update_adj_factor = trade_cal_open
        trade_cal_need_update_block_trade = trade_cal_open

    for item in trade_cal_need_update_block_trade.cal_date:
        print('update block_trade '+str(item))
        data_block_trade = pt.block_trade(item)
        if type(data_block_trade) == pd.DataFrame and not data_block_trade.empty:
            data_block_trade.to_sql('block_trade',sql_con,if_exists='append')
        elif data_block_trade.empty:
            print('update block_trade empty '+str(item))
        else:
            print('update block_trade fail '+str(item))

    
    for item in trade_cal_need_update_daily.cal_date:
        print('update daily:'+str(item))
        data = pt.daily(item)
        data = data.rename(columns = {'pct_chg':'pct_change'})
        #print(data)
        if type(data) == pd.DataFrame and not data.empty:
            data.to_sql('daily',sql_con,if_exists='append')
        else:
            print('update daily:'+str(item)+' fail')

    for item in trade_cal_need_update_daily_basic.cal_date:
        print('update daily_basic:'+str(item))
        data_daily_basic = pt.daily_basic(item)
        if type(data_daily_basic) == pd.DataFrame and not data_daily_basic.empty:
            data_daily_basic.to_sql('daily_basic',sql_con,if_exists='append')
        else:
            print('update daily_basic:'+str(item)+' fail')

    for item in trade_cal_need_update_adj_factor.cal_date:
        print('update adj_factor:'+str(item))
        data_adj_factor = pt.adj_factor(item)
        if type(data_adj_factor) == pd.DataFrame and not data_adj_factor.empty:
            data_adj_factor.to_sql('adj_factor',sql_con,if_exists='append')
        else:
            print('update adj_factor:'+str(item)+' fail')
    
            
except Exception as e:
    print("ex:"+str(e))
finally:
    print("end update")
    cursor.close()
    sql_con.close()
