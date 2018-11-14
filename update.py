import porting as pt
import pandas as pd
import sqlite3 as sql
import readdb as rdb
import datetime

sql_con = sql.connect('stock.db')
cursor = sql_con.cursor()

start_date = '20181110'
end_date = '20181112'
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
    #trade_cal_db = rdb.read_trade_cal(sql_con)
    #trade_cal_open = trade_cal_db[(trade_cal_db.is_open == 1) & (trade_cal_db.cal_date <= end_date) & (trade_cal_db.cal_date >= start_date)]
    #print(trade_cal_open)
    trade_cal_need_update = None
    if rdb.is_table_exists(cursor,'daily'):
        print('append daily table')
        trade_cal_need_update = rdb.find_date_need_update(sql_con,start_date,end_date)
        print(trade_cal_need_update)
        
    else:
        print('create daily table')
        trade_cal_need_update = trade_cal_open

    for item in trade_cal_need_update.cal_date:
        data = pt.daily(item)
        if type(data) == pd.DataFrame and not data.empty:
            data.to_sql('daily',sql_con,if_exists='append')
            
except Exception as e:
    print(e)
finally:
    print("end update")
    cursor.close()
    sql_con.close()
