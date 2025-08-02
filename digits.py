import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

# Load the digits dataset
digits_bunch = load_digits()
# digits data is 64 features (8x8 pixel values) per sample
digits = pd.DataFrame(digits_bunch.data)

# Add target column
digits['digit'] = digits_bunch.target

# Basic info
print("Shape of the dataset:", digits.shape)
print("\nFirst 5 rows:")
print(digits.head())

print("\nData types and Non-nulls:")
print(digits.info())

print("\nSummary Statistics:")
print(digits.describe())

print("\nMissing Values:")
print(digits.isnull().sum())

print("\nClass Distribution:")
print(digits['digit'].value_counts())

# Since the features are pixel intensities, pairplot is very large and not very informative here.
# Instead, visualize some sample images per digit:

fig, axes = plt.subplots(2, 5, figsize=(12, 5))
fig.suptitle("Sample Images of Digits (8x8 pixels)", fontsize=16)

for i, ax in enumerate(axes.flatten()):
    # Select first image of each digit class i
    img = digits_bunch.images[digits_bunch.target == i][0]
    ax.imshow(img, cmap='gray')
    ax.set_title(f"Digit: {i}")
    ax.axis('off')

plt.show()

# Correlation heatmap of pixel features (too big for 64 features, but let's do it anyway)
plt.figure(figsize=(14, 12))
sns.heatmap(digits.drop('digit', axis=1).corr(), cmap='coolwarm', square=True)
plt.title("Pixel Feature Correlation Matrix")
plt.show()

# Boxplot for pixel values - also large, so better to plot a subset
plt.figure(figsize=(14, 6))
sns.boxplot(data=digits.drop('digit', axis=1).iloc[:, :20], orient="h")  # first 20 pixels
plt.title("Boxplot for First 20 Pixel Features")
plt.show()
