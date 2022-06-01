import pandas as pd
import statsmodels.api as sm
import numpy as np

gold = pd.read_csv('data/goldFutures.csv', usecols=["Price"])
bench = pd.read_csv('data/sp500Hist.csv', usecols=["Price"])
inflation = pd.read_csv('data/inflation/weeklyInflation1979.csv', usecols=["Value"])


gold , bench, inflation = list(gold["Price"]), list(bench["Price"]), list(inflation["Value"])


gold = np.array(gold).reshape(-1, 1)
gold = gold.astype(np.float)

X_stat = sm.add_constant(inflation)
regression = sm.OLS(gold, X_stat).fit()
print('Gold/Inflation', regression.summary())

Y_stat = sm.add_constant(inflation)
regression = sm.OLS(bench, Y_stat).fit()
print('S&P500/Inflation', regression.summary())
