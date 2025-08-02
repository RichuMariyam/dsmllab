import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load Titanic dataset from seaborn
titanic = sns.load_dataset("titanic")

# Preview data
print("🔢 Shape:", titanic.shape)
print("\n📄 First 5 rows:")
print(titanic.head())

print("\n🧾 Info:")
print(titanic.info())

print("\n📊 Summary Statistics:")
print(titanic.describe(include='all'))

print("\n❓ Missing Values:")
print(titanic.isnull().sum())

print("\n🔢 Class Distribution (Survival):")
print(titanic['survived'].value_counts())

# Plots
sns.countplot(data=titanic, x='sex', hue='survived')
plt.title("Survival by Gender")
plt.show()

sns.countplot(data=titanic, x='class', hue='survived')
plt.title("Survival by Passenger Class")
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(titanic.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Data Heatmap")
plt.show()

numeric_data = titanic.select_dtypes(include='number')
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()
