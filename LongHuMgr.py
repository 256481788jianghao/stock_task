import pandas as pd
import sqlite3 as sql

class LongHuMgr:
    def __init__(self,con):
        longhu_list = pd.read_sql_query('select * from longhubang_list',con)
        print(longhu_list)
        
if __name__ == '__main__':
    pd.set_option('max_columns', 100)
    with sql.connect('stock.db') as con:
        mgr = LongHuMgr(con)