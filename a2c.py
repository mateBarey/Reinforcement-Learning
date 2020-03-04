from binance.client import Client
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from matplotlib import pyplot
import pandas as pd
import os
from collections import OrderedDict
from utils import plotLearning
#for 1st time download file
'''
filename = 'daxyx.txt'
lines = [line.rstrip('\n') for line in open(filename)]
PUBLIC = lines[0]
SECRET = lines[1]

client = Client(api_key=PUBLIC, api_secret=SECRET)

df = client.get_historical_klines("BTCUSDT", client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "22 Jan, 2020")
real_values = OrderedDict()

for i,el in enumerate(df):
  real_values[i] = [el[1], el[4]]

real_df = pd.DataFrame.from_dict(real_values, orient='index', columns=["Real open", "Real close"])
#print(real_df.head)
print(real_df.shape)

dir_l = os.getcwd()
f_l = dir_l + "/testcsv.csv"
real_df = pd.read_csv(f_l)
normalizer = MinMaxScaler().fit(df)
df = normalizer.transform(df)
#df = pd.DataFrame(df,columns=[“Open time”, “Open”, “High”, “Low”, “Close”, “Volume”, “Close time”, “Quote asset volume”, “Number of trades”,“Taker buy base asset volume”,“Taker buy quote asset volume”, “Ignore”])
#df.drop([“Open time”, “Close time”, “Ignore”], axis=1, inplace=True)
print(df.head(5))

'''
