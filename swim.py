swim=['FAST','FAST','SLOW','FAST','NO','NO','NO','SLOW','SLOW','SLOW','NO','FAST']
fly=['NO','NO','NO','NO','SHORT','SHORT','RARELY','NO','NO','NO','LONG','NO']
headache=['MILD','NO','STRONG','MILD','NO','STRONG','STRONG','MILD']
crawl=['NO','YES','NO','NO','NO','NO','NO','YES','NO','YES','NO','NO']
classes=['FISH','ANIMAL','ANIMAL','ANIMAL','BIRD','BIRD','ANIMAL','ANIMAL','FISH','FISH','BIRD','BIRD']

from heapq import merge

from sklearn import preprocessing

from sklearn.naive_bayes import GaussianNB

le=preprocessing.LabelEncoder()
swim_encoded = le.fit_transform(swim)
print("swim_encoded:",swim_encoded)
fly_encoded = le.fit_transform(fly)
print("fly_encoded:",fly_encoded)

crawl_encoded = le.fit_transform(crawl)
print("crawl_encoded:",crawl_encoded)
classes_encoded = le.fit_transform(classes)
print("classes_encoded:",classes_encoded)

features = list(zip(swim_encoded, fly_encoded, crawl_encoded))
print(features)

from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(features, classes_encoded)


predicted = model.predict([[0,2,0]])
print("Predicted value:", predicted)
print(le.inverse_transform(predicted))
