
#loading the libraries
import numpy as np
import pandas as pd
from sklearn.datasets import load_digits

#loading datasets
dataset = load_digits()

#summarize the data
print(dataset.data)
print(dataset.target)

print(dataset.images.shape)
print(dataset.data.shape)

length_dataset= len(dataset.images)
print(length_dataset)

#data visualization and import the libariry for Visualization
n = 8
import matplotlib.pyplot as plt
plt.matshow(dataset.images[n])
plt.gray()
plt.show()

print(dataset.images[n])

#Segreting dataset into X and Y
X = dataset.images.reshape((length_dataset,-1))
X

Y = dataset.target
Y

#splitting dataset into training and testing
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=0)
print(x_train.shape)
print(X_test.shape)

#importing the algorithm
from sklearn import svm
model = svm.SVC()
model.fit(x_train,y_train)

#predicting the value
y_pred = model.predict(x_test)

#evaluation and checking accuracy
from sklearn.metrics import accuracy_score
print("The accuracy of model is : {0}".format(accuracy_score(y_test,y_pred)*100))

#check the results
n=150
result = model.predict(dataset.images[n].reshape((1,-1)))
plt.imshow(dataset.images[n], cmap=plt.cm.gray_r, interpolation='nearest')
print(result)
print("\n")
plt.axis('off')
plt.title('%i' %result)
plt.show()

