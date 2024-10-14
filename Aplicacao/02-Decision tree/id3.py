# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:49:29 2022

@author: fonte
"""

import pandas as pd

data=pd.read_csv('./data/tennis.csv')
data
label=data.play

from sklearn.preprocessing import LabelEncoder

outlook=LabelEncoder ()
temp=LabelEncoder ()
humidity=LabelEncoder ()
windy=LabelEncoder ()
play=LabelEncoder ()

data['outlook']=outlook.fit_transform(data['outlook'])
data['temp']=outlook.fit_transform(data['temp'])
data['humidity']=outlook.fit_transform(data['humidity'])
data['windy']=outlook.fit_transform(data['windy'])
data['play']=outlook.fit_transform(data['play'])

data

features_cols=['outlook','temp','humidity','windy']
X=data[features_cols]
y=data.play


#from sklearn.model_selection import train_test_split
#x_train, x_test, y_train,y_test=train_test_split(X,y,test_size=0.2)


from sklearn.tree import DecisionTreeClassifier
#build decision tree
clf = DecisionTreeClassifier(criterion='gini')
#max_depth represents max level allowed in each tree, min_samples_leaf minumum samples storable in leaf node

#fit the tree to iris dataset
clf.fit(X,y)

import graphviz 
from sklearn import tree

#plot decision tree
dot_data = tree.export_graphviz(clf, out_file=None, 
                     feature_names=features_cols,  
                     class_names=label,  
                     filled=True, rounded=True,  
                     special_characters=True)  
graph = graphviz.Source(dot_data)  
graph 