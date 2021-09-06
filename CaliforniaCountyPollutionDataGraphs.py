# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 21:23:21 2021

@author: ahato
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib
import squarify

datap = pd.read_excel(r'CaliforniaCountyDailyPolution.xlsx', 'PolutionData')

class Pollution(object):
  def __init__(self,county,ozonepct,dieselpct,waterpct,trafficpct,groundpct):
      self.county = county
      self.ozonepct = ozonepct
      self.dieselpct = dieselpct
      self.waterpct = waterpct
      self.trafficpct = trafficpct
      self.groundpct = groundpct
      

def findcounty(data, county):
    for i in range(0,len(data)):
        if data[i].county==county:
            compid=i
            return(compid)
    return(-1)  
'''PROBLEM 1'''    
data = []

for i in range(len(datap)):
    county = datap.iloc[i,0]
    compid = findcounty(data,county)
    if compid==-1:
        ozonepct = [datap.iloc[i,3]]
        dieselpct = [datap.iloc[i,7]]
        waterpct = [datap.iloc[i,9]]
        trafficpct = [datap.iloc[i,15]]
        groundpct = [datap.iloc[i,19]]
        data.append(Pollution(county,ozonepct,dieselpct,waterpct,trafficpct,groundpct))
    else:
        data[compid].ozonepct.append(datap.iloc[i,3])
        data[compid].dieselpct.append(datap.iloc[i,7])
        data[compid].waterpct.append(datap.iloc[i,9])
        data[compid].trafficpct.append(datap.iloc[i,15])
        data[compid].groundpct.append(datap.iloc[i,19])
    


'''PROBLEM2'''

counties = []
mean_data = []
percent = []
for i in range(0,len(data)):
    counties.append(data[i].county)
    percent.append(data[i].dieselpct)
    mean = np.mean(percent[i])
    mean_data.append(mean)
percent = percent[:13]
mean_data = mean_data[:13]
counties = counties[:13]
print(counties,len(counties))


'''1. Bar'''    
for i in range(len(data)):
    print(data[i].county,data[i].dieselpct)
    plt.bar(data[i].county,data[i].dieselpct, edgecolor = 'black')
plt.xlabel('Counties', fontsize = 18, color = 'Purple')
plt.ylabel("Percentile %", fontsize = 18, color = 'Purple')
plt.title("Distribution of the Diesel Percentile", fontsize = 25, color = 'Green')
plt.xticks(rotation = 90)
plt.show()

'''2. Pie chart'''
sns.set(style ='darkgrid')
plt.title("Averages of the Diesel Percentile",fontsize = 25, color = 'Green')
plt.pie(mean_data, labels = counties, wedgeprops = {'linewidth': 2})
plt.show()


'''3. Violin plot'''
ticks = range(1,len(counties)+1)
sns.violinplot(data = percent,palette = ["b", "0.85"], split=True, inner="quart", cut = 1, linewidth=1,edgecolor = 'black')
plt.title("Distribution of the Diesel Percentile",fontsize = 25, color = 'Green')
plt.xticks(ticks = ticks, labels = counties, rotation = 90)
plt.xlabel('Counties', fontsize = 18, color = 'Purple')
plt.show()

'''4. Strip plot'''
ticks = range(1,len(counties)+1)
sns.set(style = 'darkgrid')
sns.stripplot( data=percent,size=4, color="purple", linewidth=1, alpha = 0.5)
plt.title("Distribution of the Diesel Percentile",fontsize = 25, color = 'Green')
plt.xticks(ticks = ticks,labels = counties, rotation = 90)
plt.xlabel('Counties', fontsize = 18)
plt.show()


'''5. Box plot'''
ticks = range(1,len(counties)+1)
sns.set(style = 'darkgrid')
sns.boxplot(data = percent, palette=["m", "g"])
plt.title("Distribution of the Diesel Percentile",fontsize = 25, color = 'Green')
plt.xticks(ticks = ticks,labels = counties, rotation = 90)
plt.xlabel('Counties', fontsize = 18, color = 'Purple')
plt.show()

'''6. Lollipop Plot'''
# plt.figure(figsize = (10,6))
plt.stem(mean_data)
plt.title("Averages of the Diesel Percentile",fontsize = 25, color = 'Green')
plt.xticks(ticks = ticks,labels = counties,rotation = 45, ha = 'right')
# plt.setp( ax.xaxis.get_majorticklabels(), rotation=-45, )
(markers, stemlines, baseline) = plt.stem(mean_data)
plt.setp(markers, marker='D', markersize=10, markeredgecolor="orange", markeredgewidth=2)
plt.show()




'''Problem 3'''
orntraffic = data[4].trafficpct
orndiesel = data[4].dieselpct
ornozone = data[4].ozonepct
ornwater = data[4].waterpct
ornground = data[4].groundpct
pollute = [orndiesel,ornozone,ornwater,ornground,orntraffic]

means = [np.mean(orndiesel),np.mean(ornozone),np.mean(ornwater),np.mean(ornground),np.mean(orntraffic)]
labels = ["Diesel","Ozone","Drinking Water","Groundwater", "Traffic"]
print(means)
'''1. Pie chart'''
sns.set(style ='darkgrid')
plt.title("Averages of the data of Orange county",fontsize = 25, color = 'Green')
plt.pie(means, labels =labels , wedgeprops = {'linewidth': 2})
plt.show()



'''2. Lollipop Plot'''
ticks = range(1,len(labels)+1)
# plt.figure(figsize = (10,6))
plt.stem(means, label = '0 = Diesel, 1 = Ozone\n2 = Drinking Water, 3 = Ground Water\n4 = Traffic' )
plt.title("Averages of the data of Orange county",fontsize = 25, color = 'Green')
(markers, stemlines, baseline) = plt.stem(means)
plt.setp(markers, marker='D', markersize=10, markeredgecolor="orange", markeredgewidth=2)
plt.legend(loc="upper left")
plt.show()



'''3. Line plot'''
sns.set(style = "darkgrid")
sns.scatterplot(data = orntraffic, palette=["m", "g"], label = "Traffic")
# sns.lineplot(data = orndiesel, palette=["m", "g"], label = "Diesel", linestyle = "dashed")
plt.title("Distribution of the Traffic and Diesel Percentiles on Orange County",fontsize = 25, color = 'Green')
plt.legend()
plt.show()




'''4. Bar'''
y_pos = np.arange(len(labels))
plt.bar(y_pos, means,edgecolor='black', color=['grey', 'tan', 'darkseagreen', 'teal', 'royalblue'])
plt.xticks(y_pos, labels, rotation = 45)
plt.title("Distribution of the Traffic and Diesel Percentiles on Orange County",fontsize = 25, color = 'Green')

plt.show()



'''5. Scatter plot'''
plt.scatter(labels,means, color = ['red', 'orange', 'purple', 'cyan', 'blue'])
plt.title("Averages of the data of Orange county",fontsize = 25, color = 'Green')
plt.show()

'''6. Treemap plot'''
cmap = matplotlib.cm.Blues
mini=min(means)
maxi=max(means)
norm = matplotlib.colors.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in means]
squarify.plot(sizes=means, label=labels, alpha=.8,color=colors, bar_kwargs={'alpha':.7}, text_kwargs={'fontsize':11, 'weight':'bold'})
plt.axis('off')
plt.title("Averages of the data of Orange county",fontsize = 25, color = 'Green')
plt.show()










