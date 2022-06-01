import pandas as pd

from_week = 709 #start week no. of analysis
weeks_to_analyze = 743 #roughly, max 743 in DB
weeklyInf = pd.DataFrame()
monthlyInf = pd.read_excel('data/inflation/monthlyCPI.xlsx')
sp500 = pd.read_csv('data/stocks_LT/SPY.csv', usecols=["Date", "Adj Close"])
weeklyRow=0
for row in range(0,int(weeks_to_analyze/4.3)):
    monthlyInf.at[row, "Period"] = monthlyInf.at[row, "Period"].replace('M0','')
    monthlyInf.at[row, "Period"] = monthlyInf.at[row, "Period"].replace('M', '')


for monthlyRow in range(0,int(weeks_to_analyze/4.3)):
    if monthlyRow%3 == 1:
        for weeklyIterarion in range(1,4):
            weeklyInf.at[weeklyRow, "Value"] = monthlyInf.at[monthlyRow, "Value"]
            weeklyRow +=1

    if monthlyRow%3 != 1:
        for weeklyIterarion in range(1,5):
            weeklyInf.at[weeklyRow, "Value"] = monthlyInf.at[monthlyRow, "Value"]
            weeklyRow +=1

print('weeklyInf', weeklyInf)
weeklyInf.to_csv('./data/inflation/weeklyInflation.csv', index=False)