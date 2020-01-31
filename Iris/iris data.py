import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#from sklearn.cluster import k_means_
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
#from sklearn.metrics import  confusion_matrix

#Read csv file
df=pd.read_csv("iris.data")
names=["Sepal length","Sepal Width","Petal length","Petal Width","Class"]
#Print first 10 records
print(df.head(10))
print(df.describe())
#Plot histogram on records
df.hist(bins=20)
#show histogram
plt.show()
#convert dataFrame into n dimensional array
datashuffle=df.values
#now shuffle this using numpy
np.random.shuffle(datashuffle)
#Now Use 4 atttributes of 100 records into x
X_learn=datashuffle[:100][:,0:4]
#Use 5 attrbute of 100 records into y
Y_learn=datashuffle[:100][:,4]
#use support vector classification for machine learning
svc=SVC()
#fit into SVC model
svc.fit(X_learn,Y_learn)
x_test=datashuffle[-20:][:,0:4]
y_test=datashuffle[-20:][:,4]
#Now predict on last 20 records for prediction
y_predict=svc.predict(x_test)

print(f'Predicted results are {y_predict}')
print(f'Actual results are {y_test}')

print(f'Accuracy score is {accuracy_score(y_test,y_predict)}')

print("Classification Report is \n ",classification_report(y_test,y_predict))