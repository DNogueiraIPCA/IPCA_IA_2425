# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 16:12:01 2022

@author: Daniel Nogueira

from matplotlib import pyplot as plt
fig, ax = plt.subplots(figsize=(6, 6)) #figsize value changes the size of plot
tree.plot_tree(clf,ax=ax,feature_names=['sepal length','sepal width','petal length','petal width'])
plt.show()

https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html

"""

from sklearn.datasets import load_iris
from sklearn import tree
import graphviz 

# Load dataset 
iris = load_iris()
print("As classes possiveis são " + str(list(iris.target_names)))

# Dataset split (Input - X and Output - Y)
X = iris.data
y = iris.target

# Building Decision Tree
'''
Cria um classificador de árvore de decisão com alguns parâmetros. 
- O parâmetro criterion define a medida de impureza usada para dividir os nós 
da árvore (neste caso, "entropia"). 
- max_depth define a profundidade máxima da árvore
- min_samples_leaf especifica o número mínimo de amostras necessárias em um nó folha.
'''
clf = tree.DecisionTreeClassifier(criterion='entropy',
                                  max_depth=4, 
                                  min_samples_leaf=4)
# criterion defines the impurity measure used to split the nodes of the tree ("entropy")
# max_depth represents max level allowed in each tree 
# min_samples_leaf minumum samples storable in leaf node

# Fit the tree to iris dataset
clf.fit(X,y)

# Plot decision tree
'''
Gera uma representação em formato DOT da árvore de decisão treinada. 
Isso é feito com o auxílio da função export_graphviz da biblioteca tree. 
Os parâmetros especificam: nomes de recursos, nomes de classes e que o gráfico 
gerado deve ser preenchido, arredondado e conter caracteres especiais.
'''
dot_data = tree.export_graphviz(clf, out_file=None, 
                     feature_names=iris.feature_names,  
                     class_names=iris.target_names,  
                     filled=True,
                     rounded=True,  
                     special_characters=True)  
graph = graphviz.Source(dot_data)  
graph 


##############################################################################
clf2 = tree.DecisionTreeClassifier(criterion='gini',
                                   max_depth=4,
                                   min_samples_leaf=4)

clf2.fit(X,y)
dot_data2 = tree.export_graphviz(clf2, out_file=None,
                                 feature_names=iris.feature_names,  
                                 class_names=iris.target_names,  
                                 filled=True, 
                                 rounded=True,  
                                 special_characters=True)  
graph2 = graphviz.Source(dot_data2)  
graph2 


