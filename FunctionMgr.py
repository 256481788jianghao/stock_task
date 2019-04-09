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
            tmp['mean_count'] = len(item)
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
            tmp['sum_count'] = len(item)
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
    '''
           获得换手率与价格浮动的关系表，截止到某日
    '''
    def GetPctChangeAndTurnoverRateRelationList(self,end_date,al=5,bs=5,bl=10):
        date_all_len = al+bl
        date_list = pd.read_sql_query('select * from trade_cal where is_open = 1 and cal_date <="'+str(end_date)+'"',self.sql_con)
        date_list_all = date_list[-date_all_len:]
        pdate = date_list_all.cal_date.iloc[-al]
        sdate_bl = date_list_all.cal_date.iloc[0]
        sdate_bs = date_list_all.cal_date.iloc[bs]
        data_turnover = pd.read_sql_query('select ts_code,trade_date,turnover_rate,turnover_rate_f from daily_basic where trade_date <='+str(end_date)+' and trade_date >='+str(sdate_bl), self.sql_con)
        data_daily = pd.read_sql_query('select trade_date,ts_code,pct_change from daily where trade_date >= '+str(sdate_bl)+' and trade_date <= '+str(end_date),self.sql_con)
        merge_data = pd.merge(left=data_daily, left_on=['ts_code','trade_date'],right=data_turnover, right_on=['ts_code','trade_date'])
        def sum_pct_change(data):
            ans_sum = 1
            for item in data:
                ans_sum = ans_sum * (1+item/100)
            return ans_sum
        merge_date_group = merge_data.groupby('ts_code')
        def g_func(items):
            tmp= dict()
            data_bl = items[items.trade_date < pdate]
            data_bs = items[(items.trade_date <pdate) & (items.trade_date >= sdate_bs)]
            data_al = items[items.trade_date >= pdate]
            tmp['mean_turnover_f_bl'+str(bl)] = data_bl.turnover_rate_f.mean()
            tmp['mean_turnover_f_bs'+str(bs)] = data_bs.turnover_rate_f.mean()
            tmp['sum_pchaneg_bl'+str(bl)] = sum_pct_change(data_bl['pct_change'])
            tmp['sum_pchaneg_al'+str(al)] = sum_pct_change(data_al['pct_change'])
            tmp['data_len'] = len(items)
            return pd.Series(tmp)
        ans_data = merge_date_group.apply(g_func)
        sub_ans_data = ans_data[ans_data.data_len >= date_all_len]
        sub_ans_data['t_rate'] = sub_ans_data['mean_turnover_f_bs'+str(bs)]/sub_ans_data['mean_turnover_f_bl'+str(bl)]
        sort_data = sub_ans_data.sort_values(by='sum_pchaneg_al'+str(al),ascending=False)
        print(sort_data[(sort_data.t_rate > 1.3) & (sort_data.sum_pchaneg_al5 < 1)])
        
        
if __name__ == '__main__':
    pd.set_option('max_columns', 100)
    with sql.connect('stock.db') as con:
        mgr = FunctionMgr(con)
        mgr.GetPctChangeAndTurnoverRateRelationList(20190401)
        #data_concept_mean = mgr.GetSumPChangeAndMeanTurnoverRateList( 20190401, 20190403)
        #data_mean = data_concept_mean.sort_values(by='sum_pct_change',ascending=False)
        #print(mgr.GetConceptSortList(data_mean[0:21].index))
        #data = mgr.GetTurnoverRateMeanSortList(20190120,20190329)
        #data_sort = data.sort_values(by='mean_rate_f',ascending=False)
        #concept_data = mgr.GetConceptSortList(data_sort[0:21].index)
        #print(concept_data)