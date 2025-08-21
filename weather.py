weather = ['sunny','overcast','rainy','rainy','rainy','overcast','sunny','sunny','rainy','sunny','overcast','overcast','rainy']
temp = ['hot','hot','hot','mild','cool','cool','cool','mild','cool','mild','mild','mild','hot']
play = ['no','no','yes','yes','yes','yes','no','yes','no','yes','yes','yes','yes']

from heapq import merge
from typing import List
from sklearn import preprocessing

# Use separate encoders
le_weather = preprocessing.LabelEncoder()
le_temp = preprocessing.LabelEncoder()
le_play = preprocessing.LabelEncoder()

weather_encoded = le_weather.fit_transform(weather)
print("weather:", weather_encoded)

temp_encoded = le_temp.fit_transform(temp)
print("temp:", temp_encoded)

label = le_play.fit_transform(play)
print("play:", label)

features = list(zip(weather_encoded, temp_encoded))
print(features)

from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(features, label)

# Predicting for: weather=0 ('overcast'), temp=2 ('mild') based on encoding
predicted = model.predict([[0, 2]])
print("Predicted value:", predicted)
print(le_play.inverse_transform(predicted))
