import porting as pt
import pandas as pd
import sqlite3 as sql
import readdb as rdb
import datetime
import time
from _overlapped import NULL

def StrToDate(str):
    date = datetime.datetime.strptime(str,'%Y%m%d')
    return date
    
def UpdateFunction(start_date,end_date):
    pd.set_option('max_columns', 100)
    
    sql_con = sql.connect('stock.db')
    cursor = sql_con.cursor()
    
    #start_date = '20170101'
    #end_date = '20191225'
    now_date = datetime.datetime.now().strftime('%Y%m%d')
    
    report_years = ['20161231','20171231','20181231']
    
    tables_info = None
    
    def UpdateReport(report_type,ts_code_list,report_end_date):
        if rdb.is_table_exists(cursor,report_type):
            print(report_type+' exsist')
            report_index = 0
            for ts_code in ts_code_list:
                if rdb.is_in_report_db(sql_con, ts_code, report_end_date, report_type):
                    #print(report_type+' '+ts_code+' '+report_end_date+' exsist')
                    pass
                else:
                    print(report_type+' '+ts_code+' '+report_end_date+' update')
                    data_report = NULL
                    try:
                        if report_type == 'balance_report':
                            data_report = pt.balance_report(ts_code, report_end_date)
                        elif report_type == 'income_report':
                            data_report = pt.income_report(ts_code, report_end_date)
                        else:
                            data_report = pt.cash_report(ts_code, report_end_date)
                    except Exception as ex:
                        print("exception at "+ts_code+" d:"+report_end_date+" t:"+report_type+" ex:"+str(ex))
                        time.sleep(1)
                    if type(data_report) == pd.DataFrame and not data_report.empty:
                        data_report.to_sql(report_type,sql_con,if_exists='append')
                        report_index = report_index + 1
                        if report_index > 78:
                            report_index = 0
                            print('wait for '+report_type)
                            time.sleep(61)
                    else:
                        print("ts_code="+ts_code+" d:"+report_end_date+" t:"+report_type+" empty or not DateFrame")
        else:
            print(report_type+' not exsist')
            report_index = 0
            for ts_code in data_ts_codes.ts_code:
                print('update '+report_type+' of '+ts_code+' at '+report_end_date)
                data_report = NULL
                if report_type == 'balance_report':
                    data_report = pt.balance_report(ts_code, report_end_date)
                elif report_type == 'income_report':
                    data_report = pt.income_report(ts_code, report_end_date)
                else:
                    data_report = pt.cash_report(ts_code, report_end_date)
                if type(data_report) == pd.DataFrame and not data_report.empty:
                    data_report.to_sql(report_type,sql_con,if_exists='append')
                    report_index = report_index + 1
                    if report_index > 78:
                        report_index = 0
                        print('wait for '+report_type)
                        time.sleep(61)
    
    try:
    
        if rdb.is_table_exists(cursor,'tables_info'):
            tables_info = rdb.read_tables_info(sql_con)
        else:
            tables_info = pd.DataFrame()
            tables_info['stock_basic_info'] = [start_date]
            tables_info['trade_cal_info'] = [start_date]
            tables_info['stock_company_info_sz'] = [start_date]
            tables_info['stock_company_info_sh'] = [start_date]
            tables_info['concept_info'] = [start_date]
            tables_info['stk_holdernumber_info'] = [start_date]
    
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
                
        if tables_info['stock_company_info_sz'].iloc[0] != now_date:
            print('start update stock_company_info_sz')
            data_stock_company_info_sz = pt.stock_company('szse')
            if type(data_stock_company_info_sz) == pd.DataFrame:
                data_stock_company_info_sz.to_sql('stock_company_info_sz',sql_con,if_exists='replace')
                tables_info['stock_company_info_sz'] = [now_date]
            else:
                print('get stock_company_info_sz faild')
                
        if tables_info['stock_company_info_sh'].iloc[0] != now_date:
            print('start update stock_company_info_sh')
            data_stock_company_info_sh = pt.stock_company('sse')
            if type(data_stock_company_info_sh) == pd.DataFrame:
                data_stock_company_info_sh.to_sql('stock_company_info_sh',sql_con,if_exists='replace')
                tables_info['stock_company_info_sh'] = [now_date]
            else:
                print('get stock_company_info_sh faild')
        
        if tables_info['concept_info'].iloc[0] != now_date:
            print('start update concept_info')
            data_concept_info = pt.concept()
            if type(data_concept_info) == pd.DataFrame:
                data_concept_info.to_sql('concept_info',sql_con,if_exists='replace')
                concept_detail_list = []
                concept_detail_list_index = 0
                for concept_id in data_concept_info.code:
                    item = pt.concept_detail(concept_id)
                    if type(item) == pd.DataFrame:
                        print("update concept_detail id="+str(concept_id))
                        concept_detail_list.append(item)
                    else:
                        print("concept_detail failed id="+str(concept_id))
                    concept_detail_list_index = concept_detail_list_index + 1
                    if(concept_detail_list_index > 198):
                        concept_detail_list_index = 0
                        print("wait for concept_detail")
                        time.sleep(61)
                detail_data = pd.concat(concept_detail_list)
                detail_data.to_sql('concept_detail',sql_con,if_exists='replace')       
                tables_info['concept_info'] = [now_date]
            else:
                print('get concept_info faild')
                
        
        tables_info.to_sql('tables_info',sql_con,if_exists='replace')
        #print(tables_info)
        
            
        print('start update daily')
        if rdb.is_table_exists(cursor,'daily'):
            print('append daily table')
            trade_cal_need_update_daily = rdb.find_date_need_update_daily(sql_con,start_date,end_date)
            trade_cal_need_update_daily_basic = rdb.find_date_need_update_daily_basic(sql_con,start_date,end_date)
            trade_cal_need_update_adj_factor = rdb.find_date_need_update_adj_factor(sql_con,start_date,end_date)
            trade_cal_need_update_block_trade = rdb.find_date_need_update_block_trade(sql_con,start_date,end_date)
            trade_cal_need_update_stock_suspend = rdb.find_date_need_update_stock_suspend(sql_con,start_date,end_date)
            trade_cal_need_update_longhubang_list = rdb.find_date_need_update_longhubang_list(sql_con,start_date,end_date)
            trade_cal_need_update_money_flow = rdb.find_date_need_update_money_flow(sql_con,start_date,end_date)
            trade_cal_need_update_stock_limit_price = rdb.find_date_need_update_stock_limit_price(sql_con,start_date,end_date)
            trade_cal_need_update_stk_holdernumber = rdb.find_date_need_update_stk_holdernumber(sql_con,start_date,end_date)
            trade_cal_need_update_hk_hold = rdb.find_date_need_update_hk_hold(sql_con,start_date,end_date)
            trade_cal_need_update_margin_detail = rdb.find_date_need_update_margin_detail(sql_con,start_date,end_date)
            print('need update:')
            #print(trade_cal_need_update_daily)
        else:
            print('create daily table')
            trade_cal_db = rdb.read_trade_cal(sql_con)
            trade_cal_open = trade_cal_db[(trade_cal_db.is_open == 1) & (trade_cal_db.cal_date <= end_date) & (trade_cal_db.cal_date >= start_date)]
            #print(trade_cal_open)
            trade_cal_need_update_daily = trade_cal_open
            trade_cal_need_update_daily_basic = trade_cal_open
            trade_cal_need_update_adj_factor = trade_cal_open
            trade_cal_need_update_block_trade = trade_cal_open
            trade_cal_need_update_stock_suspend = trade_cal_open
            trade_cal_need_update_longhubang_list = trade_cal_open
        
        margin_detail_index = 0
        for item in trade_cal_need_update_margin_detail.cal_date:
            dateobj = StrToDate(str(item))
            if dateobj.weekday() == 5 or dateobj.weekday() == 6:
                continue
            print('update margin_detail at '+item)
            data_margin_detail = pt.margin_detail(item)
            if type(data_margin_detail) == pd.DataFrame and not data_margin_detail.empty:
                data_margin_detail.to_sql('margin_detail',sql_con,if_exists='append')
            else:
                print('margin_detail empty at '+item)
        
        hk_hold_index=0
        for item in trade_cal_need_update_hk_hold.cal_date:
            dateobj = StrToDate(str(item))
            if dateobj.weekday() == 6:
                continue
            print('update hk_hold at '+item)
            data_hk_hold = pt.hk_hold(item)
            if type(data_hk_hold) == pd.DataFrame and not data_hk_hold.empty:
                data_hk_hold.to_sql('hk_hold',sql_con,if_exists='append')
            else:
                print('hk_hold empty at '+item)
            hk_hold_index = hk_hold_index+1
            if hk_hold_index > 90:
                hk_hold_index = 0
                print('wait for update hk_hold')
                time.sleep(62)
        
        stk_hn_index = 0
        for item in trade_cal_need_update_stk_holdernumber.cal_date:
            dateobj = StrToDate(str(item))
            if dateobj.weekday() == 5 or dateobj.weekday() == 6:
                continue
            print('update stk_holdernumber at '+item)
            data_stk_hn = pt.stk_holdernumber(item)
            if type(data_stk_hn) == pd.DataFrame and not data_stk_hn.empty:
                data_stk_hn.to_sql('stk_holder_num',sql_con,if_exists='append')
            else:
                print('stk_holder empty at '+item)
            stk_hn_index = stk_hn_index + 1
            if stk_hn_index > 98:
                print('wait for update stk_hn')
                time.sleep(60)
                stk_hn_index = 0
        #exit()
        longhubang_list_dates = [20181115]
        if type(trade_cal_need_update_longhubang_list) == pd.DataFrame:
            longhubang_list_dates = trade_cal_need_update_longhubang_list.cal_date
            
        longhubang_list_index = 0
        for item in longhubang_list_dates:
            print('update longhubang_list '+str(item))
            data_longhubang_list = pt.longhubang_list(item)
            if type(data_longhubang_list) == pd.DataFrame and not data_longhubang_list.empty:
                data_longhubang_list.to_sql('longhubang_list',sql_con,if_exists='append')
            elif data_longhubang_list.empty:
                print('update longhubang_list empty '+str(item))
            else:
                print('update longhubang_list fail '+str(item))
            longhubang_list_index = longhubang_list_index + 1
            if longhubang_list_index > 55:
                print('longhubang_list wait for time')
                longhubang_list_index = 0
                time.sleep(61)
        
        stock_suspend_dates = [20181115]
        if type(trade_cal_need_update_stock_suspend) == pd.DataFrame:
            stock_suspend_dates = trade_cal_need_update_stock_suspend.cal_date
            
        stock_suspend_index = 0
        for item in stock_suspend_dates:
            print('update stock_suspend '+str(item))
            data_stock_suspend = pt.stock_suspend(item)
            if type(data_stock_suspend) == pd.DataFrame and not data_stock_suspend.empty:
                data_stock_suspend.to_sql('stock_suspend',sql_con,if_exists='append')
            elif data_stock_suspend.empty:
                print('update stock_suspend empty '+str(item))
            else:
                print('update stock_suspend fail '+str(item))
            stock_suspend_index = stock_suspend_index + 1
            if stock_suspend_index > 75:
                print('stock_suspend wait for time')
                stock_suspend_index = 0
                time.sleep(61)
        
        block_trade_dates = [20181115]
        if type(trade_cal_need_update_block_trade) == pd.DataFrame:
            block_trade_dates = trade_cal_need_update_block_trade.cal_date
    
        block_trade_index = 0
        for item in block_trade_dates:
            print('update block_trade '+str(item))
            data_block_trade = pt.block_trade(item)
            if type(data_block_trade) == pd.DataFrame and not data_block_trade.empty:
                data_block_trade.to_sql('block_trade',sql_con,if_exists='append')
            elif data_block_trade.empty:
                print('update block_trade empty '+str(item))
            else:
                print('update block_trade fail '+str(item))
            block_trade_index = block_trade_index + 1
            if block_trade_index > 75:
                print('block_trade wait for time')
                block_trade_index = 0
                time.sleep(61)
    
        stock_price_limit_index = 0
        for item in trade_cal_need_update_stock_limit_price.cal_date:
            print('update stock_price_limit:'+str(item))
            data_stock_price_limit = pt.stock_price_limit(item)
            if type(data_stock_price_limit) == pd.DataFrame and not data_stock_price_limit.empty:
                data_stock_price_limit.to_sql('stock_price_limit',sql_con,if_exists='append')
                stock_price_limit_index = stock_price_limit_index + 1
                if stock_price_limit_index > 58:
                    print('stock_price_limit wait for time')
                    stock_price_limit_index = 0
                    time.sleep(61)
            else:
                print('update stock_price_limit:'+str(item)+' fail')
        
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
                
        for item in trade_cal_need_update_money_flow.cal_date:
            print('update money_flow:'+str(item))
            data_money_flow = pt.moneyflow(item)
            if type(data_money_flow) == pd.DataFrame and not data_money_flow.empty:
                data_money_flow.to_sql('money_flow',sql_con,if_exists='append')
            else:
                print('update money_flow:'+str(item)+' fail')
                
                
        #exit()
        for report_end_date in report_years:
            print('check report need update:'+report_end_date)
            data_ts_codes = rdb.read_ts_codes(sql_con)
            
            UpdateReport('income_report',data_ts_codes.ts_code,report_end_date)
            UpdateReport('balance_report',data_ts_codes.ts_code,report_end_date)
            UpdateReport('cash_report',data_ts_codes.ts_code,report_end_date)
                
    except Exception as e:
        print("ex:"+str(e))
        ex = Exception("需要重新尝试")
        raise ex
    finally:
        print("end update")
        cursor.close()
        sql_con.close()

if __name__ == '__main__':
    loop = True
    trycout = 1
    while loop:
        try:
            print("trycout="+str(trycout))
            UpdateFunction('20170101', '20200303')
        except Exception as ex:
            print("ex="+str(ex))
            time.sleep(61)
            trycout = trycout + 1
        else:
            loop = False
            print("更新成功，结束")
    print(StrToDate('20200103').weekday())