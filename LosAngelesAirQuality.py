# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 13:13:17 2021

@author: ahato
"""

# import random
import pandas as pd
import scipy
import numpy as np
from scipy import stats

datap = pd.read_excel(r'LosAngelesAirQuality.xlsx', 'Demographic profile')

# print(datap.iloc[0,6])  #accessing data in a cell
# print(datap.iloc[1,7])  #accessing data in a cell

class Census(object):
  def __init__(self,census_tract,population,totalpop,county,child,childpop,midage,midpop,elder,oldpop,hispanic,hispop,white,whitepop,
               afroamerican,afropop,natamerican,nativepop,asiamerican,asiapop,other,otherpop):
      self.census_tract = census_tract
      self.population = population
      self.totalpop = totalpop
      self.county = county
      self.child = child
      self.childpop = childpop
      self.midage = midage
      self.midpop = midpop
      self.elder = elder
      self.oldpop = oldpop
      self.hispanic = hispanic
      self.hispop = hispop
      self.white = white
      self.whitepop = whitepop
      self.afroamerican = afroamerican
      self.afropop = afropop
      self.natamerican = natamerican
      self.nativepop = nativepop
      self.asiamerican = asiamerican
      self.asiapop = asiapop
      self.other = other
      self.otherpop = otherpop

def findcounty(data, county):
    for i in range(0,len(data)):
        if data[i].county==county:
            compid=i
            return(compid)
    return(-1)

def f_test(county1,county2):
    f = np.var(county1, ddof=1)/np.var(county2, ddof=1) #calculate F test statistic 
    dfn = county1.size-1 #define degrees of freedom numerator 
    dfd = county2.size-1 #define degrees of freedom denominator 
    p = 1-scipy.stats.f.cdf(f, dfn, dfd) #find p-value of F test statistic 
    return f, p

def t_test(county1,county2,equalvar):
    t=stats.ttest_ind(county1, county2, axis=0, equal_var=equalvar)
    return t
    
'''************** 1. Create a database based upon the county.  This data should have all of the data from the spreadsheet.  The census tracks should be grouped based upon the county.   ******'''
data = []
cnt = 0
for i in range(len(datap)):
    if cnt >=1:
        county = datap.iloc[i,5]
        compid = findcounty(data,county)
        if compid==-1:
            census_tract = [datap.iloc[i,0]]
            population = [datap.iloc[i,4]]
            child = [datap.iloc[i,6]]
            midage = [datap.iloc[i,7]]
            elder = [datap.iloc[i,8]]
            hispanic = [datap.iloc[i,9]]
            white = [datap.iloc[i,10]]
            afroamerican = [datap.iloc[i,11]]
            natamerican = [datap.iloc[i,12]]
            asiamerican = [datap.iloc[i,13]]
            other = [datap.iloc[i,14]]
            totalpop = 0
            childpop = 0
            midpop = 0
            oldpop = 0
            hispop = 0
            whitepop = 0
            afropop = 0
            nativepop = 0
            asiapop = 0
            otherpop = 0
            data.append(Census(census_tract,population,totalpop,county,child,childpop,midage,midpop,elder,oldpop,hispanic,hispop,white,whitepop,
               afroamerican,afropop,natamerican,nativepop,asiamerican,asiapop,other,otherpop))
        else:
            data[compid].census_tract.append(datap.iloc[i,0])
            data[compid].population.append(datap.iloc[i,4])
            data[compid].child.append(datap.iloc[i,6])
            data[compid].midage.append(datap.iloc[i,7])
            data[compid].elder.append(datap.iloc[i,8])
            data[compid].hispanic.append(datap.iloc[i,9])
            data[compid].white.append(datap.iloc[i,10])
            data[compid].afroamerican.append( datap.iloc[i,11])
            data[compid].natamerican.append(datap.iloc[i,12])
            data[compid].asiamerican.append( datap.iloc[i,13])
            data[compid].other.append(datap.iloc[i,14])
    cnt+=1

# print(data[0].population)

'''******** 2. Calculate the population for each county (not percentages).  Do this population for all the categories given.******** '''

for i in range(len(data)):
    pop = 0
    popch = 0
    popmid = 0
    popold = 0
    pophis = 0
    popwhite = 0
    popaf = 0
    popnat = 0
    popasia = 0
    popother = 0
    for j in range(len(data[i].population)):
        pop += data[i].population[j]
        popch += 0.01 * data[i].population[j] * data[i].child[j]
        popmid += 0.01 *data[i].population[j] * data[i].midage[j]
        popold += 0.01 *data[i].population[j] * data[i].elder[j]
        pophis += 0.01 *data[i].population[j] * data[i].hispanic[j]
        popwhite += 0.01 *data[i].population[j] * data[i].white[j]
        popaf += 0.01 *data[i].population[j] * data[i].afroamerican[j]
        popnat += 0.01 *data[i].population[j] * data[i].natamerican[j]
        popasia += 0.01 *data[i].population[j]* data[i].asiamerican[j]
        popother +=0.01 * data[i].population[j] * data[i].other[j]
    data[i].totalpop = int(pop)
    data[i].childpop = int(popch)
    data[i].midpop = int(popmid)
    data[i].oldpop = int(popold)
    data[i].hispop = round(float(pophis),0)
    data[i].whitepop = round(float(popwhite),0)
    data[i].afropop = round(float(popaf),0)
    data[i].nativepop = round(float(popnat),0)
    data[i].asiapop = round(float(popasia),0)
    data[i].otherpop = round(float(popother),0)
    
'''****** 3. Report the population for Los Angeles, San Diego, Orange, Riverside and San Bernardino counties. '''

for i in range(len(data)):
    if data[i].county == "Los Angeles":
        print("Total population of Los Angeles is: ",data[i].totalpop)
    if data[i].county == "San Diego":
        print("Total population of San Diego is: ",data[i].totalpop)
    if data[i].county == "Orange ":
        print("Total population of Orange is: ",data[i].totalpop)
    if data[i].county == "Riverside ":
        print("Total population of Riverside is: ",data[i].totalpop)
    if data[i].county == "San Bernardino":
        print("Total population of San Bernardino is: ",data[i].totalpop)
    print("Age Demographics for", data[i].county, "county:" )
    print(data[i].childpop, "children,", data[i].midpop, "middle aged, and", data[i].oldpop, "old aged." )
    
    print("Race Demographics:", data[i].county, "county has")
    print(data[i].hispop, "hispanic, ", data[i].whitepop, "white, ",data[i].afropop, "african-american, ",data[i].nativepop, "native-american, ",data[i].asiapop, "asian-american, and",data[i].otherpop, "other races.",)
    print(80*"*")
    
    
'''********** 4. Find a 95% confidence interval for the mean of the percentage of the 11-64 population for all 5 of these counties in python ***************'''
midaged = []
for k in range(len(datap)):
    midaged.append(datap.iloc[i,7])

print("95% confidence interval for 11-64 population of all these counties:")
print(stats.t.interval(alpha=0.95, df=len(midaged)-1, loc=np.mean(midaged), scale=stats.sem(midaged)))


'''****5. Do a comparison of equal variances using the F test on the percent of whites for each combination of counties.  If the p value is >.2, then perform a t-test for the difference of means with equal variances  with alpha =.1.  If the p value <=.2, then perform a t-test for the difference of means with unequal variances. '''

print(len(data))
i = int(input('Enter the index of your first county (between 0 and 57) for F-test: '))
j = int(input('Enter the index of your second county (between 0 and 57) for F-test: '))
county1=np.asarray(data[i].white)
county2=np.asarray(data[j].white)


alpha = 0.2
print('The result of f-test is: ', 'F-value is ', round(f_test(county1, county2)[0],4), 'and p_value is ', round(f_test(county1, county2)[1],4))
p_value = f_test(county1, county2)[1]


if p_value>alpha:
    equalvar = True
    print('We fail to reject H0: Var1 = Var2 and conduct a t-test for the difference of means with equal variances.')
else:
    equalvar = False
    print('We reject H0: Var1 = Var2 and conduct a t-test for the difference of means with unequal variances.')


'''****6. If the p value is >.2, then perform a t-test for the difference of means with equal variances  with alpha =.1.  If the p value <=.2, then perform a t-test for the difference of means with unequal variances'''

t_value, p_value1 =  t_test(county1, county2,equalvar)
print('The result of t-test is: ', 't-value is ',round(t_value,4), 'and p_value is ', round(p_value1,4))
alpha = 0.1
if p_value1>alpha/2:
    print('We fail to reject H0: mean1 = mean2 ')
else:
    print('We reject H0: mean1=mean2 ')









