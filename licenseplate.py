import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm, skew
from sklearn.metrics import mean_squared_error



dir = "D:/xzd/bisai/tianchi_qicheshangpai/"
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
date_weak_gb = train.groupby(['date','day_of_week'],as_index=False).cnt.sum()
'''
plt.plot(train['day_of_week'],train['cnt'],'.')
plt.show()
for i in range(7):
    tmp = train[train['day_of_week']==i+1]
    plt.subplot(7, 1, i+1)
    plt.plot(tmp['date'],tmp['cnt'],'.')
plt.show()
'''

#查看时序特征
xx = date_weak_gb
#xx = xx[xx['date']>344]
cnt = xx['cnt']
date = xx['date']
plt.plot(date,cnt,color='#99CC01',linewidth=1,markeredgewidth=3,markeredgecolor='#99CC01',alpha=0.8)
plt.show()

#数据分三份1-344,345-688,689-1032
y1 = date_weak_gb[date_weak_gb['date']<=344]
y2 = date_weak_gb[date_weak_gb['date']<=688]
y2 = y2[y2['date']>344]
y3 = date_weak_gb[date_weak_gb['date']>688]
'''
print("y1:")
print(y1['cnt'].describe())
print("y2:")
print(y2['cnt'].describe())
print("y3:")
print(y3['cnt'].describe())

print("y2:y1用比增长:",y2['cnt'].sum()/y1['cnt'].sum()-1)#0.0514839817632
print("y3:y2用比增长:",y3['cnt'].sum()/y2['cnt'].sum()-1)#0.152209492635
'''
#每个品牌
brand1 = train[train['date']<=344]
brand2 = train[train['date']<=688]
brand2 = brand2[brand2['date']>344]
brand3 = train[train['date']>688]
brand_gb1 = brand1.groupby(['brand'],as_index=False).cnt.sum()
brand_gb2 = brand2.groupby(['brand'],as_index=False).cnt.sum()
brand_gb3 = brand3.groupby(['brand'],as_index=False).cnt.sum()
brand_gb = train.groupby(['brand'],as_index=False).cnt.sum()
print(brand_gb1)
print(brand_gb2)
print(brand_gb3)
print(brand_gb)

#每年数据分割为12份
#30:1,3,7,8,12     150
#28:4,5,6,9,10,11  168
#20:2              26
'''
1-30   1:30
2-26   31:56
3-30   57:86
4-28   87:114
5-28   115:142
6-28   143:170
7-30   171:200
8-30   201:230
9-28   231:258
10-28  259:286
11-28  287:314
12-30  315:344
第一步：分别统计每月的周X的mean()
第二步：merge到每月中
第三步：计算mse
'''
#第一步
year = 344
y1_brand = brand1.groupby(['date','day_of_week'],as_index=False).cnt.sum()
y1_m1 = y1_brand[y1_brand['date']<=30]
y1_m2 = y1_brand[y1_brand['date']<=56]
y1_m2 = y1_m2[y1_m2['date']>=31]
y1_m3 = y1_brand[y1_brand['date']<=86]
y1_m3 = y1_m3[y1_m3['date']>=57]
y1_m4 = y1_brand[y1_brand['date']<=114]
y1_m4 = y1_m4[y1_m4['date']>=87]
y1_m5 = y1_brand[y1_brand['date']<=142]
y1_m5 = y1_m5[y1_m5['date']>=115]
y1_m6 = y1_brand[y1_brand['date']<=170]
y1_m6 = y1_m6[y1_m6['date']>=143]
y1_m7 = y1_brand[y1_brand['date']<=200]
y1_m7 = y1_m7[y1_m7['date']>=171]
y1_m8 = y1_brand[y1_brand['date']<=230]
y1_m8 = y1_m8[y1_m8['date']>=201]
y1_m9 = y1_brand[y1_brand['date']<=258]
y1_m9 = y1_m9[y1_m9['date']>=231]
y1_m10 = y1_brand[y1_brand['date']<=286]
y1_m10 = y1_m10[y1_m10['date']>=259]
y1_m11 = y1_brand[y1_brand['date']<=314]
y1_m11 = y1_m11[y1_m11['date']>=287]
y1_m12 = y1_brand[y1_brand['date']<=344]
y1_m12 = y1_m12[y1_m12['date']>=315]

y1_m1_gb = y1_m1.groupby(['day_of_week'],as_index=False).cnt.mean()
y1_m2_gb = y1_m2.groupby(['day_of_week'],as_index=False).cnt.mean()
y1_m3_gb = y1_m3.groupby(['day_of_week'],as_index=False).cnt.mean()
y1_m4_gb = y1_m4.groupby(['day_of_week'],as_index=False).cnt.mean()
y1_m5_gb = y1_m5.groupby(['day_of_week'],as_index=False).cnt.mean()
y1_m6_gb = y1_m6.groupby(['day_of_week'],as_index=False).cnt.mean()
y1_m7_gb = y1_m7.groupby(['day_of_week'],as_index=False).cnt.mean()
y1_m8_gb = y1_m8.groupby(['day_of_week'],as_index=False).cnt.mean()
y1_m9_gb = y1_m9.groupby(['day_of_week'],as_index=False).cnt.mean()
y1_m10_gb = y1_m10.groupby(['day_of_week'],as_index=False).cnt.mean()
y1_m11_gb = y1_m11.groupby(['day_of_week'],as_index=False).cnt.mean()
y1_m12_gb = y1_m12.groupby(['day_of_week'],as_index=False).cnt.mean()
y1_mAll_gb = y1_brand.groupby(['day_of_week'],as_index=False).cnt.mean()

y2_brand = brand2.groupby(['date','day_of_week'],as_index=False).cnt.sum()
y2_m1 = y2_brand[y2_brand['date']<=30+year]
y2_m2 = y2_brand[y2_brand['date']<=56+year]
y2_m2 = y2_m2[y2_m2['date']>=31+year]
y2_m3 = y2_brand[y2_brand['date']<=86+year]
y2_m3 = y2_m3[y2_m3['date']>=57+year]
y2_m4 = y2_brand[y2_brand['date']<=114+year]
y2_m4 = y2_m4[y2_m4['date']>=87+year]
y2_m5 = y2_brand[y2_brand['date']<=142+year]
y2_m5 = y2_m5[y2_m5['date']>=115+year]
y2_m6 = y2_brand[y2_brand['date']<=170+year]
y2_m6 = y2_m6[y2_m6['date']>=143+year]
y2_m7 = y2_brand[y2_brand['date']<=200+year]
y2_m7 = y2_m7[y2_m7['date']>=171+year]
y2_m8 = y2_brand[y2_brand['date']<=230+year]
y2_m8 = y2_m8[y2_m8['date']>=201+year]
y2_m9 = y2_brand[y2_brand['date']<=258+year]
y2_m9 = y2_m9[y2_m9['date']>=231+year]
y2_m10 = y2_brand[y2_brand['date']<=286+year]
y2_m10 = y2_m10[y2_m10['date']>=259+year]
y2_m11 = y2_brand[y2_brand['date']<=314+year]
y2_m11 = y2_m11[y2_m11['date']>=287+year]
y2_m12 = y2_brand[y2_brand['date']<=344+year]
y2_m12 = y2_m12[y2_m12['date']>=315+year]

y2_m1_gb = y2_m1.groupby(['day_of_week'],as_index=False).cnt.mean()
y2_m2_gb = y2_m2.groupby(['day_of_week'],as_index=False).cnt.mean()
y2_m3_gb = y2_m3.groupby(['day_of_week'],as_index=False).cnt.mean()
y2_m4_gb = y2_m4.groupby(['day_of_week'],as_index=False).cnt.mean()
y2_m5_gb = y2_m5.groupby(['day_of_week'],as_index=False).cnt.mean()
y2_m6_gb = y2_m6.groupby(['day_of_week'],as_index=False).cnt.mean()
y2_m7_gb = y2_m7.groupby(['day_of_week'],as_index=False).cnt.mean()
y2_m8_gb = y2_m8.groupby(['day_of_week'],as_index=False).cnt.mean()
y2_m9_gb = y2_m9.groupby(['day_of_week'],as_index=False).cnt.mean()
y2_m10_gb = y2_m10.groupby(['day_of_week'],as_index=False).cnt.mean()
y2_m11_gb = y2_m11.groupby(['day_of_week'],as_index=False).cnt.mean()
y2_m12_gb = y2_m12.groupby(['day_of_week'],as_index=False).cnt.mean()
y2_mAll_gb = y2_brand.groupby(['day_of_week'],as_index=False).cnt.mean()


y3_brand = brand3.groupby(['date','day_of_week'],as_index=False).cnt.sum()
y3_m1 = y3_brand[y3_brand['date']<=30+year*2]
y3_m2 = y3_brand[y3_brand['date']<=56+year*2]
y3_m2 = y3_m2[y3_m2['date']>=31+year*2]
y3_m3 = y3_brand[y3_brand['date']<=86+year*2]
y3_m3 = y3_m3[y3_m3['date']>=57+year*2]
y3_m4 = y3_brand[y3_brand['date']<=114+year*2]
y3_m4 = y3_m4[y3_m4['date']>=87+year*2]
y3_m5 = y3_brand[y3_brand['date']<=142+year*2]
y3_m5 = y3_m5[y3_m5['date']>=115+year*2]
y3_m6 = y3_brand[y3_brand['date']<=170+year*2]
y3_m6 = y3_m6[y3_m6['date']>=143+year*2]
y3_m7 = y3_brand[y3_brand['date']<=200+year*2]
y3_m7 = y3_m7[y3_m7['date']>=171+year*2]
y3_m8 = y3_brand[y3_brand['date']<=230+year*2]
y3_m8 = y3_m8[y3_m8['date']>=201+year*2]
y3_m9 = y3_brand[y3_brand['date']<=258+year*2]
y3_m9 = y3_m9[y3_m9['date']>=231+year*2]
y3_m10 = y3_brand[y3_brand['date']<=286+year*2]
y3_m10 = y3_m10[y3_m10['date']>=259+year*2]
y3_m11 = y3_brand[y3_brand['date']<=314+year*2]
y3_m11 = y3_m11[y3_m11['date']>=287+year*2]
y3_m12 = y3_brand[y3_brand['date']<=344+year*2]
y3_m12 = y3_m12[y3_m12['date']>=315+year*2]

y3_m1_gb = y3_m1.groupby(['day_of_week'],as_index=False).cnt.mean()
y3_m2_gb = y3_m2.groupby(['day_of_week'],as_index=False).cnt.mean()
y3_m3_gb = y3_m3.groupby(['day_of_week'],as_index=False).cnt.mean()
y3_m4_gb = y3_m4.groupby(['day_of_week'],as_index=False).cnt.mean()
y3_m5_gb = y3_m5.groupby(['day_of_week'],as_index=False).cnt.mean()
y3_m6_gb = y3_m6.groupby(['day_of_week'],as_index=False).cnt.mean()
y3_m7_gb = y3_m7.groupby(['day_of_week'],as_index=False).cnt.mean()
y3_m8_gb = y3_m8.groupby(['day_of_week'],as_index=False).cnt.mean()
y3_m9_gb = y3_m9.groupby(['day_of_week'],as_index=False).cnt.mean()
y3_m10_gb = y3_m10.groupby(['day_of_week'],as_index=False).cnt.mean()
y3_m11_gb = y3_m11.groupby(['day_of_week'],as_index=False).cnt.mean()
y3_m12_gb = y3_m12.groupby(['day_of_week'],as_index=False).cnt.mean()
y3_mAll_gb = y3_brand.groupby(['day_of_week'],as_index=False).cnt.mean()
#第二步(第一步可能出现没有周7的情况)


















