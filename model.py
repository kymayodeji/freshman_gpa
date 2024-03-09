# Load Libraries
# Numeric
import numpy as np
import pandas as pd

# Model packages
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load data 
df = pd.read_csv("data/satgpa_cleaned.csv", sep=',')

# separate feature & target (freshman year gpa)
X = df.iloc[:, :-1].values
y = df.iloc[:, 1].values

# Splitting the data set into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 250)

# Fitting Simple Linear Regression to the Training set
lr = LinearRegression()
lr.fit(X_train, y_train)

# Dump to save the model
joblib.dump(lr, 'model.pkl')