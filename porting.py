import tushare as ts
import pandas as pd


ts.set_token("edd599506620c2fa4466f6ff765ff458d3dd894b136356c68b8baa32")
pro_api = ts.pro_api()

#get stock base info
'''
ts_code	str	TS代码
symbol	str	股票代码
name	str	股票名称
area	str	所在地域
industry	str	所属行业
fullname	str	股票全称
enname	str	英文全称
market	str	市场类型 （主板/中小板/创业板）
exchange	str	交易所代码
curr_type	str	交易货币
list_status	str	上市状态： L上市 D退市 P暂停上市
list_date	str	上市日期
delist_date	str	退市日期
is_hs	str	是否沪深港通标的，N否 H沪股通 S深股通
'''
def stock_basic():
    return pro_api.stock_basic()

#get trade date
'''
exchange	str	交易所 SSE上交所 SZSE深交所
cal_date	str	日历日期
is_open	int	是否交易 0休市 1交易
pretrade_date	str	上一个交易日
'''
def trade_cal(start_date='20160101'):
    return pro_api.trade_cal(start_date = start_date)

#get daily date
'''
ts_code	str	股票代码
trade_date	str	交易日期
open	float	开盘价
high	float	最高价
low	float	最低价
close	float	收盘价
pre_close	float	昨收价
change	float	涨跌额
pct_change	float	涨跌幅
vol	float	成交量 （手）
amount	float	成交额 （千元）
'''
def daily(trade_date):
    return pro_api.daily(trade_date = trade_date)

#get adj_factor
'''
ts_code	str	股票代码
trade_date	str	交易日期
adj_factor	float	复权因子
start_date	str	开始日期
end_date	str	结束日期
'''
def adj_factor(trade_date):
    return pro_api.adj_factor(trade_date = trade_date)


#get daily_basic
'''
ts_code	str	TS股票代码
trade_date	str	交易日期
close	float	当日收盘价
turnover_rate	float	换手率
turnover_rate_f	float	换手率（自由流通股）
volume_ratio	float	量比
pe	float	市盈率（总市值/净利润）
pe_ttm	float	市盈率（TTM）
pb	float	市净率（总市值/净资产）
ps	float	市销率
ps_ttm	float	市销率（TTM）
total_share	float	总股本 （万）
float_share	float	流通股本 （万）
free_share	float	自由流通股本 （万）
total_mv	float	总市值 （万元）
circ_mv	float	流通市值（万元）
'''
def daily_basic(trade_date):
    return pro_api.daily_basic(trade_date = trade_date)

if __name__ == '__main__':
    data = adj_factor('20170711')
    print(data)
