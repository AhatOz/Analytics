# -*- coding: utf-8 -*-
"""
Created on Sun May  2 12:00:33 2021

@author: ahato
"""
import scipy
import numpy as np
from scipy import stats
import Database as db


def f_test(county1,county2):
    f = np.var(county1, ddof=1)/np.var(county2, ddof=1) #calculate F test statistic 
    dfn = county1.size-1 #define degrees of freedom numerator 
    dfd = county2.size-1 #define degrees of freedom denominator 
    p = 1-scipy.stats.f.cdf(f, dfn, dfd) #find p-value of F test statistic 
    return f, p

def t_test(county1,county2,equalvar):
    t=stats.ttest_ind(county1, county2, axis=0, equal_var=equalvar)
    return t


defectives= [] 
for i in range(len(db.suppliers)):
    for j in range(len(db.suppliers[i].defective)):
        defectives.append(db.suppliers[i].defective[j])
    
    
# print(defectives)    
print("95% confidence interval for defectives of all these suppliers:")
print(stats.t.interval(alpha=0.95, df=len(defectives)-1, loc=np.mean(defectives), scale=stats.sem(defectives)))




# print(db.suppliers[29].defective)
'''F-Test'''
for i in range (len(db.suppliers)-1):
    defect1 = np.asarray(db.suppliers[i].defective)
    defect2 = np.asarray(db.suppliers[i+1].defective)
    alpha = 0.2
    print('The result of f-test between suppliers',i,'and',i+1,'is:' + 'F-value is ', round(f_test(defect1, defect2)[0],4), 'and p_value is ', round(f_test(defect1, defect2)[1],4))
    p_value = f_test(defect1, defect2)[1]
    if p_value>alpha:
        equalvar = True
        print('We fail to reject H0: Var1 = Var2 and conduct a t-test for the difference of means with equal variances.')
    else:
        equalvar = False
        print('We reject H0: Var1 = Var2 and conduct a t-test for the difference of means with unequal variances.')
        

#T-Test
    t_value, p_value1 =  t_test(defect1, defect2,equalvar)
    print('The result of t-test between suppliers',i,'and',i+1,'is:' + 't-value is ',round(t_value,4), 'and p_value is ', round(p_value1,4))
    alpha = 0.1
    if p_value1>alpha/2:
        print('We fail to reject H0: mean1 = mean2 ')
    else:
        print('We reject H0: mean1=mean2 ')
        
    print(100*'*')