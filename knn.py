from mlxtend.plotting import plot_decision_regions
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import warnings
warnings.filterwarnings('ignore')

#plt.style.use('ggplot')
#ggplot is R based visualisation package that provides better graphics with higher level of abstraction
diabetes_data = pd.read_csv('D://ug/dataset/diabetes.csv')
print(diabetes_data.head())
y = diabetes_data.Outcome
X = diabetes_data.drop("Outcome",axis = 1)
print(X)
print(y)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=1/3,random_state=42, stratify=y)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=1/3,random_state=42, stratify=y)

from sklearn.neighbors import KNeighborsClassifier

test_scores = []
train_scores = []

knn = KNeighborsClassifier(11)

knn.fit(X_train,y_train)
print(knn.score(X_test,y_test))