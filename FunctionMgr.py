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
    '''
            根据代码查询概念
    '''
    def GetConceptByCode(self,code):
        name_data = pd.read_sql_query('select * from concept_info',self.sql_con)
        detail_data = pd.read_sql_query('select * from concept_detail where ts_code = \''+str(code)+'\'', self.sql_con)
        name_list = []
        for item in detail_data.id:
            subdata = name_data[name_data.code == item]
            #print(subdata.name.iloc[0])
            name_list.append(subdata.name.iloc[0])
        #print(name_list)
        detail_data['concept_name'] = name_list
        return detail_data
        
    
if __name__ == '__main__':
    pd.set_option('max_columns', 100)
    with sql.connect('stock.db') as con:
        mgr = FunctionMgr(con)
        #data = mgr.GetTurnoverRateMeanSortList(20190301,20190329)
        #data_sort = data.sort_values(by='mean_rate_f',ascending=False)
        data = mgr.GetConceptByCode('300312.SZ')
        print(data)