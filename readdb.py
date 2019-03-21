import pandas as pd
from _overlapped import NULL

def read_tables_info(con):
    data = pd.read_sql_query('select * from tables_info',con,index_col='index')
    return data

def is_table_exists(cursor,table_name):
    cursor.execute('select count(*)  from sqlite_master where type="table" and name="'+table_name+'"')
    values = cursor.fetchall()
    #print(values[0][0])
    return values[0][0] == 1

def table_info(cursor,table_name):
    cursor.execute('pragma table_info("'+table_name+'")')
    values = cursor.fetchall()
    print(values)

def read_trade_cal(con):
    data = pd.read_sql_query('select * from trade_cal',con,index_col='index')
    return data

def read_daily_by_date(con,sdate,edate):
    sql_str = 'select * from daily where trade_date >= "'+sdate+'" and trade_date <= "'+edate+'"'
    data = pd.read_sql_query(sql_str,con,index_col='index')
    return data

def read_daily_basic_by_date(con,sdate,edate):
    sql_str = 'select * from daily_basic where trade_date >= "'+sdate+'" and trade_date <= "'+edate+'"'
    data = pd.read_sql_query(sql_str,con,index_col='index')
    return data

def read_daily_by_date_and_tscode(con,tscode,sdate,edate):
    sql_str = 'select * from daily where ts_code="'+tscode+'" and trade_date >= "'+sdate+'" and trade_date <= "'+edate+'"'
    data = pd.read_sql_query(sql_str,con,index_col='trade_date')
    return data

def find_date_need_update(con,sdate,edate):
    sql_str='select cal_date from trade_cal where is_open = 1 and cal_date >="'+sdate+'" and cal_date <="'+edate+'" and (cal_date not in (select trade_date from daily) or cal_date not in (select trade_date from daily_basic))'
    data = pd.read_sql_query(sql_str,con)
    return data

def find_date_need_update_daily(con,sdate,edate):
    sql_str='select cal_date from trade_cal where is_open = 1 and cal_date >="'+sdate+'" and cal_date <="'+edate+'" and cal_date not in (select trade_date from daily)'
    data = pd.read_sql_query(sql_str,con)
    return data

def find_date_need_update_daily_basic(con,sdate,edate):
    sql_str='select cal_date from trade_cal where is_open = 1 and cal_date >="'+sdate+'" and cal_date <="'+edate+'" and cal_date not in (select trade_date from daily_basic)'
    data = pd.read_sql_query(sql_str,con)
    return data

def find_date_need_update_adj_factor(con,sdate,edate):
    sql_str='select cal_date from trade_cal where is_open = 1 and cal_date >="'+sdate+'" and cal_date <="'+edate+'" and cal_date not in (select trade_date from adj_factor)'
    data = pd.read_sql_query(sql_str,con)
    return data

def find_date_need_update_block_trade(con,sdate,edate):
    try:
        sql_str='select cal_date from trade_cal where is_open = 1 and cal_date >="'+sdate+'" and cal_date <="'+edate+'" and cal_date not in (select trade_date from block_trade)'
        data = pd.read_sql_query(sql_str,con)
    except Exception as e:
        print("ex:"+str(e))
        return None
    return data

def find_date_need_update_stock_suspend(con,sdate,edate):
    try:
        sql_str='select cal_date from trade_cal where is_open = 1 and cal_date >="'+sdate+'" and cal_date <="'+edate+'" and cal_date not in (select suspend_date from stock_suspend)'
        data = pd.read_sql_query(sql_str,con)
    except Exception as e:
        print("ex:"+str(e))
        return None
    return data

def read_stock_basic_by_name(con,name):
    sql_str='select * from stock_basic where name="'+name+'"'
    data = pd.read_sql_query(sql_str,con)
    return data
    
