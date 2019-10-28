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

def read_daily_by_tscode(con,tscode):
    sql_str = 'select * from daily where ts_code="'+tscode+'"'
    data = pd.read_sql_query(sql_str,con)
    return data

def read_daily_basic_by_date(con,sdate,edate):
    sql_str = 'select * from daily_basic where trade_date >= "'+sdate+'" and trade_date <= "'+edate+'"'
    data = pd.read_sql_query(sql_str,con,index_col='index')
    return data

def read_daily_by_date_and_tscode(con,tscode,sdate,edate):
    sql_str = 'select * from daily where ts_code="'+tscode+'" and trade_date >= "'+sdate+'" and trade_date <= "'+edate+'"'
    data = pd.read_sql_query(sql_str,con,index_col='trade_date')
    return data

def read_daily_basic_by_tscode(con,tscode):
    sql_str = 'select * from daily_basic where ts_code="'+tscode+'"'
    data = pd.read_sql_query(sql_str,con)
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

def find_date_need_update_longhubang_list(con,sdate,edate):
    try:
        sql_str='select cal_date from trade_cal where is_open = 1 and cal_date >="'+sdate+'" and cal_date <="'+edate+'" and cal_date not in (select trade_date from longhubang_list)'
        data = pd.read_sql_query(sql_str,con)
    except Exception as e:
        print("ex:"+str(e))
        return None
    return data

def find_date_need_update_money_flow(con,sdate,edate):
    try:
        sql_str='select cal_date from trade_cal where is_open = 1 and cal_date >="'+sdate+'" and cal_date <="'+edate+'" and cal_date not in (select trade_date from money_flow)'
        data = pd.read_sql_query(sql_str,con)
    except Exception as e:
        print("ex:"+str(e))
        return None
    return data

def find_date_need_update_stock_limit_price(con,sdate,edate):
    try:
        sql_str='select cal_date from trade_cal where is_open = 1 and cal_date >="'+sdate+'" and cal_date <="'+edate+'" and cal_date not in (select trade_date from stock_price_limit)'
        data = pd.read_sql_query(sql_str,con)
    except Exception as e:
        print("ex:"+str(e))
        return None
    return data

def find_date_need_update_stk_holdernumber(con,sdate,edate):
    try:
        sql_str='select cal_date from trade_cal where cal_date >="'+'20190101'+'" and cal_date <="'+edate+'" and cal_date not in (select end_date from stk_holder_num)'
        data = pd.read_sql_query(sql_str,con)
    except Exception as e:
        print("ex:"+str(e))
        return None
    return data

def read_money_flow(con,tscode):
    sql_str='select * from money_flow where ts_code="'+tscode+'"'
    data = pd.read_sql_query(sql_str,con)
    return data

def read_stock_basic(con):
    sql_str='select * from stock_basic'
    data = pd.read_sql_query(sql_str,con,index_col='index')
    return data

def read_stock_basic_by_name(con,name):
    sql_str='select * from stock_basic where name="'+name+'"'
    data = pd.read_sql_query(sql_str,con)
    return data

def read_ts_codes(con):
    sql_str='select ts_code from stock_basic'
    data = pd.read_sql_query(sql_str,con)
    return data
def read_stk_holdernumber(con,end_date):
    sql_str='select * from stk_holder_num where end_date <="'+end_date+'"'
    data = pd.read_sql_query(sql_str,con)
    def lam_fun(item):
        if len(item) > 1:
            sItem = item.sort_values(by='end_date',ascending=False)
        else:
            sItem = item
        #print(sItem)
        return sItem.iloc[0]
    return data.groupby(by='ts_code').apply(lam_fun).set_index('index')

readdb_income_report= pd.DataFrame()
readdb_balance_report = pd.DataFrame()
readdb_cashflow_report = pd.DataFrame()
def is_in_report_db(con,ts_code,end_date,report_name):
    #sql_str='select count(*) from '+report_name+' where ts_code="'+ts_code+'"'+' and end_date="'+end_date+'"'
    #data = pd.read_sql_query(sql_str,con)
    #return data.iloc[0][0] != 0
    global readdb_balance_report
    global readdb_cashflow_report
    global readdb_income_report
    if report_name == 'balance_report':
        if readdb_balance_report.empty:
            readdb_balance_report = pd.read_sql_query('select ts_code,end_date from balance_report',con)
        data = readdb_balance_report[(readdb_balance_report.ts_code == ts_code)&(readdb_balance_report.end_date == end_date)]
        return type(data) == pd.DataFrame and not data.empty
    elif report_name == 'income_report':
        if readdb_income_report.empty:
            readdb_income_report = pd.read_sql_query('select ts_code,end_date from income_report',con)
        data = readdb_income_report[(readdb_income_report.ts_code == ts_code)&(readdb_income_report.end_date == end_date)]
        return type(data) == pd.DataFrame and not data.empty
    else:
        if readdb_cashflow_report.empty:
            readdb_cashflow_report = pd.read_sql_query('select ts_code,end_date from cash_report',con)
        data = readdb_cashflow_report[(readdb_cashflow_report.ts_code == ts_code)&(readdb_cashflow_report.end_date == end_date)]
        return type(data) == pd.DataFrame and not data.empty
    
