############################# Fait par BEDDAG Badr

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from mpl_toolkits.mplot3d import Axes3D


ticker = "SPY" 
Apple = yf.Ticker(ticker)

expirations = Apple.options

Dict_Calls = {}
for expiry_date in expirations:
    Dict_Calls[expiry_date] = pd.DataFrame(Apple.option_chain(expiry_date).calls)
    Dict_Calls[expiry_date]["Expiry Date"] = expiry_date

List = []
for df_Call in Dict_Calls.values():
    List.append(df_Call)
    DataFrame_Calls = pd.concat(List, ignore_index= False)

DataFrame_Calls = DataFrame_Calls[["contractSymbol","lastTradeDate","strike","lastPrice","impliedVolatility","Expiry Date"]]
DataFrame_Calls["Expiry Date"] = pd.to_datetime(DataFrame_Calls["Expiry Date"])
DataFrame_Calls["lastTradeDate"] = pd.to_datetime(DataFrame_Calls["lastTradeDate"].dt.strftime("%Y-%m-%d"))
DataFrame_Calls["Maturity"] = (DataFrame_Calls["Expiry Date"] - DataFrame_Calls["lastTradeDate"]).dt.days

Dict_Puts = {}
for expiry_date in expirations:
    Dict_Puts[expiry_date] = pd.DataFrame(Apple.option_chain(expiry_date).puts)
    Dict_Puts[expiry_date]["Expiry Date"] = expiry_date

List = []
for df_Put in Dict_Puts.values():
    List.append(df_Put)
    DataFrame_Puts = pd.concat(List, ignore_index= False)

DataFrame_Puts = DataFrame_Puts[["contractSymbol","lastTradeDate","strike","lastPrice","impliedVolatility","Expiry Date"]]
DataFrame_Puts["Expiry Date"] = pd.to_datetime(DataFrame_Puts["Expiry Date"])
DataFrame_Puts["lastTradeDate"] = pd.to_datetime(DataFrame_Puts["lastTradeDate"].dt.strftime("%Y-%m-%d"))
DataFrame_Puts["Maturity"] = (DataFrame_Puts["Expiry Date"] - DataFrame_Puts["lastTradeDate"]).dt.days

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(DataFrame_Calls['strike'], DataFrame_Calls['Maturity'], DataFrame_Calls['impliedVolatility'], color='b', marker='o')

ax.set_xlabel('strike')
ax.set_ylabel('Maturity')
ax.set_zlabel('impliedVolatility')

ax.set_title('3D Plot of Option Data')

plt.show()