import pandas as pd

stock_data_09 = pd.read_csv('STOCK_DAY_0050_202009.csv')
stock_data_10 = pd.read_csv('STOCK_DAY_0050_202010.csv')
stock_data_concat = pd.concat([stock_data_09,stock_data_10])
print(stock_data_concat)
print(stock_data_concat[stock_data_concat.open < stock_data_concat.close])