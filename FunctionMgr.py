import pandas as pd
import sqlite3 as sql
from asn1crypto._ffi import null
from pandas.tests.frame.test_sort_values_level_as_str import ascending

class FunctionMgr:
    def __init__(self,sql_con):
        self.sql_con = sql_con
        pass
    
    '''
           获取大于某换手率的股票列表
    '''
    def GetTurnoverRateList(self,rate,start_date,end_date):
        data = pd.read_sql_query('select ts_code,trade_date,turnover_rate,turnover_rate_f from daily_basic where trade_date <='+str(end_date)+' and trade_date >='+str(start_date)+' and turnover_rate_f >='+str(rate),self.sql_con)
        return data
    
    '''
           获取时间段内平均换手率排名列表
    '''
    def GetTurnoverRateMeanSortList(self,start_date,end_date):
        data = self.GetTurnoverRateList(1, start_date, end_date)
        group = data.groupby(by = 'ts_code')
        def func(item):
            tmp = dict()
            tmp['mean_rate_f'] = item.turnover_rate_f.mean()
            tmp['mean_rate'] = item.turnover_rate.mean()
            return pd.Series(tmp)
        ans = group.apply(func)
        return (ans)
    
if __name__ == '__main__':
    pd.set_option('max_columns', 100)
    with sql.connect('stock.db') as con:
        mgr = FunctionMgr(con)
        data = mgr.GetTurnoverRateMeanSortList(20190301,20190329)
        print(data.sort_values(by='mean_rate_f',ascending=False))