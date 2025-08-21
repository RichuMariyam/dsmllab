import pandas as pd
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

# Step 1: Read Excel file
# (Assume your Excel file is "weather.xlsx" and has columns: Weather, Temp, Play)
df = pd.read_excel("weather_data.xlsx")

print("Dataset:\n", df)

# Step 2: Encode categorical columns
le = preprocessing.LabelEncoder()

weather_encoded = le.fit_transform(df['Weather'])
temp_encoded = le.fit_transform(df['Temperature'])
label = le.fit_transform(df['Play'])

print("Weather Encoded:", weather_encoded)
print("Temp Encoded:", temp_encoded)
print("Play Encoded:", label)

# Step 3: Combine features
features = list(zip(weather_encoded, temp_encoded))
print("Features:", features)

# Step 4: Train Naive Bayes
model = GaussianNB()
model.fit(features, label)

# Step 5: Predict a new sample (example: Weather=0, Temp=2)
predicted = model.predict([[0, 2]])
print("Predicted Value:", predicted)

# Step 6: Evaluate Model
y_pred = model.predict(features)

print("Accuracy:", accuracy_score(label, y_pred))
print("Precision:", precision_score(label, y_pred, average='binary'))
print("Recall:", recall_score(label, y_pred, average='binary'))
print("Confusion Matrix:\n", confusion_matrix(label, y_pred))