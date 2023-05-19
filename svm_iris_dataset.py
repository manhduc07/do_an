# -*- coding: utf-8 -*-
"""SVM_Iris_Dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11J8Kh6gs8m1vK991I4EELdo45sqGrz2H

Các thư viện
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
import plotly.figure_factory as ff
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
# %matplotlib inline

"""Đọc dữ liệu Iris"""

iris=pd.read_csv('IRIS.csv')
iris.head()

iris.describe()

iris['species'].value_counts()

iris.plot(kind="scatter", x="sepal_length", y="sepal_width")

sns.pairplot(data=iris, hue='species', palette='Set2')

"""Chia dữ liệu train và test"""

x=iris.iloc[:,:-1]
y=iris.iloc[:,4]
x_train,x_test, y_train, y_test=train_test_split(x,y,test_size=0.30)

"""Đào tạo mô hình và dự đoán tập dữ liệu test"""

model=SVC()
model.fit(x_train, y_train)
pred=model.predict(x_test)

"""Confusion Matrix"""

fig = ff.create_annotated_heatmap(z=confusion_matrix(y_test,pred), x=list(range(3)), y=list(range(3)), colorscale='Blues')
fig.show()

"""Classification Report"""

print(classification_report(y_test, pred))