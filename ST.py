import pandas as pd
import os
import numpy as np


debug = False
from_week = 43 #start week no. of analysis
weeks_to_analyze = 96 #max of 632 weeks in database

results =  pd.DataFrame()
benchResults = pd.DataFrame()
ncavPortfolio = pd.DataFrame()

ncavPortfolio = pd.read_csv('data/stocks_LT/AA.csv', usecols=["Date"])
#function that returns the portfolio value at any point in time
def NCAVsum(df, period):
    return df.loc[period, df.columns != 'Date'].sum()

#view whole dataframe option
if(False):
    pd.set_option("display.max_rows", None, "display.max_columns", None)

for file in os.listdir('data/stocks_LT'):
    filename = os.fsdecode(file)

#benchmark performance block
    if filename == 'SPY.csv':
        combo = pd.read_csv(r'data/stocks_LT/' + filename, usecols=["Date", "Adj Close"])

        combo.at[from_week-1, "Invested"] = 100000
        ticker = filename.replace(".csv", '')
        for row in range(from_week, weeks_to_analyze-1):
            combo.at[row, "Invested"] = (combo.iloc[row]["Adj Close"] / combo.iloc[row - 1]["Adj Close"]) * \
                                        combo.iloc[row - 1]["Invested"]
            combo.at[row, 'Log returns'] = np.log(combo.iloc[row]['Adj Close'] / combo.iloc[row-1]['Adj Close'])

        weekly_stdDev = combo['Log returns'].std()
        annualized_stdDev = weekly_stdDev * np.sqrt(52)
        print('benchmarkStddev: ',annualized_stdDev)


        benchResults.at[0, ticker] = combo.iloc[weeks_to_analyze-1]["Invested"]
        combo.to_csv('./benchmark.csv', index=False)
        #benchResults.at[1, ticker] = annualized_stdDev
        continue


    #if filename == 'AA.csv' or filename == 'ACH.csv':
    combo = pd.read_csv(r'data/stocks_LT/'+filename, usecols=["Date","Adj Close"])
    combo.at[from_week-1, "Invested"] = 2857.14
    ticker = filename.replace(".csv", '')

    #printout for every week
    for row in range(from_week,weeks_to_analyze):
        combo.at[row,"Invested"] = (combo.iloc[row]["Adj Close"] / combo.iloc[row-1]["Adj Close"]) * combo.iloc[row-1]["Invested"]
        combo.at[row, 'Log returns'] = np.log(combo.iloc[row]['Adj Close'] / combo.iloc[row - 1]['Adj Close'])
        ncavPortfolio.at[row, ticker] = combo.at[row,"Invested"]

    weekly_stdDev = combo['Log returns'].std()
    annualized_stdDev = weekly_stdDev * np.sqrt(52)

    results.at[0,0] = "Terminal value"
    results.at[1,0] = "Standard Deviation"

    results.at[0,ticker] = combo.iloc[weeks_to_analyze-1]["Invested"]
    #computing the annualized rate of return for each stock
    results.at[1,ticker] = annualized_stdDev

results.to_csv('./aggregate.csv', index=False)


if(True):
    printoutM = pd.read_csv('printout_M.csv', usecols=["Sum"])
    for row in range(1, weeks_to_analyze):
        printoutM.at[row, 'Log returns'] = np.log(printoutM.iloc[row]['Sum'] / printoutM.iloc[row - 1]['Sum'])

    weekly_stdDev = printoutM['Log returns'].std()
    annualized_stdDev = weekly_stdDev * np.sqrt(52)
    print('NCAVStddev: ', annualized_stdDev)

for row in range(1,weeks_to_analyze):
    ncavPortfolio.at[row,"Total"] = NCAVsum(ncavPortfolio, row)

ncavPortfolio.to_csv('./printout.csv', index=False)