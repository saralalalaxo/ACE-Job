#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 15:27:48 2022

@author: felixlee
"""

#Question 1
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("/Users/felixlee/Desktop/Jobs and Qualifications/PreScreen_r3/ingredient.csv", index_col= False); df

#a)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df.describe())

sns.heatmap(df.corr())
    
#b) Done in R

#c) Aim: Find the optimum number of distinctive dataset 

import sklearn as sk
import random
from sklearn.cluster import KMeans

#Data set
#X = df.iloc[:,:] ; X

X = np.concatenate(np.array([df['a'],df['b'],df['c'],df['d'],df['e'],df['f'],df['g'],df['h'],df['i']])) 

#Convert them to numericals


#Labels before kmeans clustering
y = [np.repeat(letter,len(df[letter])) for letter in df.columns]
#Randomising data set
#random.shuffle(X)

colnames = list(df.columns) ; colnames

#I will be using random seed to reproduce the exact clusters again. Random state= 0

kmeans = KMeans(n_clusters=9, random_state=0).fit(X)
identified_clusters = kmeans.fit_predict(X)


identified_clusters



data_with_clusters = df.copy()
data_with_clusters['Clusters'] = identified_clusters 
plt.scatter(data_with_clusters['a'],data_with_clusters['b'],data_with_clusters['c'],data_with_clusters['d'],data_with_clusters['e'],data_with_clusters['f'],data_with_clusters['g'],data_with_clusters['h'],data_with_clusters['i'],c=data_with_clusters['Clusters'],cmap='rainbow')


#Choosing a good number of clusters: Using the elbow method


'''
Reference:
https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
https://www.analyticsvidhya.com/blog/2021/04/k-means-clustering-simplified-in-python/#:~:text=Step%2D1%3A%20Select%20the%20value,will%20form%20the%20predefined%20clusters.
'''

#Question 2
'''
Aim: Investigate the fluctuating yield of oil palm trees, want to analyse on how external factors influence fresh fruit bunch yield

- Palm oil is extracted from FFB by a mechanical process


'''

df1 = pd.read_csv("/Users/felixlee/Desktop/Jobs and Qualifications/PreScreen_r3/palm_ffb.csv")
df1.describe()
sns.pairplot(df1) #checking all combinations of correlation graphs to see which is worth looking into 
plt.show() 
 
#3D graph
fig = plt.figure()
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')
 
# defining all 3 axes
z = df1["FFB_Yield"].values
x = df1["SoilMoisture"].values
y = df1["Precipitation"].values

# plotting
ax.scatter(x, y, z)
ax.set_title('3D line plot')
ax.set_xlabel('Soil Moisture')
ax.set_ylabel('Precipitation')
ax.set_zlabel('FFB Yield')

plt.show()



'''
Reference:
https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe    

'''








        

