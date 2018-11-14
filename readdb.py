import pandas as pd

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

def find_date_need_update(con,sdate,edate):
    sql_str='select cal_date from trade_cal'
    data = pd.read_sql_query(sql_str,con,index_col='index')
    return data
