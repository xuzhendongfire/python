from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

dir = "D:/xzd/bisai/tianchi_qicheshangpai/"
train = pd.read_table(dir+"train_20171215.txt",engine="python")
test_A = pd.read_table(dir+"test_A_20171225.txt",engine="python")
sample_A = pd.read_table(dir + 'sample_A_20171225.txt',engine='python',header=None)

date_week_gb = train.groupby(['date','day_of_week'],as_index = False).cnt.sum()
#dta = np.array(train['cnt'],dtype=np.float)
#dta = pd.Series(date_week_gb['cnt'])
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2001','6773'))
dta.index = pd.Index(date_week_gb['date'])
dta.plot(figsize=(12,8))

'''
fig = plt.figure(figsize=(12,8))
ax1= fig.add_subplot(211)#x行y列第z块
diff1 = dta.diff(1)
diff1.plot(ax=ax1)

ax2= fig.add_subplot(212)
diff2 = dta.diff(2)
diff2.plot(ax=ax2)

#选择合适的ARIMA模型，即ARIMA模型中合适的p,q
diff1= dta.diff(1)
diff1.dropna(inplace=True)
fig = plt.figure(figsize=(12,8))
ax1=fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dta,lags=70,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dta,lags=70,ax=ax2)
'''

y1 = date_week_gb[date_week_gb['date']<=344]
y2 = date_week_gb[date_week_gb['date']<=688]
y2 = y2[y2['date']>344]
y3 = date_week_gb[date_week_gb['date']>688]
#data1
fig = plt.figure(figsize=(12,8))
dta1 = np.array(y1['cnt'],dtype=np.float)
dta1 = pd.Series(dta1)
dta1.index = pd.Index(sm.tsa.datetools.dates_from_range('1800','2143'))
dta1.plot(figsize=(12,8))

#data1 差分
fig = plt.figure(figsize=(12,8))
ax1= fig.add_subplot(211)
diff1 = dta1.diff(1)
diff1.plot(ax=ax1)

ax2= fig.add_subplot(212)
diff2 = dta1.diff(2)
diff2.plot(ax=ax2)

#data1 p q
diff1.dropna(inplace=True)
fig = plt.figure(figsize=(12,8))
ax1=fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dta,lags=70,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dta,lags=70,ax=ax2)


#plt.show()

arma_mod90 = sm.tsa.ARMA(diff1,(12,0)).fit()
print(arma_mod90.aic,arma_mod90.bic,arma_mod90.hqic)

arma_mod120 = sm.tsa.ARMA(dta1,order=(12,0)).fit()
print(arma_mod120.aic,arma_mod120.bic,arma_mod120.hqic)

#预测

predict_sunspots = arma_mod120.predict('2143', '2261', dynamic=True)
print(predict_sunspots)
fig, ax = plt.subplots(figsize=(12, 8))
ax = diff2.ix['2143':].plot(ax=ax)
predict_sunspots.plot(ax=ax)

#对比
t = y2[y2['date']<464]#118条数据
t = np.array(t['cnt'],dtype=np.float)
t = pd.Series(t)
t.index = pd.Index(sm.tsa.datetools.dates_from_range('2143','2261'))
t.plot(figsize=(12,8))
plt.show()

