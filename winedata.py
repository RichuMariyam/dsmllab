from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

# Load the Wine dataset
winedata = load_wine()
x = winedata.data
y = winedata.target

# Display the dataset
print("X values (features):")
print(x)

print("\nY values (target labels):")
print(y)

# Split into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

# Display train/test data
print("\nX Train values:")
print(x_train)

print("\nX Test values:")
print(x_test)

print("\nY Train values:")
print(y_train)

print("\nY Test values:")
print(y_test)
