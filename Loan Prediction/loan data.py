import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

#read csv file in daatFrame
train=pd.read_csv("train.csv")
print(train.head())
#Description of dataFrame
print(train.describe())

print(train.info())

#Appy funtion to print sum of null elements in column
print(train.apply(lambda x: np.sum(train.isnull()),axis=0))

#Filling Missing data with data of most records
print(train["Gender"].value_counts())
train.Gender=train.Gender.fillna("Male")
print(train["Gender"].value_counts())

print(train["Married"].value_counts())
train.Married=train.Married.fillna("Yes")
print(train["Married"].value_counts())

print(train["Dependents"].value_counts())
train.Dependents=train.Dependents.fillna("0")
print(train["Dependents"].value_counts())

print(train["Self_Employed"].value_counts())
train.Self_Employed=train.Self_Employed.fillna("No")
print(train["Self_Employed"].value_counts())

print(train["LoanAmount"].value_counts())
train.LoanAmount=train.LoanAmount.fillna(train.LoanAmount.mean())
print(train["LoanAmount"].value_counts())

print(train["Loan_Amount_Term"].value_counts())
train.Loan_Amount_Term=train.Loan_Amount_Term.fillna(360)
print(train["Loan_Amount_Term"].value_counts())

print(train["Credit_History"].value_counts())
train.Credit_History=train.Credit_History.fillna(1)
print(train["Credit_History"].value_counts())

print(train["Loan_Status"].value_counts())

#Checking if any missing data remaining in dataframe
print(train.apply(lambda x: np.sum(train.isnull()),axis=0))


#using only 6 to 10 column for X
X=train.iloc[:,6:11].values
print(X)

Y=train.iloc[:,12].values
print(Y)

#Now reading csv on which prediction is to be made
test=pd.read_csv("test.csv")
print(test.head())

print(test.apply(lambda x: np.sum(test.isnull()),axis=0))

#Filling Missing data with data of most records
print(test["Gender"].value_counts())
test.Gender=test.Gender.fillna("Male")
print(test["Gender"].value_counts())

print(test["Married"].value_counts())
test.Married=test.Married.fillna("Yes")
print(test["Married"].value_counts())

print(test["Dependents"].value_counts())
test.Dependents=test.Dependents.fillna("0")
print(test["Dependents"].value_counts())

print(test["Self_Employed"].value_counts())
test.Self_Employed=test.Self_Employed.fillna("No")
print(test["Self_Employed"].value_counts())

print(test["LoanAmount"].value_counts())
test.LoanAmount=test.LoanAmount.fillna(test.LoanAmount.mean())
print(test["LoanAmount"].value_counts())

print(test["Loan_Amount_Term"].value_counts())
test.Loan_Amount_Term=test.Loan_Amount_Term.fillna(360)
print(test["Loan_Amount_Term"].value_counts())

print(test["Credit_History"].value_counts())
test.Credit_History=test.Credit_History.fillna(1)
print(test["Credit_History"].value_counts())

#Checking if any missing data remaining in dataframe
print(test.apply(lambda x: np.sum(test.isnull()),axis=0))


#using only 6 to 10 column for X_test
X_test=test.iloc[:,6:11].values
print(X_test)

#USing Linear Model Logistic Regrssion to train and predict
Classifier=LogisticRegression()
Classifier.fit(X,Y)

#Predicting on test dataset
Y_pred=Classifier.predict(X_test)
print(Y_pred)
