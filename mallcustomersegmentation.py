# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:33:08 2020

@author: ramravi
"""

#importing the necessary libraries

import pandas as pd
import numpy as np
import seaborn as sns
from pandas import plotting

#for visualization
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')

#for interactive visualizations
import plotly.offline as py
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go
from plotly import tools
init_notebook_mode(connected=True)
import plotly.figure_factory as ff

#importing the dataset
data= pd.read_csv('mallcustomersegmentation.csv')

dat=ff.create_table(data.head())

py.iplot(dat)


data.describe()

#checking if there is null data
data.isnull().any().any()

#plotting the andrews_curve
plt.rcParams['figure.figsize']=(15,10)

plotting.andrews_curves(data.drop('CustomerID', axis=1), 'Gender')
plt.title('Andrew curves for gender', fontsize=20)
plt.show()

# the andrews curve preserves the means, distance(up to a constant) adn variances. 

import warnings
warnings.filterwarnings('ignore')

plt.rcParams['figure.figsize']=(18,8)

plt.subplot(1,2,1)
sns.set(style='whitegrid')
sns.distplot(data['Annual Income (k$)'])
plt.title('annual income distribution', fontsize=20)
plt.xlabel('Range of Annual Income')
plt.ylabel('Count')

plt.subplot(1,2,2)
sns.set(style='whitegrid')
sns.distplot(data['Age'], color='red')
plt.title('Distribution of Age', fontsize=20)
plt.xlabel('Range of age')
plt.ylabel('count')

# we can infer one thing that There are few people who earn more than 100 US Dollars. Most of the people have an earning of around 50-75 US Dollars. Also, we can say that the least Income is around 20 US Dollars.
 
# Taking inferences about the Customers.

# The most regular customers for the Mall has age around 30-35 years of age. Whereas the the senior citizens age group is the least frequent visitor in the Mall. Youngsters are lesser in umber as compared to the Middle aged people.


labels=['Female','Male']
size=data['Gender'].value_counts()
colors=['lightgreen', 'orange']
explode=[0,0.1]

plt.rcParams['figure.figsize']=(9,9)
plt.pie(size, explode=explode, labels=labels, autopct='%.2f%%', shadow=True)
plt.title('Gender Pie distribution')
plt.axis('off')
plt.legend()
plt.show()

#if you can see the pie chart, it is clear that female gender leads the male count by atleast 56%
# that is a huge gap specially when the population of Males is comparatively higher than females

plt.rcParams['figure.figsize'] = (15, 8)
sns.countplot(data['Age'], palette = 'hsv')
plt.title('Distribution of Age', fontsize = 20)
plt.show()

#This graph shows a more interactive chart about the distribution of each Age grou in the mall.
#it is seen that the ages from 27 to 39 are very much frequent but there is no clear pattern. Interesting Fact, There are equal no. of Visitors in the Mall for the Agee 18 and 67. People of Age 55, 56, 69, 64 are very less frequent in the Malls. People at Age 32 are the Most Frequent Visitors in the Mall.


plt.rcParams['figure.figsize']=(15,8)
sns.countplot(data['Annual Income (k$)'], palette='hsv')
plt.title('Distribution of Annual Income', fontsize=25)
plt.show()

#Interesting Fact, There are equal no. of Visitors in the Mall for the Agee 18 and 67. People of Age 55, 56, 69, 64 are very less frequent in the Malls. People at Age 32 are the Most Frequent Visitors in the Mall.

plt.rcParams['figure.figsize']=(15,8)
sns.countplot(data['Spending Score (1-100)'], palette='copper')
plt.title('Distribution of Spending score', fontsize=25)
plt.show()

#this is the most important chart of all. 
#This shows that the mall has a variety of customers coming in since the chart here shows a spending score from 1 till 99. This shoes that the mall caters to the needs of different class of poeple. However, the most cutomers spending score lies between 35-60.

sns.pairplot(data)
plt.title('Paiplot for the data', fontsize=20)
plt.show()

# This shows the relationship between each feature variable with itself and with the other variables in the table. This helps in finding the hidden relationship between the chosen variable(target) and the other important features selected.

plt.rcParams['figure.figsize']=(15,8)
sns.heatmap(data.corr(), cmap='Wistia', annot=True)
plt.title('Correlation matrix')
plt.show()

#If you can see the matrix, the features does not have any good correlation, thus proceeding with all the features.

#Bi-Variate Analysis

plt.rcParams['figure.figsize']=(15,8)
sns.boxenplot('Gender','Spending Score (1-100)',data=data,palette='Blues')
plt.title('Bi-Variate Analysis of gender and spending score')
plt.show()


#This shows the spending score of male is around 25k to 70k whearas the female gender has a spending score of 35k to 75k.This shows the clear domination of female gender in the shopping arena!

plt.rcParams['figure.figsize']=(15,8)
sns.boxplot('Gender', 'Annual Income (k$)', data=data, palette='rainbow')
plt.title('Bivariate analysis Gender vs Annual Income', fontsize=20)
plt.show()

#This is that the male has higher average salary than the female gender, while if you compare lower income, both the gender is almost equal.

x=data['Annual Income (k$)']
y=data['Age']
z=data['Spending Score (1-100)']

sns.lineplot(x,y,color='blue')
sns.lineplot(x,z,color='pink')
plt.title('Multivariate anaysis of age vs annual income vs spending score')
plt.show()

#the above chart shows the relationship between age and annula income and also annual income and spending score.

#Clustering analysis
x=data.iloc[:,[3,4]].values


#k means Algorithm

#elbow method to find the number of optimum clusters
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    km=KMeans(n_clusters=i, init='k-means++',max_iter=300,
              n_init=10, random_state=0)
    km.fit(x)
    wcss.append(km.inertia_)
    
plt.plot(range(1,11), wcss)
plt.title('The elbow method', fontsize=20)
plt.xlabel('No of clusters')
plt.ylabel('wcss')
plt.show()

#visualizing the clusters
km=KMeans(n_clusters=5, init='k-means++', max_iter=300,
          n_init=10, random_state=0)
y_means=km.fit_predict(x)

plt.scatter(x[y_means==0,0], x[y_means==0,1], 
            s=100, c='pink', label='misser')
plt.scatter(x[y_means==1,0], x[y_means==1,1], s=100, c='yellow',
            label='general')
plt.scatter(x[y_means==2,0], x[y_means==2,1], s=100, c='cyan', 
            label='target')
plt.scatter(x[y_means==3,0], x[y_means==3,1], s=100, c='magenta',
            label='spendthrift')
plt.scatter(x[y_means==4,0], x[y_means==4,1],s=100, c='orange',
            label='careful')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1], s=50, c='blue', label='centeriod')


plt.style.use('fivethirtyeight')
plt.title('K means Clsutering', fontsize=20)
plt.xlabel('Annaul Income')
plt.ylabel('Spending score')
plt.legend()
plt.grid()
plt.show()


#there are five segments in the mall and the label explains them in breifly.The mall authorities have to take care of the careul categories to avail some benefits so that they move to the general category.


#Hierarchial Clustering

#using dendograms

import scipy.cluster.hierarchy as sch
dendogram=sch.dendrogram(sch.linkage(x, method='ward'))
plt.title('dendogram',fontsize=20)
plt.xlabel('customers')
plt.ylabel('Ecuclidian Distance')
plt.show()




from sklearn.cluster import AgglomerativeClustering

hc=AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
y_hc=hc.fit_predict(x)

plt.scatter(x[y_hc==0,0], x[y_hc==0,1], s=100, c='pink', label='misser')
plt.scatter(x[y_hc==1,0], x[y_hc==1,1], s=100, c='yellow', label='general')
plt.scatter(x[y_hc==2,0], x[y_hc==2,1], s=100, c='orange', label='target')
plt.scatter(x[y_hc==3,0], x[y_hc==3,1], s=100, c='magenta', label='spendthrift')
plt.scatter(x[y_hc==4,0], x[y_hc==4,1], s=100, c='cyan', label='careful')
plt.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:,1], s=100, c='blue',label='centroid')

plt.style.use('fivethirtyeight')
plt.title('Cluster analysis-hierarchial Clustering', fontsize=20)
plt.xlabel('Annual income')
plt.ylabel('spending score (1-100)')
plt.legend()
plt.grid()
plt.show()

#age and spending score:
    
    
x= data.iloc[:,[2,4]].values

wcss=[]
for i in range(1,11):
    km=KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=300, random_state=0)
    km.fit(x)
    wcss.append(km.inertia_)
    
plt.plot(range(1,11),wcss)
plt.title('The elbow method', fontsize=20)
plt.xlabel('No of clusters')
plt.ylabel('wcss')
plt.show()

km=KMeans(n_clusters=4, init='k-means++', max_iter=300,
          n_init=10, random_state=0)
y_means=km.fit_predict(x)

plt.scatter(x[y_means==0,0], x[y_means==0,1], 
            s=100, c='pink', label='target customer')
plt.scatter(x[y_means==1,0], x[y_means==1,1], s=100, c='yellow',
            label='priority')
plt.scatter(x[y_means==2,0], x[y_means==2,1], s=100, c='cyan', 
            label='usual customer')
plt.scatter(x[y_means==3,0], x[y_means==3,1], s=100, c='magenta',
            label='target old customer')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1], s=50, c='blue', label='centeriod')


plt.style.use('fivethirtyeight')
plt.title('K means Clustering', fontsize=20)
plt.xlabel('Age')
plt.ylabel('Spending score')
plt.legend()
plt.grid()
plt.show()

#the age and spending score by looking at the above chart, we have the usual customer spread over all ages. And we also have the target customers with young and old ages.Then after getting the results we can accordingly make different marketing strategies and policies to optimize the spending scores of the customer in the Mall.

x=data[['Age','Spending Score (1-100)', 'Annual Income (k$)']].values
km=KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init= 10, random_state=0)
km.fit(x)
labels=km.labels_
centroids=km.cluster_centers_

data['labels']= labels
trace1= go.Scatter3d(
    x= data['Age'],
    y=data['Spending Score (1-100)'],
    z=data['Annual Income (k$)'],
    mode='markers',
    marker=dict(
        color=data['labels'],
        size=10,
        line=dict(
            color=data['labels'],
            width=12
            ),
        opacity=0.8
        )
    )
df=[trace1]

layout= go.Layout(
    title='Character vs Gender vs Alive or not',
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
        ),
    scene=dict(
        xaxis=dict(title='Age'),
        yaxis=dict(title='Spending Score'),
        zaxis=dict(title='Annual Income')
        )
    )
fig=go.Figure(data=df, layout=layout)
py.offline.plot(fig)

# this is a multivariate analysis of age vs annual income vs spending score.





















































































































































