'''
ARIMA链接：http://blog.csdn.net/u010414589/article/details/49622625
链接有些许错误，下面是亲测可运行代码
ARMA外文链接：http://www.statsmodels.org/devel/examples/notebooks/generated/tsa_arma_0.html
'''
from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

dta=[10930,10318,10595,10972,7706,6756,9092,10551,9722,10913,11151,8186,6422, 
6337,11649,11652,10310,12043,7937,6476,9662,9570,9981,9331,9449,6773,6304,9355, 
10477,10148,10395,11261,8713,7299,10424,10795,11069,11602,11427,9095,7707,10767, 
12136,12812,12006,12528,10329,7818,11719,11683,12603,11495,13670,11337,10232, 
13261,13230,15535,16837,19598,14823,11622,19391,18177,19994,14723,15694,13248, 
9543,12872,13101,15053,12619,13749,10228,9725,14729,12518,14564,15085,14722, 
11999,9390,13481,14795,15845,15271,14686,11054,10395]



#数据导入
dta=np.array(dta,dtype=np.float)
dta=pd.Series(dta)
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2001','2090'))
dta.plot(figsize=(12,8))
#plt.show()
'''
#做时间序列的差分，直到得到一个平稳时间序列
fig = plt.figure(figsize=(12,8))
ax1= fig.add_subplot(111)
diff1 = dta.diff(1)
diff1.plot(ax=ax1)

fig = plt.figure(figsize=(12,8))
ax2= fig.add_subplot(111)
diff2 = dta.diff(2)
diff2.plot(ax=ax2)
'''

'''
#选择合适的ARIMA模型，即ARIMA模型中合适的p,q
diff1= dta.diff(1)
diff1.dropna(inplace=True)
fig = plt.figure(figsize=(12,8))
ax1=fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dta,lags=40,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dta,lags=40,ax=ax2)
'''

#有以下模型可以供选择
diff1= dta.diff(1)
diff1.dropna(inplace=True)
arma_mod20 = sm.tsa.ARMA(diff1,(7,0)).fit()
print(arma_mod20.aic,arma_mod20.bic,arma_mod20.hqic)
arma_mod30 = sm.tsa.ARMA(diff1,(0,1)).fit()
print(arma_mod30.aic,arma_mod30.bic,arma_mod30.hqic)
arma_mod40 = sm.tsa.ARMA(diff1,(7,1)).fit()
print(arma_mod40.aic,arma_mod40.bic,arma_mod40.hqic)
arma_mod50 = sm.tsa.ARMA(diff1,(8,0)).fit()
print(arma_mod50.aic,arma_mod50.bic,arma_mod50.hqic)

print()
arma_mod60 = sm.tsa.ARMA(dta,(7,0)).fit()
print(arma_mod60.aic,arma_mod60.bic,arma_mod60.hqic)
arma_mod70 = sm.tsa.ARMA(dta,(0,1)).fit()
print(arma_mod70.aic,arma_mod70.bic,arma_mod70.hqic)
arma_mod80 = sm.tsa.ARMA(dta,(7,1)).fit()
print(arma_mod80.aic,arma_mod80.bic,arma_mod80.hqic)
arma_mod90 = sm.tsa.ARMA(dta,(8,0)).fit()
print(arma_mod90.aic,arma_mod90.bic,arma_mod90.hqic)

'''
#模型检验
#对ARMA(7,0)模型所产生的残差做自相关图
resid = arma_mod90.resid#残差
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(resid, lags=40, ax=ax2)

#做D-W检验
print(sm.stats.durbin_watson(resid.values))

#观察是否符合正态分布
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit=True)

#Ljung-Box检验
r,q,p = sm.tsa.acf(resid.values.squeeze(), qstat=True)
data = np.c_[range(1,41), r[1:], q, p]
table = pd.DataFrame(data, columns=['lag', "AC", "Q", "Prob(>Q)"])
print(table.set_index('lag'))
'''

#模型预测
predict_sunspots = arma_mod20.predict('2090', '2261', dynamic=True)
print(predict_sunspots)
fig, ax = plt.subplots(figsize=(12, 8))
ax = diff1.ix['2001':].plot(ax=ax)
predict_sunspots.plot(ax=ax)


predict_sunspots = arma_mod60.predict('2090', '2261', dynamic=True)
print(predict_sunspots)
fig, ax = plt.subplots(figsize=(12, 8))
ax = dta.ix['2001':].plot(ax=ax)
predict_sunspots.plot(ax=ax)
plt.show()
