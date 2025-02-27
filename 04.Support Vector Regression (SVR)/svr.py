# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 01:16:11 2018

@At Pabna
@author: Arnob
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, [2]].values  # [] is added because convert 1D array to 2D array


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)


# Fitting SVR to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X,y)

# Predicting  a new result
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]]))))

# Visualising the SVR result
plt.scatter(X,y, color= 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('SVR Lookup')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

# Visualising the SVR result
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X,y, color= 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('SVR Lookup (SVR Model)')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()
