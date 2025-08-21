from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

# ​​ Input Data (Make sure all lists have equal lengths, here 14 items each)
weather = [
    'Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy',
    'Overcast', 'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast',
    'Overcast', 'Rainy'
]
temp = [
    'Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool',
    'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'
]
play = [
    'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes',
    'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No'
]

# ​​ Use separate LabelEncoders
le_weather = LabelEncoder()
le_temp = LabelEncoder()
le_play = LabelEncoder()

weather_encoded = le_weather.fit_transform(weather)
temp_encoded = le_temp.fit_transform(temp)
label = le_play.fit_transform(play)

print("weather encoded:", weather_encoded)
print("temp encoded:   ", temp_encoded)
print("play encoded:   ", label)

# ​​ Combine features properly
features = list(zip(weather_encoded, temp_encoded))
print("feature tuples:", features)

# Sanity check: must match lengths
print("Features length:", len(features))
print("Labels length:  ", len(label))

# ​​ Train the Gaussian Naive Bayes model
model = GaussianNB()
model.fit(features, label)

# ​​ Make a prediction
# Example: weather = 'Sunny', temp = 'Cool'
test_weather = 'Sunny'
test_temp = 'Cool'
test_feature = [
    le_weather.transform([test_weather])[0],
    le_temp.transform([test_temp])[0]
]

predicted = model.predict([test_feature])
predicted_label = le_play.inverse_transform(predicted)

print(f"Test feature: {test_weather, test_temp} -> Predicted play:", predicted_label[0])
                                                                                                                                                                                                                