import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

# Load dataset
cancer_bunch = load_breast_cancer()
cancer = pd.DataFrame(cancer_bunch.data, columns=cancer_bunch.feature_names)

# Add target column with labels
cancer['target'] = cancer_bunch.target
cancer['target'] = cancer['target'].map({0: 'malignant', 1: 'benign'})

# Basic info
print("🔢 Shape of dataset:", cancer.shape)
print("\n📄 First 5 rows:")
print(cancer.head())

print("\n🧾 Info:")
print(cancer.info())

print("\n📊 Summary Statistics:")
print(cancer.describe())

print("\n❓ Missing Values:")
print(cancer.isnull().sum())

print("\n🔢 Class Distribution:")
print(cancer['target'].value_counts())

# 🎨 Pairplot (subset to avoid overload)
subset = cancer[['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'target']]
sns.pairplot(subset, hue='target', diag_kind='kde')
plt.suptitle("Pairplot of Selected Features", y=1.02)
plt.show()

# 🔥 Correlation Heatmap
plt.figure(figsize=(14, 10))
corr = cancer.drop('target', axis=1).corr()
sns.heatmap(corr, cmap="coolwarm", annot=False)
plt.title("Correlation Matrix of Features")
plt.show()

# 📦 Boxplot by class
plt.figure(figsize=(12, 6))
sns.boxplot(data=cancer.drop('target', axis=1), orient='h')
plt.title("Boxplot of Features")
plt.tight_layout()
plt.show()
