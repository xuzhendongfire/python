import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm, skew
from sklearn.metrics import mean_squared_error



dir = "D:/xzd/bisai/tianchi_shuchuangweilai/"
train = pd.read_table(dir+"train_20171215.txt",engine="python")
test_A = pd.read_table(dir+"test_A_20171225.txt",engine="python")
sample_A = pd.read_table(dir + 'sample_A_20171225.txt',engine='python',header=None)


print(test_A.info())
'''
#箱型图
plt.boxplot(train['cnt'])
plt.show()

#正态图
color = sns.color_palette()
sns.set_style('darkgrid')
sns.distplot(train['cnt'],fit=norm)
plt.show()

#日期与星期
plt.plot(train['date'],train['cnt'])
plt.show()


print(train['cnt'].describe())
'''
'''
#均方误差
train['25%'] = 221
train['50%'] = 351
train['75%'] = 496
train['median'] = train['cnt'].median()
train['mean'] = train['cnt'].mean()
print(mean_squared_error(train['cnt'],train['25%']))
print(mean_squared_error(train['cnt'],train['50%']))
print(mean_squared_error(train['cnt'],train['75%']))
print(mean_squared_error(train['cnt'],train['median']))
print(mean_squared_error(train['cnt'],train['mean']))
'''
'''
#一周七天
monday = train[train['day_of_week']==1]
plt.plot(range(len(monday)),monday['cnt'])
plt.show()
'''
print("一周七天，每个均值")
cnt_gb = train.groupby(['day_of_week'],as_index=False)
res = cnt_gb.cnt.mean()
xx = train.merge(res,on=['day_of_week'])
print(xx.head())
print(mean_squared_error(xx['cnt_x'],xx['cnt_y']))

print("一周七天，每个75%")
week75 = pd.read_table(dir+"week75.txt",engine="python")
xx = train.merge(week75,on=['day_of_week'])
print(xx.head())
print(mean_squared_error(xx['cnt_x'],xx['cnt_y']))


#合并5个品牌
brand_gb = train.groupby(['date','day_of_week'],as_index=False).cnt.sum()
plt.plot(train['day_of_week'],train['cnt'],'.')
plt.show()


for i in range(7):
    tmp = train[train['day_of_week']==i+1]
    plt.subplot(7, 1, i+1)
    plt.plot(tmp['date'],tmp['cnt'],'.')
plt.show()




























