import pandas as pd

from_week = 0 #start week no. of analysis
weeks_to_analyze = 2266 #roughly, max 743 in DB
weeklyInf = pd.DataFrame()
monthlyInf = pd.read_excel('data/inflation/inflation1979.xlsx')
sp500 = pd.read_csv('data/stocks_LT/SPY.csv', usecols=["Date", "Adj Close"])
weeklyRow=0

for row in range(0,int(weeks_to_analyze/4.35)):
    monthlyInf.at[row, "Period"] = monthlyInf.at[row, "Period"].replace('M0','')
    monthlyInf.at[row, "Period"] = monthlyInf.at[row, "Period"].replace('M', '')


for monthlyRow in range(0,int(weeks_to_analyze/4.35)):
    if monthlyRow%10 == 3:
        for weeklyIteration in range(1,6):
            weeklyInf.at[weeklyRow, "Value"] = monthlyInf.at[monthlyRow, "Value"]
            weeklyRow +=1

    if monthlyRow%10 != 3:
        for weeklyIteration in range(1,5):
            weeklyInf.at[weeklyRow, "Value"] = monthlyInf.at[monthlyRow, "Value"]
            weeklyRow +=1

print('weeklyInf', weeklyInf)
weeklyInf.to_csv('./data/inflation/weeklyInflation1979.csv', index=False)
