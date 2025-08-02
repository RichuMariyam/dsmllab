from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
irisdata=load_iris()
x=irisdata.data
y=irisdata.target
print("X values")
print(x)
print("Y values")
print(y)
x_train,x_test,y_train,y_test=train_test_split(x,y)

print("x Train Values")
print(x_train)
print("x Test Values")
print(x_test)
print("Y Train Values")
print(y_train)
print("Y Test Values")
print(y_test)