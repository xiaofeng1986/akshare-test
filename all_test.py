import akshare as ak
import pandas as pd

fundlist = ['164902','519723','519782','519718','006793','519755','519738','519752','002503','002058','002435','003967','002414','519772','519773','519704','000478','100032','163407','110020','001469','001064','001052','004752','100038','001180','002708','000968','502010','161017','002903','000051','110027','340001','270048','000563','000147','003376','002001','000071','000216']
overseefundlist = ['000614','050025','164906','162411','160416']
etflist =['162411','159920','159938','512980'] # 162411 no data
a_stockList = ['600036','000002']
us_stockList = ['VOO','TLT','BIL','SGOL'] # VOO,BIl no data

def select_today_price(df,codeColumn,valueColumn,codelist):
  df = df[df[codeColumn].isin(codelist)]
  df = df[[codeColumn,valueColumn]]
  df[codeColumn] = pd.Categorical(df[codeColumn], codelist)
  df = df.sort_values(codeColumn)
  df.columns = ['代码', '-']
  return df

open_df = ak.fund_em_open_fund_daily()
open_df = select_today_price(open_df,'基金代码',open_df.columns[2],fundlist)

qdii_df = ak.fund_em_open_fund_daily()
qdii_df = select_today_price(qdii_df,'基金代码',qdii_df.columns[4],overseefundlist)

etf_df = select_today_price(ak.fund_em_etf_fund_daily(),'基金代码','市价',etflist)

a_stock_df = select_today_price(ak.stock_zh_a_spot(),'code','trade',a_stockList)
open_df.append(qdii_df).append(etf_df).append(a_stock_df).to_csv('all_test.csv')

# not so many stock, 7 min to query data
# a_stock_df = select_today_price(ak.stock_zh_a_spot(),'code','trade',a_stockList)
# us_stock_df = select_today_price(ak.stock_us_spot(),'symbol','price',us_stockList)


