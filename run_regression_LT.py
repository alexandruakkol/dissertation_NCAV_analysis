import pandas as pd
import numpy as np
from math import isnan
import statsmodels.api as sm

##############inflation regression###############

inflation = pd.read_csv('data/inflation/weeklyInflation.csv')
NCAVValue = pd.read_csv('printout.csv', usecols=["Total"])
benchValue = pd.read_csv('benchmark.csv', usecols=["Invested"])

NCAVValue = list(NCAVValue["Total"])

lst_benchValue = list(filter(lambda x: (not isnan(x) and x > 1), benchValue["Invested"]))

NCAVValue = filter(lambda x: (not isnan(x) and x > 1), NCAVValue)

lst_NCAVValue = np.array(list(NCAVValue))
lst_Inflation = np.array(list(inflation["Value"]))

if(True):
    print('ncav', lst_NCAVValue, len(lst_NCAVValue))
    print('bench', lst_benchValue, len(lst_benchValue))
    print('inflation', lst_Inflation, len(lst_Inflation))

lst_NCAVValue = lst_NCAVValue.reshape(-1, 1)
lst_Inflation = lst_Inflation.reshape(-1, 1)

X_stat = sm.add_constant(lst_Inflation)
ncavReg = sm.OLS(lst_NCAVValue, X_stat).fit()
benchReg = sm.OLS(lst_benchValue, X_stat).fit()

print('NCAV', ncavReg.summary())
print('Bench', benchReg.summary())