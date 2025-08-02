import pandas as pd 
import numpy as np 
import seaborn as sns  
import matplotlib.pyplot as plt 
from sklearn.datasets import load_wine

# Load the wine dataset
wine_bunch = load_wine()
wine = pd.DataFrame(wine_bunch.data, columns=wine_bunch.feature_names)

# Add target as a new column and map target names
wine['wine_class'] = wine_bunch.target
wine['wine_class'] = wine['wine_class'].map(dict(enumerate(wine_bunch.target_names)))

# Basic information
print("Shape of the dataset:", wine.shape)
print("\nFirst 5 rows:")
print(wine.head())

print("\nData types and Non-nulls:")
print(wine.info())

print("\nSummary Statistics:")
print(wine.describe())

print("\nMissing Values:")
print(wine.isnull().sum())

print("\nClass Distribution:")
print(wine['wine_class'].value_counts())

# Pairplot
sns.pairplot(wine, hue='wine_class', diag_kind='kde')
plt.suptitle("Pairplot of Wine Features", y=1.02)
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(wine.drop('wine_class', axis=1).corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Matrix")
plt.show()

# Boxplot for each feature
plt.figure(figsize=(12, 6))
sns.boxplot(data=wine.drop('wine_class', axis=1), orient="h")
plt.title("Boxplot for Each Feature")
plt.show()
