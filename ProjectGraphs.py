# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 11:04:37 2021

@author: ahato
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import scipy
from scipy import stats
from six.moves import urllib
import zipfile
import seaborn as sns

import Database as db



quantities = []
defectives = []
costs = []
# print(db.suppliers[0].person)
for i in range(len(db.suppliers)):
    quantities.append(np.mean(db.suppliers[i].quantity))
    defectives.append(np.mean(db.suppliers[i].defective))
    costs.append(np.mean(db.suppliers[i].cost))
    
    
'''Means of Defectives for each Supplier'''    
sns.set(style ='darkgrid')
for i in range(len(db.suppliers)):
    plt.bar(i,defectives[i],edgecolor = 'black',)
plt.title("Means of Defectives for each Supplier",fontsize = 25, color = 'Black')
plt.ion()
plt.show()

'''Average Quantities for each Supplier'''    
for i in range(len(db.suppliers)):
    plt.bar(i,quantities[i],edgecolor = 'black',)
plt.title("Average Quantities for each Supplier",fontsize = 25, color = 'Black')
plt.ion()
plt.show()
    

'''Average Costs for each Supplier'''    
for i in range(len(db.suppliers)):
    plt.bar(i,costs[i],edgecolor = 'black',)
    
plt.title("Average Costs for each Supplier",fontsize = 25, color = 'Black')
plt.ion()
plt.show()
    


defectivess= np.argsort(defectives)
print(defectivess)

