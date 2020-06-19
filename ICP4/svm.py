# Support Vector Machine (SVM)

# Importing the libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Importing the dataset
dataset = pd.read_csv('glass.csv')
X = dataset.drop('Type', axis=1)
Y = dataset['Type']

# Splitting the dataset into the Training set and Test set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.4)

# Fitting SVM to the Training set
svc = SVC(kernel='linear')
svc.fit(X_train, Y_train)

# Predicting the Test set results
y_pred = svc.predict(X_test)

acc_svc = round(svc.score(X_train, Y_train) * 100, 2)
print("svm accuracy is:", acc_svc)
print(classification_report(Y_test,y_pred))