import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_linnerud

# Load the Linnerud dataset
linnerud = load_linnerud(as_frame=True)
X = linnerud.data       # Exercise data (independent variables)
y = linnerud.target     # Physiological data (dependent variables)

# Combine features and target into one DataFrame
data = pd.concat([X, y], axis=1)

# Show dataset overview
print("🔢 Shape of the dataset:", data.shape)
print("\n📄 First 5 rows:")
print(data.head())

print("\n🧾 Data types and info:")
print(data.info())

print("\n📊 Summary Statistics:")
print(data.describe())

print("\n❓ Missing Values:")
print(data.isnull().sum())

# 💡 Pairplot of full dataset
sns.pairplot(data)
plt.suptitle("Pairplot of Linnerud Dataset (Exercise vs Physiology)", y=1.02)
plt.show()

# 🔥 Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# 📦 Boxplot of exercise features
plt.figure(figsize=(8, 4))
sns.boxplot(data=X)
plt.title("Boxplot of Exercise Features")
plt.show()

# 📦 Boxplot of physiological targets
plt.figure(figsize=(8, 4))
sns.boxplot(data=y)
plt.title("Boxplot of Physiological Features")
plt.show()
