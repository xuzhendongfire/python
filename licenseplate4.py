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
dta = np.array(train['cnt'],dtype=np.float)
dta = pd.Series(date_week_gb['cnt'])
dta.index = pd.date_range('2013-1-1',periods = dta.size)
dta.plot(figsize=(12,8))



#周天数据太少，先分析均匀的1-6
week1_6 = date_week_gb[date_week_gb['day_of_week']<7]

'''
week1_6 = week1_6.drop([36,37])
week1_6.index = range(len(week1_6))
week1_6 = week1_6.drop([94,95,96,97])
week1_6.index = range(len(week1_6))
week1_6 = week1_6.drop([124,125,126,127])
week1_6.index = range(len(week1_6))
week1_6 = week1_6.drop([202,203,204,205,206])
week1_6.index = range(len(week1_6))
week1_6 = week1_6.drop([208,209,210,211,212,213,214,215,216])
week1_6.index = range(len(week1_6))
week1_6 = week1_6.drop([274,275,276,277,278])
week1_6.index = range(len(week1_6))
week1_6 = week1_6.drop([292,293,294,295,296,297,298,299])
week1_6.index = range(len(week1_6))
week1_6 = week1_6.drop([358,359,360,361,362])
week1_6.index = range(len(week1_6))
'''
#week1_6['date2'] = week1_6.index
#week1_6['day_of_week2'] = (week1_6.index%6+3)%6
#t = week1_6[week1_6['day_of_week']%6 != week1_6['day_of_week2']]

#dta1_6
fig = plt.figure(figsize=(12,8))
dta1_6 = np.array(week1_6['cnt'],dtype=np.float)
dta1_6 = pd.Series(dta1_6)
#dta1_6.index = pd.date_range('2013-1-1',periods = dta1_6.size)
dta1_6.index = pd.Index(sm.tsa.datetools.dates_from_range('1990m1',length = dta1_6.size))
dta1_6.plot(figsize=(12,8))

#a 训练， b 预测
dta1_6_a = dta1_6[0:489]
dta1_6_b = dta1_6[490:978]

#差分
fig = plt.figure(figsize=(12,8))
ax1= fig.add_subplot(211)
diff1 = dta1_6_a.diff(1)
diff1.dropna(inplace=True)
diff1.plot(ax=ax1)

ax2= fig.add_subplot(212)
diff2 = dta1_6_a.diff(2)
diff2.dropna(inplace=True)
diff2.plot(ax=ax2)
#p q

fig = plt.figure(figsize=(12,8))
ax1=fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dta1_6_a,lags=70,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dta1_6_a,lags=70,ax=ax2)


#aic,bic,hqic
arma_mod120 = sm.tsa.ARMA(dta1_6_a,order=(12,0)).fit()
print(arma_mod120.aic,arma_mod120.bic,arma_mod120.hqic)

#预测
predict_sunspots = arma_mod120.predict('2030m1', '2033m1', dynamic=True)
print(predict_sunspots)
fig, ax = plt.subplots(figsize=(12, 8))
ax = dta1_6_a.ix['2030-01-31':].plot(ax=ax)
predict_sunspots.plot(ax=ax)
#对比
#t = dta1_6[504:600]
#t.plot(figsize=(12,8))

plt.show()





