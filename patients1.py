from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB

# Step 1: Input data
chills = ['Y','Y','Y','N','N','N','N','Y']
runningnose = ['N','Y','N','Y','N','Y','Y','Y']
headache = ['MILD','NO','STRNG','MILD','NO','STRONG','STRONG','MILD']
fever = ['Y','N','Y','Y','N','Y','N','Y']
hasflu = ['N','Y','Y','Y','N','Y','N','Y']

# Step 2: Label Encoding
le_chills = preprocessing.LabelEncoder()
le_runningnose = preprocessing.LabelEncoder()
le_headache = preprocessing.LabelEncoder()
le_fever = preprocessing.LabelEncoder()
le_hasflu = preprocessing.LabelEncoder()

chills_encoded = le_chills.fit_transform(chills)
runningnose_encoded = le_runningnose.fit_transform(runningnose)
headache_encoded = le_headache.fit_transform(headache)
fever_encoded = le_fever.fit_transform(fever)
hasflu_encoded = le_hasflu.fit_transform(hasflu)

# Step 3: Combine features
features = list(zip(chills_encoded, fever_encoded, headache_encoded, runningnose_encoded))

# Step 4: Train the model
model = GaussianNB()
model.fit(features, hasflu_encoded)

# Step 5: Predict for a new case: chills=Y, fever=Y, headache=MILD, runningnose=N
sample = [
    le_chills.transform(['Y'])[0],
    le_fever.transform(['Y'])[0],
    le_headache.transform(['MILD'])[0],
    le_runningnose.transform(['N'])[0]
]
predicted = model.predict([sample])

# Step 6: Decode and print the result
print("Predicted (encoded):", predicted)
print("Does the person have flu?:", le_hasflu.inverse_transform(predicted))
