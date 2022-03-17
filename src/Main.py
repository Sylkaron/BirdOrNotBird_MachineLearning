import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

df=pd.read_csv("../Ressources/spectre.csv",index_col='itemid').sort_index()

freq=range(0,20000,100)

X=df[[str(i) for i in freq]]

y=df['hasBird']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

clf_lr = LogisticRegression(solver='lbfgs')

clf_lr.fit(X_train,y_train)

train_score = clf_lr.score(X_train,y_train)
test_score = clf_lr.score(X_test,y_test)
cross_val=cross_val_score(clf_lr,X,y,cv=7)



