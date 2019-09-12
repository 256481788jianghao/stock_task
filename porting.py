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

'''
ts_code    str    Y    TS代码
ann_date    str    Y    公告日期
f_ann_date    str    Y    实际公告日期
end_date    str    Y    报告期
report_type    str    Y    报告类型 1合并报表 2单季合并 3调整单季合并表 4调整合并报表 5调整前合并报表 6母公司报表 7母公司单季表 8 母公司调整单季表 9母公司调整表 10母公司调整前报表 11调整前合并报表 12母公司调整前报表
comp_type    str    Y    公司类型(1一般工商业2银行3保险4证券)
basic_eps    float    Y    基本每股收益
diluted_eps    float    Y    稀释每股收益
total_revenue    float    Y    营业总收入
revenue    float    Y    营业收入
int_income    float    Y    利息收入
prem_earned    float    Y    已赚保费
comm_income    float    Y    手续费及佣金收入
n_commis_income    float    Y    手续费及佣金净收入
n_oth_income    float    Y    其他经营净收益
n_oth_b_income    float    Y    加:其他业务净收益
prem_income    float    Y    保险业务收入
out_prem    float    Y    减:分出保费
une_prem_reser    float    Y    提取未到期责任准备金
reins_income    float    Y    其中:分保费收入
n_sec_tb_income    float    Y    代理买卖证券业务净收入
n_sec_uw_income    float    Y    证券承销业务净收入
n_asset_mg_income    float    Y    受托客户资产管理业务净收入
oth_b_income    float    Y    其他业务收入
fv_value_chg_gain    float    Y    加:公允价值变动净收益
invest_income    float    Y    加:投资净收益
ass_invest_income    float    Y    其中:对联营企业和合营企业的投资收益
forex_gain    float    Y    加:汇兑净收益
total_cogs    float    Y    营业总成本
oper_cost    float    Y    减:营业成本
int_exp    float    Y    减:利息支出
comm_exp    float    Y    减:手续费及佣金支出
biz_tax_surchg    float    Y    减:营业税金及附加
sell_exp    float    Y    减:销售费用
admin_exp    float    Y    减:管理费用
fin_exp    float    Y    减:财务费用
assets_impair_loss    float    Y    减:资产减值损失
prem_refund    float    Y    退保金
compens_payout    float    Y    赔付总支出
reser_insur_liab    float    Y    提取保险责任准备金
div_payt    float    Y    保户红利支出
reins_exp    float    Y    分保费用
oper_exp    float    Y    营业支出
compens_payout_refu    float    Y    减:摊回赔付支出
insur_reser_refu    float    Y    减:摊回保险责任准备金
reins_cost_refund    float    Y    减:摊回分保费用
other_bus_cost    float    Y    其他业务成本
operate_profit    float    Y    营业利润
non_oper_income    float    Y    加:营业外收入
non_oper_exp    float    Y    减:营业外支出
nca_disploss    float    Y    其中:减:非流动资产处置净损失
total_profit    float    Y    利润总额
income_tax    float    Y    所得税费用
n_income    float    Y    净利润(含少数股东损益)
n_income_attr_p    float    Y    净利润(不含少数股东损益)
minority_gain    float    Y    少数股东损益
oth_compr_income    float    Y    其他综合收益
t_compr_income    float    Y    综合收益总额
compr_inc_attr_p    float    Y    归属于母公司(或股东)的综合收益总额
compr_inc_attr_m_s    float    Y    归属于少数股东的综合收益总额
ebit    float    Y    息税前利润
ebitda    float    Y    息税折旧摊销前利润
insurance_exp    float    Y    保险业务支出
undist_profit    float    Y    年初未分配利润
distable_profit    float    Y    可分配利润
update_flag    str    N    更新标识，0未修改1更正过
'''

def income_report(ts_code,period):
    return pro_api.income(ts_code = ts_code,period = period,report_type = 1,fields='update_flag')

'''
ts_code    str    Y    TS代码
trade_date    str    Y    交易日期
buy_sm_vol    int    Y    小单买入量（手）
buy_sm_amount    float    Y    小单买入金额（万元）
sell_sm_vol    int    Y    小单卖出量（手）
sell_sm_amount    float    Y    小单卖出金额（万元）
buy_md_vol    int    Y    中单买入量（手）
buy_md_amount    float    Y    中单买入金额（万元）
sell_md_vol    int    Y    中单卖出量（手）
sell_md_amount    float    Y    中单卖出金额（万元）
buy_lg_vol    int    Y    大单买入量（手）
buy_lg_amount    float    Y    大单买入金额（万元）
sell_lg_vol    int    Y    大单卖出量（手）
sell_lg_amount    float    Y    大单卖出金额（万元）
buy_elg_vol    int    Y    特大单买入量（手）
buy_elg_amount    float    Y    特大单买入金额（万元）
sell_elg_vol    int    Y    特大单卖出量（手）
sell_elg_amount    float    Y    特大单卖出金额（万元）
net_mf_vol    int    Y    净流入量（手）
net_mf_amount    float    Y    净流入额（万元）
'''

def moneyflow(trade_date):
    return pro_api.moneyflow(trade_date = trade_date)

if __name__ == '__main__':
    data = moneyflow('20190911')
    print(data)
