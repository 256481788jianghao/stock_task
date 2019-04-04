import tushare as ts
import pandas as pd

pd.set_option('max_columns', 100)

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

#get block_trade
'''
ts_code	str	Y	TS代码
trade_date	str	Y	交易日历
price	float	Y	成交价
vol	float	Y	成交量（万股）
amount	float	Y	成交金额
buyer	str	Y	买方营业部
seller	str	Y	卖房营业部
'''
def block_trade(trade_date):
    return pro_api.block_trade(trade_date = trade_date)

'''
ts_code    str    股票代码
suspend_date    str    停牌日期
resume_date    str    复牌日期
ann_date    str    公告日期
suspend_reason    str    停牌原因
reason_type    str    停牌原因类别
'''
def stock_suspend(trade_date):
    return pro_api.suspend(ts_code='', suspend_date=trade_date, resume_date='')

'''
ts_code    str    Y    股票代码
exchange    str    Y    交易所代码 ，SSE上交所 SZSE深交所
chairman    str    Y    法人代表
manager    str    Y    总经理
secretary    str    Y    董秘
reg_capital    float    Y    注册资本
setup_date    str    Y    注册日期
province    str    Y    所在省份
city    str    Y    所在城市
introduction    str    N    公司介绍
website    str    Y    公司主页
email    str    Y    电子邮件
office    str    N    办公室
employees    int    Y    员工人数
main_business    str    N    主要业务及产品
business_scope    str    N    经营范围
'''
def stock_company(market_code):
    return pro_api.stock_company(exchange=market_code,fields='ts_code,reg_capital,province,city,main_business,business_scope')

'''
trade_date    str    Y    交易日期
ts_code    str    Y    TS代码
exalter    str    Y    营业部名称
buy    float    Y    买入额（万）
buy_rate    float    Y    买入占总成交比例
sell    float    Y    卖出额（万）
sell_rate    float    Y    卖出占总成交比例
net_buy    float    Y    净成交额（万）
'''
def longhubang_list(trade_date):
    return pro_api.top_inst(trade_date=trade_date)

'''
code    str    Y    概念分类ID
name    str    Y    概念分类名称
src    str    Y    来源
'''
def concept(src='ts'):
    return pro_api.concept(src=src)

'''
id    str    Y    概念代码
ts_code    str    Y    股票代码
name    str    Y    股票名称
in_date    str    N    纳入日期
out_date    str    N    剔除日期
'''
def concept_detail(Id):
    return pro_api.concept_detail(id=Id)

if __name__ == '__main__':
    data = trade_cal()
    print(data[data.cal_date > str(20190322)])
