# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 12:10:33 2021

@author: ahato
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

datap = pd.read_excel(r'CountriesData.xlsx', 'Data')
datap.fillna(0,inplace = True)


class Country(object):
  def __init__(self,country,GDP,Gross_national_expenditure,Final_consumption_expenditure ,
                Households_expend_capita,Gen_gov,Inflation,IncomeReceipt,Exports,GoodImp,ServImp,
                Household_expend,Manufacturing):
      self.country = country
      self.GDP = GDP
      self.Gross_national_expenditure = Gross_national_expenditure
      self.Final_consumption_expenditure = Final_consumption_expenditure
      self.Households_expend_capita = Households_expend_capita
      self.Gen_gov = Gen_gov
      self.Inflation = Inflation
      self.IncomeReceipt = IncomeReceipt
      self.Exports = Exports
      self.GoodImp = GoodImp
      self.ServImp = ServImp
      self.Household_expend = Household_expend
      self.Manufacturing = Manufacturing

def findcountry(data, country):
    for i in range(0,len(data)):
        if data[i].country==country:
            compid=i
            return(compid)
    return(-1)

    
'''PROBLEM 1'''    
data = []

for i in range(len(datap)):
    country = datap.iloc[i,0]
    compid = findcountry(data,country)
    if compid==-1:
        GDP = []
        Gross_national_expenditure = []
        Final_consumption_expenditure = []
        Households_expend_capita = []
        Gen_gov = []
        Inflation = []
        IncomeReceipt = []
        Exports= []
        GoodImp = []
        ServImp = []
        Household_expend = []
        Manufacturing = []
        if datap.iloc[i,2] == 'GDP (constant LCU)':
            GDP.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Gross national expenditure (current US$)':
            Gross_national_expenditure.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Final consumption expenditure (% of GDP)':
            Final_consumption_expenditure.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Households and NPISHs Final consumption expenditure per capita growth (annual %)':
            Households_expend_capita.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'General government final consumption expenditure (% of GDP)':
            Gen_gov.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Inflation, consumer prices (annual %)':
            Inflation.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Primary income receipts (BoP, current US$)':
            IncomeReceipt.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Exports of goods and services (BoP, current US$)':
            Exports.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Goods imports (BoP, current US$)':
            GoodImp.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Service imports (BoP, current US$)':
            ServImp.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Households and NPISHs final consumption expenditure (% of GDP)':
            Household_expend.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Manufacturing, value added (current US$)':
            Manufacturing.append(datap.iloc[i,4:34].tolist())
        data.append(Country(country,GDP,Gross_national_expenditure,Final_consumption_expenditure ,Households_expend_capita,Gen_gov,Inflation,IncomeReceipt,Exports,GoodImp,ServImp,Household_expend,Manufacturing))
    else:
        if datap.iloc[i,2] == 'GDP (constant LCU)':
            data[compid].GDP.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Gross national expenditure (current US$)':
            data[compid].Gross_national_expenditure.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Final consumption expenditure (% of GDP)':
            data[compid].Final_consumption_expenditure.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Households and NPISHs Final consumption expenditure per capita growth (annual %)':
            data[compid].Households_expend_capita.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'General government final consumption expenditure (% of GDP)':
            data[compid].Gen_gov.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Inflation, consumer prices (annual %)':
            data[compid].Inflation.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Primary income receipts (BoP, current US$)':
            data[compid].IncomeReceipt.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Exports of goods and services (BoP, current US$)':
            data[compid].Exports.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Goods imports (BoP, current US$)':
            data[compid].GoodImp.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Service imports (BoP, current US$)':
            data[compid].ServImp.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Households and NPISHs final consumption expenditure (% of GDP)':
            data[compid].Household_expend.append(datap.iloc[i,4:34].tolist())
        elif datap.iloc[i,2] == 'Manufacturing, value added (current US$)':
            data[compid].Manufacturing.append(datap.iloc[i,4:34].tolist())
    
        
# print(data[0].Exports[0])
# print(80*"*")
# print(data[0].GoodImp[0])
# for i in range(len(data)):
#     print(data[i].country,i)


# '''Problem 2'''
    
US_gdp = data[0].GDP[0]
Russia_gdp = data[3].GDP[0]   

    
datax=[]
for i in range (len(Russia_gdp)): 
    datax.append(round(Russia_gdp[i],2))

outputy=[]
for i in range(len(US_gdp)):
    outputy.append(round(US_gdp[i],2))

print ( datax)
# print ('The dependent data is \n', outputy)

# graphx=[]
# for i in range(0,len(datax)):
#     graphx.append(datax[i])

# datax= sm.add_constant(datax,True)

# mod = sm.OLS(outputy,datax)
# model=mod.fit()
# print(model.summary())

# print('****************************************\nThe best linear model is ')
# print ('y = ',model.params[1], ' x + ', model.params[0])
# print('****************************************\n')

# newdatapoint=90000000000000
# prediction = model.params[1]*newdatapoint +model.params[0]
# print ('If Russia has $', newdatapoint,'in GDP in 2021, US will have an estimate of $', prediction, 'in 2021.')


# print('\nHere is the graph of the linear Regression:')
# minx=min(graphx)
# maxx=max(graphx)
# diffx=maxx-minx
# maxx+=.05*diffx
# minx-=.05*diffx
# linex=[minx, maxx]
# liney = [model.params[1]*minx +model.params[0], model.params[1]*maxx +model.params[0]]
# plt.figure()
# plt.scatter(graphx,outputy, color='black')
# plt.plot(linex, liney,linewidth=3,color='g')
# plt.ion()

# plt.show()


# print('Here is the graph of the residuals:')
# residualy=[]
# for i in range(0,len(graphx)):
#     residualy.append(outputy[i]-(model.params[1]*graphx[i]+model.params[0]))
# plt.figure()
# plt.scatter(graphx,residualy)
# plt.ion()
# plt.show()

# print ('The sum of the residuals is ', sum(residualy))
# print ('This sum should always be 0, which is a nice check')    
    
    
# '''PROBLEM 3'''    
# Mexico_gdp = data[1].GDP[0]    

# outputy=[]
# for i in range(len(US_gdp)):
#     outputy.append(round(US_gdp[i],2))

# # print ( datax)
# # print ('The dependent data is \n', outputy)

# graphx=[]
# for i in range(0,len(Mexico_gdp)):
#     graphx.append(Mexico_gdp[i])


# Mexico_gdp= sm.add_constant(Mexico_gdp,True)

# mod = sm.OLS(outputy,Mexico_gdp)
# model=mod.fit()
# print(model.summary())

# print('****************************************\nThe best linear model is ')
# print ('y = ',model.params[1], ' x + ', model.params[0])
# print('****************************************\n')

# newdatapoint=19000000000000
# prediction = model.params[1]*newdatapoint +model.params[0]
# print ('If Mexico has $', newdatapoint,'in GDP in 2021, US will have an estimate of $', prediction, 'in 2021.')


# print('\nHere is the graph of the linear Regression:')
# minx=min(graphx)
# maxx=max(graphx)
# diffx=maxx-minx
# maxx+=.05*diffx
# minx-=.05*diffx
# linex=[minx, maxx]
# liney = [model.params[1]*minx +model.params[0], model.params[1]*maxx +model.params[0]]
# plt.figure()
# plt.scatter(graphx,outputy, color='black')
# plt.plot(linex, liney,linewidth=3,color='g')
# plt.ion()

# plt.show()


# print('Here is the graph of the residuals:')
# residualy=[]
# for i in range(0,len(graphx)):
#     residualy.append(outputy[i]-(model.params[1]*graphx[i]+model.params[0]))
# plt.figure()
# plt.scatter(graphx,residualy)
# plt.ion()
# plt.show()

# print ('The sum of the residuals is ', sum(residualy))
# print ('This sum should always be 0, which is a nice check')     
    

# '''PROBLEM 4.'''
# datax = []
# outputy =[]
# outputy = data[0].GDP[0]

# # print(len(data[0].Gross_national_expenditure[0]))
# for i in range(0,len(data[0].Gross_national_expenditure[0])):
#     datax.append([data[0].Gross_national_expenditure[0][i], data[0].Final_consumption_expenditure[0][i], data[0].Households_expend_capita[0][i],data[0].Gen_gov[0][i],data[0].Inflation[0][i], data[0].IncomeReceipt[0][i], data[0].Exports[0][i],data[0].GoodImp[0][i],data[0].ServImp[0][i],data[0].Household_expend[0][i],data[0].Manufacturing[0][i]])# print (len(datax))
# datax = sm.add_constant(datax, True)
# model = sm.OLS(outputy, datax).fit()
# print(model.summary())


# startingvariablenames=[]
# for i in range (0,len(datax)):
#     startingvariablenames.append(i)

# print ( datax)
# print ('The dependent data is \n', outputy)

# alpha=.2
# constant=True
# maxp=1

# while maxp>alpha:
#     #copydata
#     copy=[]
#     for i in range(0,len(datax)):
#         temp=[]
#         for j in range(0,len(datax[i])):
#             temp.append(datax[i][j])
#         copy.append(temp)
#     if constant==True:
#         datax= sm.add_constant(datax,True)
#     mod = sm.OLS(outputy,datax)
#     model=mod.fit()
#     print(model.summary())
#     maxp=max(model.pvalues)
#     #This gets the position in the list of the max.
#     worstindex=np.argmax(model.pvalues)
#     if constant==True:
#         worstindex=worstindex-1
#     print('The p values are ', model.pvalues)
#     print ('The maximum p value is ', round(maxp,5) , ' occurring at x', worstindex)
#     print('This index is actually x', startingvariablenames[worstindex],' in the original')
#     if maxp>alpha and len(model.pvalues)>=2:
#         if worstindex ==0 and constant==True:
#             constant=False
#             print('Removing the Constant')
#             datax=[]
#             for i in range (0,len(copy)):   
#                 temp=[]
#                 for j in range(0,len(copy[i])):
#                     temp.append(copy[i][j])
#                 datax.append(temp)
#         else:
#             print ('Removing x', startingvariablenames[worstindex], ' from this model')
#             #If you have a big data, you could do this by poping if you had a different structure.  Just be careful
#             datax=[]
#             for i in range (0,len(copy)):
#                 temp=[]
#                 for j in range(0,len(copy[i])):
#                     if j !=worstindex:
#                         temp.append(copy[i][j])
#                 datax.append(temp)
#             #reset the names
#             for j in range(worstindex,len(startingvariablenames)-1):
#                 startingvariablenames[j]=startingvariablenames[j+1]
#             startingvariablenames.pop(-1)        
#     else:
#         #force and exit from the while loop
#         maxp=0
#         print('\n\nDone removing variables\n')
#         print('The remaining variables are ', startingvariablenames)
#         print('The recommended model is ')
#         a = str('y=')
#         shiftforconstant=0
#         if constant==True:
#             a+=str(round(model.params[0],3))
#             if (len(model.pvalues)>=2):
#                 for i in range (0,len(startingvariablenames)):
#                     a+= ' + '+str(round(model.params[i],3))+'x'+str(startingvariablenames[i])
#         else:
#             a+= str(model.params[0])+'x'+str(startingvariablenames[0]) 
#             # if (len(model.pvalues)>=2):
#             #     for i in range (0,len(startingvariablenames)):
#             #         a+= ' + '+str(round(model.params[i],3))+'x'+str(startingvariablenames[i])
#         print(a)
#         print('This does not mean that it is the best model, but you should')
#         print('eliminate more variables with caution!')