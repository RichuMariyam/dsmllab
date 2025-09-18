from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import datasets,linear_model
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import mean_squared_error,r2_score
df = pd.read_excel('regression_data.xlsx')  # Make sure this path is correct

# Use correct column names from the Excel file
X = df[['x_i (Aptitude Score)']]
y = df[['y_i (Statistics Grade)']]
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
print(x_train)
print(y_train)
clf=LinearRegression()
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)
print(y_pred)
newvalue=float(input("enter aptitude score:"))
y_pred=clf.intercept_+clf.coef_*newvalue
print(y_pred)
