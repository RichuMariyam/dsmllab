chills=['Y','Y','Y','N','N','N','N','Y']
runningnose=['N','Y','N','Y','N','Y','Y','Y']
headache=['MILD','NO','STRONG','MILD','NO','STRONG','STRONG','MILD']
fever=['Y','N','Y','Y','N','Y','N','Y']
hasflu=['N','Y','Y','Y','N','Y','N','Y']

from heapq import merge

from sklearn import preprocessing

from sklearn.naive_bayes import GaussianNB

le=preprocessing.LabelEncoder()

chills_encoded = le.fit_transform(chills)
print("chills_encoded:",chills_encoded)
runningnose_encoded = le.fit_transform(runningnose)
print("runningnose_encoded:",runningnose_encoded)
headache_encoded = le.fit_transform(headache)
print("headache_encoded:",headache_encoded)
fever_encoded = le.fit_transform(fever)
print("fever_encoded:",fever_encoded)
hasflu_encoded = le.fit_transform(hasflu)
print("hasflu_encoded:",hasflu_encoded)

features = list(zip(chills_encoded, fever_encoded, headache_encoded, runningnose_encoded))
print(features)

model = GaussianNB()
model.fit(features, hasflu_encoded)

predicted = model.predict([[1,1,0,0]])
print("Predicted value:", predicted)
print('HAS FLU:', le.inverse_transform(predicted))

from sklearn.metrics import accuracy_score, precision_score,recall_score,confusion_matrix

y_pred=model.predict(features)
acc=accuracy_score(hasflu_encoded,y_pred)
prec=precision_score(hasflu_encoded,y_pred,average='binary')
rec=recall_score(hasflu_encoded,y_pred,average='binary')
print('Accuracy:', acc)
print("Precision:",prec)
print('Recall:', rec)
cm=confusion_matrix(hasflu_encoded,y_pred)
print("Confusion Matrix:\n",cm)


