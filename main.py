import pandas as pd
import os

results = pd.DataFrame()

for file in os.listdir('data'):
    filename = os.fsdecode(file)
    combo = pd.read_csv(r'data/'+filename, usecols=["Date","Adj Close"])
    combo.at[0, "Invested"] = 2500
    ticker = filename.replace(".csv", '')
    for row in range(1,627):
        combo.at[row,"Invested"] = (combo.iloc[row]["Adj Close"] / combo.iloc[row-1]["Adj Close"]) * combo.iloc[row-1]["Invested"]
    results.at[0,ticker] = combo.iloc[626]["Invested"]
    results.to_csv('./aggregate.csv', index=False)