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
    return pro_api.income(ts_code = ts_code,period = period,report_type = 1,fields='''
ts_code    ,
ann_date    ,
f_ann_date    ,
end_date    ,
report_type    ,
comp_type    ,
basic_eps    ,
diluted_eps    ,
total_revenue    ,
revenue    ,
int_income    ,
prem_earned    ,
comm_income    ,
n_commis_income    ,
n_oth_income    ,
n_oth_b_income    ,
prem_income    ,
out_prem    ,
une_prem_reser    ,
reins_income    ,
n_sec_tb_income    ,
n_sec_uw_income    ,
n_asset_mg_income    ,
oth_b_income    ,
fv_value_chg_gain    ,
invest_income    ,
ass_invest_income    ,
forex_gain    ,
total_cogs    ,
oper_cost    ,
int_exp    ,
comm_exp    ,
biz_tax_surchg    ,
sell_exp    ,
admin_exp    ,
fin_exp    ,
assets_impair_loss    ,
prem_refund    ,
compens_payout    ,
reser_insur_liab    ,
div_payt    ,
reins_exp    ,
oper_exp    ,
compens_payout_refu    ,
insur_reser_refu    ,
reins_cost_refund    ,
other_bus_cost    ,
operate_profit    ,
non_oper_income    ,
non_oper_exp    ,
nca_disploss    ,
total_profit    ,
income_tax    ,
n_income    ,
n_income_attr_p    ,
minority_gain    ,
oth_compr_income    ,
t_compr_income    ,
compr_inc_attr_p    ,
compr_inc_attr_m_s    ,
ebit    ,
ebitda    ,
insurance_exp    ,
undist_profit    ,
distable_profit    ,
update_flag
''')

'''
ts_code    str    Y    TS股票代码
ann_date    str    Y    公告日期
f_ann_date    str    Y    实际公告日期
end_date    str    Y    报告期
report_type    str    Y    报表类型
comp_type    str    Y    公司类型
total_share    float    Y    期末总股本
cap_rese    float    Y    资本公积金
undistr_porfit    float    Y    未分配利润
surplus_rese    float    Y    盈余公积金
special_rese    float    Y    专项储备
money_cap    float    Y    货币资金
trad_asset    float    Y    交易性金融资产
notes_receiv    float    Y    应收票据
accounts_receiv    float    Y    应收账款
oth_receiv    float    Y    其他应收款
prepayment    float    Y    预付款项
div_receiv    float    Y    应收股利
int_receiv    float    Y    应收利息
inventories    float    Y    存货
amor_exp    float    Y    长期待摊费用
nca_within_1y    float    Y    一年内到期的非流动资产
sett_rsrv    float    Y    结算备付金
loanto_oth_bank_fi    float    Y    拆出资金
premium_receiv    float    Y    应收保费
reinsur_receiv    float    Y    应收分保账款
reinsur_res_receiv    float    Y    应收分保合同准备金
pur_resale_fa    float    Y    买入返售金融资产
oth_cur_assets    float    Y    其他流动资产
total_cur_assets    float    Y    流动资产合计
fa_avail_for_sale    float    Y    可供出售金融资产
htm_invest    float    Y    持有至到期投资
lt_eqt_invest    float    Y    长期股权投资
invest_real_estate    float    Y    投资性房地产
time_deposits    float    Y    定期存款
oth_assets    float    Y    其他资产
lt_rec    float    Y    长期应收款
fix_assets    float    Y    固定资产
cip    float    Y    在建工程
const_materials    float    Y    工程物资
fixed_assets_disp    float    Y    固定资产清理
produc_bio_assets    float    Y    生产性生物资产
oil_and_gas_assets    float    Y    油气资产
intan_assets    float    Y    无形资产
r_and_d    float    Y    研发支出
goodwill    float    Y    商誉
lt_amor_exp    float    Y    长期待摊费用
defer_tax_assets    float    Y    递延所得税资产
decr_in_disbur    float    Y    发放贷款及垫款
oth_nca    float    Y    其他非流动资产
total_nca    float    Y    非流动资产合计
cash_reser_cb    float    Y    现金及存放中央银行款项
depos_in_oth_bfi    float    Y    存放同业和其它金融机构款项
prec_metals    float    Y    贵金属
deriv_assets    float    Y    衍生金融资产
rr_reins_une_prem    float    Y    应收分保未到期责任准备金
rr_reins_outstd_cla    float    Y    应收分保未决赔款准备金
rr_reins_lins_liab    float    Y    应收分保寿险责任准备金
rr_reins_lthins_liab    float    Y    应收分保长期健康险责任准备金
refund_depos    float    Y    存出保证金
ph_pledge_loans    float    Y    保户质押贷款
refund_cap_depos    float    Y    存出资本保证金
indep_acct_assets    float    Y    独立账户资产
client_depos    float    Y    其中：客户资金存款
client_prov    float    Y    其中：客户备付金
transac_seat_fee    float    Y    其中:交易席位费
invest_as_receiv    float    Y    应收款项类投资
total_assets    float    Y    资产总计
lt_borr    float    Y    长期借款
st_borr    float    Y    短期借款
cb_borr    float    Y    向中央银行借款
depos_ib_deposits    float    Y    吸收存款及同业存放
loan_oth_bank    float    Y    拆入资金
trading_fl    float    Y    交易性金融负债
notes_payable    float    Y    应付票据
acct_payable    float    Y    应付账款
adv_receipts    float    Y    预收款项
sold_for_repur_fa    float    Y    卖出回购金融资产款
comm_payable    float    Y    应付手续费及佣金
payroll_payable    float    Y    应付职工薪酬
taxes_payable    float    Y    应交税费
int_payable    float    Y    应付利息
div_payable    float    Y    应付股利
oth_payable    float    Y    其他应付款
acc_exp    float    Y    预提费用
deferred_inc    float    Y    递延收益
st_bonds_payable    float    Y    应付短期债券
payable_to_reinsurer    float    Y    应付分保账款
rsrv_insur_cont    float    Y    保险合同准备金
acting_trading_sec    float    Y    代理买卖证券款
acting_uw_sec    float    Y    代理承销证券款
non_cur_liab_due_1y    float    Y    一年内到期的非流动负债
oth_cur_liab    float    Y    其他流动负债
total_cur_liab    float    Y    流动负债合计
bond_payable    float    Y    应付债券
lt_payable    float    Y    长期应付款
specific_payables    float    Y    专项应付款
estimated_liab    float    Y    预计负债
defer_tax_liab    float    Y    递延所得税负债
defer_inc_non_cur_liab    float    Y    递延收益-非流动负债
oth_ncl    float    Y    其他非流动负债
total_ncl    float    Y    非流动负债合计
depos_oth_bfi    float    Y    同业和其它金融机构存放款项
deriv_liab    float    Y    衍生金融负债
depos    float    Y    吸收存款
agency_bus_liab    float    Y    代理业务负债
oth_liab    float    Y    其他负债
prem_receiv_adva    float    Y    预收保费
depos_received    float    Y    存入保证金
ph_invest    float    Y    保户储金及投资款
reser_une_prem    float    Y    未到期责任准备金
reser_outstd_claims    float    Y    未决赔款准备金
reser_lins_liab    float    Y    寿险责任准备金
reser_lthins_liab    float    Y    长期健康险责任准备金
indept_acc_liab    float    Y    独立账户负债
pledge_borr    float    Y    其中:质押借款
indem_payable    float    Y    应付赔付款
policy_div_payable    float    Y    应付保单红利
total_liab    float    Y    负债合计
treasury_share    float    Y    减:库存股
ordin_risk_reser    float    Y    一般风险准备
forex_differ    float    Y    外币报表折算差额
invest_loss_unconf    float    Y    未确认的投资损失
minority_int    float    Y    少数股东权益
total_hldr_eqy_exc_min_int    float    Y    股东权益合计(不含少数股东权益)
total_hldr_eqy_inc_min_int    float    Y    股东权益合计(含少数股东权益)
total_liab_hldr_eqy    float    Y    负债及股东权益总计
lt_payroll_payable    float    Y    长期应付职工薪酬
oth_comp_income    float    Y    其他综合收益
oth_eqt_tools    float    Y    其他权益工具
oth_eqt_tools_p_shr    float    Y    其他权益工具(优先股)
lending_funds    float    Y    融出资金
acc_receivable    float    Y    应收款项
st_fin_payable    float    Y    应付短期融资款
payables    float    Y    应付款项
hfs_assets    float    Y    持有待售的资产
hfs_sales    float    Y    持有待售的负债
update_flag    str    N    更新标识
'''
def balance_report(ts_code,period):
    return pro_api.balancesheet(ts_code = ts_code,period = period,report_type = 1,fields='''
ts_code    ,
ann_date    ,
f_ann_date    ,
end_date    ,
report_type    ,
comp_type    ,
total_share    ,
cap_rese    ,
undistr_porfit,
surplus_rese    ,
special_rese    ,
money_cap    ,
trad_asset    ,
notes_receiv    ,
accounts_receiv    ,
oth_receiv    ,
prepayment    ,
div_receiv    ,
int_receiv    ,
inventories    ,
amor_exp    ,
nca_within_1y    ,
sett_rsrv    ,
loanto_oth_bank_fi    ,
premium_receiv    ,
reinsur_receiv    ,
reinsur_res_receiv    ,
pur_resale_fa    ,
oth_cur_assets    ,
total_cur_assets    ,
fa_avail_for_sale    ,
htm_invest    ,
lt_eqt_invest    ,
invest_real_estate    ,
time_deposits    ,
oth_assets    ,
lt_rec    ,
fix_assets    ,
cip    ,
const_materials    ,
fixed_assets_disp    ,
produc_bio_assets    ,
oil_and_gas_assets    ,
intan_assets    ,
r_and_d    ,
goodwill    ,
lt_amor_exp    ,
defer_tax_assets    ,
decr_in_disbur    ,
oth_nca    ,
total_nca    ,
cash_reser_cb    ,
depos_in_oth_bfi    ,
prec_metals    ,
deriv_assets    ,
rr_reins_une_prem    ,
rr_reins_outstd_cla    ,
rr_reins_lins_liab    ,
rr_reins_lthins_liab    ,
refund_depos    ,
ph_pledge_loans    ,
refund_cap_depos    ,
indep_acct_assets    ,
client_depos    ,
client_prov    ,
transac_seat_fee    ,
invest_as_receiv    ,
total_assets    ,
lt_borr    ,
st_borr    ,
cb_borr    ,
depos_ib_deposits    ,
loan_oth_bank    ,
trading_fl    ,
notes_payable    ,
acct_payable    ,
adv_receipts    ,
sold_for_repur_fa    ,
comm_payable    ,
payroll_payable    ,
taxes_payable    ,
int_payable    ,
div_payable    ,
oth_payable    ,
acc_exp    ,
deferred_inc    ,
st_bonds_payable    ,
payable_to_reinsurer    ,
rsrv_insur_cont    ,
acting_trading_sec    ,
acting_uw_sec    ,
non_cur_liab_due_1y    ,
oth_cur_liab    ,
total_cur_liab    ,
bond_payable    ,
lt_payable    ,
specific_payables    ,
estimated_liab    ,
defer_tax_liab    ,
defer_inc_non_cur_liab    ,
oth_ncl    ,
total_ncl    ,
depos_oth_bfi    ,
deriv_liab    ,
depos    ,
agency_bus_liab    ,
oth_liab    ,
prem_receiv_adva    ,
depos_received    ,
ph_invest    ,
reser_une_prem    ,
reser_outstd_claims    ,
reser_lins_liab    ,
reser_lthins_liab    ,
indept_acc_liab    ,
pledge_borr    ,
indem_payable    ,
policy_div_payable    ,
total_liab    ,
treasury_share    ,
ordin_risk_reser    ,
forex_differ    ,
invest_loss_unconf    ,
minority_int    ,
total_hldr_eqy_exc_min_int    ,
total_hldr_eqy_inc_min_int    ,
total_liab_hldr_eqy    ,
lt_payroll_payable    ,
oth_comp_income    ,
oth_eqt_tools    ,
oth_eqt_tools_p_shr    ,
lending_funds    ,
acc_receivable    ,
st_fin_payable    ,
payables    ,
hfs_assets    ,
hfs_sales    ,
update_flag
''')

'''
ts_code    str    Y    TS股票代码
ann_date    str    Y    公告日期
f_ann_date    str    Y    实际公告日期
end_date    str    Y    报告期
comp_type    str    Y    报表类型
report_type    str    Y    公司类型
net_profit    float    Y    净利润
finan_exp    float    Y    财务费用
c_fr_sale_sg    float    Y    销售商品、提供劳务收到的现金
recp_tax_rends    float    Y    收到的税费返还
n_depos_incr_fi    float    Y    客户存款和同业存放款项净增加额
n_incr_loans_cb    float    Y    向中央银行借款净增加额
n_inc_borr_oth_fi    float    Y    向其他金融机构拆入资金净增加额
prem_fr_orig_contr    float    Y    收到原保险合同保费取得的现金
n_incr_insured_dep    float    Y    保户储金净增加额
n_reinsur_prem    float    Y    收到再保业务现金净额
n_incr_disp_tfa    float    Y    处置交易性金融资产净增加额
ifc_cash_incr    float    Y    收取利息和手续费净增加额
n_incr_disp_faas    float    Y    处置可供出售金融资产净增加额
n_incr_loans_oth_bank    float    Y    拆入资金净增加额
n_cap_incr_repur    float    Y    回购业务资金净增加额
c_fr_oth_operate_a    float    Y    收到其他与经营活动有关的现金
c_inf_fr_operate_a    float    Y    经营活动现金流入小计
c_paid_goods_s    float    Y    购买商品、接受劳务支付的现金
c_paid_to_for_empl    float    Y    支付给职工以及为职工支付的现金
c_paid_for_taxes    float    Y    支付的各项税费
n_incr_clt_loan_adv    float    Y    客户贷款及垫款净增加额
n_incr_dep_cbob    float    Y    存放央行和同业款项净增加额
c_pay_claims_orig_inco    float    Y    支付原保险合同赔付款项的现金
pay_handling_chrg    float    Y    支付手续费的现金
pay_comm_insur_plcy    float    Y    支付保单红利的现金
oth_cash_pay_oper_act    float    Y    支付其他与经营活动有关的现金
st_cash_out_act    float    Y    经营活动现金流出小计
n_cashflow_act    float    Y    经营活动产生的现金流量净额
oth_recp_ral_inv_act    float    Y    收到其他与投资活动有关的现金
c_disp_withdrwl_invest    float    Y    收回投资收到的现金
c_recp_return_invest    float    Y    取得投资收益收到的现金
n_recp_disp_fiolta    float    Y    处置固定资产、无形资产和其他长期资产收回的现金净额
n_recp_disp_sobu    float    Y    处置子公司及其他营业单位收到的现金净额
stot_inflows_inv_act    float    Y    投资活动现金流入小计
c_pay_acq_const_fiolta    float    Y    购建固定资产、无形资产和其他长期资产支付的现金
c_paid_invest    float    Y    投资支付的现金
n_disp_subs_oth_biz    float    Y    取得子公司及其他营业单位支付的现金净额
oth_pay_ral_inv_act    float    Y    支付其他与投资活动有关的现金
n_incr_pledge_loan    float    Y    质押贷款净增加额
stot_out_inv_act    float    Y    投资活动现金流出小计
n_cashflow_inv_act    float    Y    投资活动产生的现金流量净额
c_recp_borrow    float    Y    取得借款收到的现金
proc_issue_bonds    float    Y    发行债券收到的现金
oth_cash_recp_ral_fnc_act    float    Y    收到其他与筹资活动有关的现金
stot_cash_in_fnc_act    float    Y    筹资活动现金流入小计
free_cashflow    float    Y    企业自由现金流量
c_prepay_amt_borr    float    Y    偿还债务支付的现金
c_pay_dist_dpcp_int_exp    float    Y    分配股利、利润或偿付利息支付的现金
incl_dvd_profit_paid_sc_ms    float    Y    其中:子公司支付给少数股东的股利、利润
oth_cashpay_ral_fnc_act    float    Y    支付其他与筹资活动有关的现金
stot_cashout_fnc_act    float    Y    筹资活动现金流出小计
n_cash_flows_fnc_act    float    Y    筹资活动产生的现金流量净额
eff_fx_flu_cash    float    Y    汇率变动对现金的影响
n_incr_cash_cash_equ    float    Y    现金及现金等价物净增加额
c_cash_equ_beg_period    float    Y    期初现金及现金等价物余额
c_cash_equ_end_period    float    Y    期末现金及现金等价物余额
c_recp_cap_contrib    float    Y    吸收投资收到的现金
incl_cash_rec_saims    float    Y    其中:子公司吸收少数股东投资收到的现金
uncon_invest_loss    float    Y    未确认投资损失
prov_depr_assets    float    Y    加:资产减值准备
depr_fa_coga_dpba    float    Y    固定资产折旧、油气资产折耗、生产性生物资产折旧
amort_intang_assets    float    Y    无形资产摊销
lt_amort_deferred_exp    float    Y    长期待摊费用摊销
decr_deferred_exp    float    Y    待摊费用减少
incr_acc_exp    float    Y    预提费用增加
loss_disp_fiolta    float    Y    处置固定、无形资产和其他长期资产的损失
loss_scr_fa    float    Y    固定资产报废损失
loss_fv_chg    float    Y    公允价值变动损失
invest_loss    float    Y    投资损失
decr_def_inc_tax_assets    float    Y    递延所得税资产减少
incr_def_inc_tax_liab    float    Y    递延所得税负债增加
decr_inventories    float    Y    存货的减少
decr_oper_payable    float    Y    经营性应收项目的减少
incr_oper_payable    float    Y    经营性应付项目的增加
others    float    Y    其他
im_net_cashflow_oper_act    float    Y    经营活动产生的现金流量净额(间接法)
conv_debt_into_cap    float    Y    债务转为资本
conv_copbonds_due_within_1y    float    Y    一年内到期的可转换公司债券
fa_fnc_leases    float    Y    融资租入固定资产
end_bal_cash    float    Y    现金的期末余额
beg_bal_cash    float    Y    减:现金的期初余额
end_bal_cash_equ    float    Y    加:现金等价物的期末余额
beg_bal_cash_equ    float    Y    减:现金等价物的期初余额
im_n_incr_cash_equ    float    Y    现金及现金等价物净增加额(间接法)
update_flag    str    N    更新标识
'''
def cash_report(ts_code,period):
    return pro_api.cashflow(ts_code = ts_code,period = period,report_type = 1,fields='''
ts_code    ,
ann_date    ,
f_ann_date    ,
end_date    ,
comp_type    ,
report_type    ,
net_profit    ,
finan_exp    ,
c_fr_sale_sg    ,
recp_tax_rends    ,
n_depos_incr_fi    ,
n_incr_loans_cb    ,
n_inc_borr_oth_fi    ,
prem_fr_orig_contr    ,
n_incr_insured_dep    ,
n_reinsur_prem    ,
n_incr_disp_tfa    ,
ifc_cash_incr    ,
n_incr_disp_faas    ,
n_incr_loans_oth_bank    ,
n_cap_incr_repur    ,
c_fr_oth_operate_a    ,
c_inf_fr_operate_a    ,
c_paid_goods_s    ,
c_paid_to_for_empl    ,
c_paid_for_taxes    ,
n_incr_clt_loan_adv    ,
n_incr_dep_cbob    ,
c_pay_claims_orig_inco    ,
pay_handling_chrg    ,
pay_comm_insur_plcy    ,
oth_cash_pay_oper_act    ,
st_cash_out_act    ,
n_cashflow_act    ,
oth_recp_ral_inv_act    ,
c_disp_withdrwl_invest    ,
c_recp_return_invest    ,
n_recp_disp_fiolta    ,
n_recp_disp_sobu    ,
stot_inflows_inv_act    ,
c_pay_acq_const_fiolta    ,
c_paid_invest    ,
n_disp_subs_oth_biz    ,
oth_pay_ral_inv_act    ,
n_incr_pledge_loan    ,
stot_out_inv_act    ,
n_cashflow_inv_act    ,
c_recp_borrow    ,
proc_issue_bonds    ,
oth_cash_recp_ral_fnc_act    ,
stot_cash_in_fnc_act    ,
free_cashflow    ,
c_prepay_amt_borr    ,
c_pay_dist_dpcp_int_exp    ,
incl_dvd_profit_paid_sc_ms    ,
oth_cashpay_ral_fnc_act    ,
stot_cashout_fnc_act    ,
n_cash_flows_fnc_act    ,
eff_fx_flu_cash    ,
n_incr_cash_cash_equ    ,
c_cash_equ_beg_period    ,
c_cash_equ_end_period    ,
c_recp_cap_contrib    ,
incl_cash_rec_saims    ,
uncon_invest_loss    ,
prov_depr_assets    ,
depr_fa_coga_dpba    ,
amort_intang_assets    ,
lt_amort_deferred_exp    ,
decr_deferred_exp    ,
incr_acc_exp    ,
loss_disp_fiolta    ,
loss_scr_fa    ,
loss_fv_chg    ,
invest_loss    ,
decr_def_inc_tax_assets    ,
incr_def_inc_tax_liab    ,
decr_inventories    ,
decr_oper_payable    ,
incr_oper_payable    ,
others    ,
im_net_cashflow_oper_act    ,
conv_debt_into_cap    ,
conv_copbonds_due_within_1y    ,
fa_fnc_leases    ,
end_bal_cash    ,
beg_bal_cash    ,
end_bal_cash_equ    ,
beg_bal_cash_equ    ,
im_n_incr_cash_equ    ,
update_flag
    ''')



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

'''
trade_date    str    Y    交易日期
ts_code    str    Y    股票代码
name    str    Y    股票名称
close    float    Y    收盘价
pct_chg    float    Y    涨跌幅
amp    float    Y    振幅
fc_ratio    float    Y    封单金额/日成交金额
fl_ratio    float    Y    封单手数/流通股本
fd_amount    float    Y    封单金额
first_time    str    Y    首次涨停时间
last_time    str    Y    最后封板时间
open_times    int    Y    打开次数
strth    float    Y    涨跌停强度
limit    str    Y    D跌停U涨停
'''
def price_limit_info(trade_date):
    return pro_api.limit_list(trade_date = trade_date)

'''
trade_date    str    Y    交易日期
ts_code    str    Y    TS股票代码
pre_close    float    N    昨日收盘价
up_limit    float    Y    涨停价
down_limit    float    Y    跌停价
'''
def stock_price_limit(trade_date):
    return pro_api.stk_limit(trade_date = trade_date)

if __name__ == '__main__':
    data = stock_price_limit('20191024')
    print(data)
