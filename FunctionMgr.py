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
        
    '''
           概念排名
    '''
    def GetConceptSortList(self,code_list):
        ans_dict=dict()
        for stock_code in code_list:
            data = self.GetConceptByCode(stock_code)
            if not data.empty:
                for name in data.concept_name:
                    if name in ans_dict.keys():
                        ans_dict[name] = ans_dict[name] + 1
                    else:
                        ans_dict[name] = 1
        ans_frame = pd.DataFrame()
        ans_frame['name'] = ans_dict.keys()
        ans_frame['value'] = ans_dict.values()
        return ans_frame.sort_values(by='value',ascending=False)
    '''
             得到某时间段内日数据
    '''
    def GetDaily(self,start_date,end_date):
        data = pd.read_sql_query('select * from daily where trade_date >= '+str(start_date)+' and trade_date <= '+str(end_date),self.sql_con)
        if data.empty:
            print('GetDaily is empty ['+str(start_date)+'->'+str(end_date)+']')
        return data
    '''
           得到某时间段内平均日价格变化
    '''
    def GetPctChangeSumList(self,start_date,end_date):
        data = self.GetDaily(start_date, end_date)
        if data.empty:
            print('GetPctChangeSumList data is empty')
        group = data.groupby(by='ts_code')
        def func(item):
            tmp = dict()
            p_all = 1
            for p in item['pct_change']:
                p_all = p_all*(1+p/100)
            tmp['sum_pct_change'] = (p_all-1)*100
            return pd.Series(tmp)
        ans = group.apply(func)
        return ans
    '''
            获取某时间段内的累计涨幅和换手率
    '''
    def GetSumPChangeAndMeanTurnoverRateList(self,start_date,end_date):
        sum_pctchange_data = self.GetPctChangeSumList(start_date, end_date)
        mean_turnover_data = self.GetTurnoverRateMeanSortList(start_date, end_date)
        mean_data = pd.merge(left=sum_pctchange_data,right=mean_turnover_data,left_index=True,right_index=True)
        return mean_data
    '''
           获取某时间段内某概念的平均涨幅和还手率
    '''
    def GetConceptSumPChangeAndMeanTurnoverRateList(self,concept_id,start_date,end_date):
        concept_detail_all_data = pd.read_sql_query('select * from concept_detail where id = \''+str(concept_id)+'\'', self.sql_con)
        concept_data = concept_detail_all_data[concept_detail_all_data.id == concept_id].set_index('ts_code')
        mean_data = self.GetSumPChangeAndMeanTurnoverRateList(start_date, end_date)
        merge_data = pd.merge(left=mean_data,right=concept_data,left_index=True,right_index=True)
        #print(sum_pctchange_data)
        return merge_data
    
if __name__ == '__main__':
    pd.set_option('max_columns', 100)
    with sql.connect('stock.db') as con:
        mgr = FunctionMgr(con)
        data_concept_mean = mgr.GetSumPChangeAndMeanTurnoverRateList( 20190101, 20190403)
        print(data_concept_mean.sort_values(by='sum_pct_change',ascending=False))
        #data = mgr.GetTurnoverRateMeanSortList(20190120,20190329)
        #data_sort = data.sort_values(by='mean_rate_f',ascending=False)
        #concept_data = mgr.GetConceptSortList(data_sort[0:21].index)
        #print(concept_data)