import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes

# Load the diabetes dataset
diabetes_bunch = load_diabetes()
diabetes = pd.DataFrame(diabetes_bunch.data, columns=diabetes_bunch.feature_names)

# Add target column (continuous numeric value)
diabetes['disease_progression'] = diabetes_bunch.target

# Basic info
print("Shape of the dataset:", diabetes.shape)
print("\nFirst 5 rows:")
print(diabetes.head())

print("\nData types and Non-nulls:")
print(diabetes.info())

print("\nSummary Statistics:")
print(diabetes.describe())

print("\nMissing Values:")
print(diabetes.isnull().sum())

# Since it's regression, no class distribution, but let's see target stats
print("\nTarget (disease_progression) statistics:")
print(diabetes['disease_progression'].describe())

# Pairplot (to see relationships)
sns.pairplot(diabetes)
plt.suptitle("Pairplot of Diabetes Features", y=1.02)
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(diabetes.corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Matrix (including target)")
plt.show()

# Boxplot for features
plt.figure(figsize=(12, 6))
sns.boxplot(data=diabetes.drop('disease_progression', axis=1), orient="h")
plt.title("Boxplot for Each Feature")
plt.show()
