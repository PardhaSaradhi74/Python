# Importing the libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

# Importing the dataset
dataset = pd.read_csv('glass.csv')
X = dataset.drop('Type', axis=1)
Y = dataset['Type']
print(X)

# Splitting the dataset into the Training set and Test set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.4)

# Fitting Naive Bayes to the Training set
classifier = GaussianNB()
classifier.fit(X_train, Y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)


acc_svc = round(classifier.score(X_train, Y_train) * 100, 2)

print("naive accuracy is:", acc_svc)
print(classification_report(Y_test,y_pred))