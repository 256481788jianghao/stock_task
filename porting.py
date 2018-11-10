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
def trade_cal():
    return pro_api.trade_cal()

data = trade_cal()

print(data)
