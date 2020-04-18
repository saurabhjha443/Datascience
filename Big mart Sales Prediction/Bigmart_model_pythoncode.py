# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 


# %%
rawdata=pd.read_csv("Proccessed_data2.csv")


# %%
data=rawdata.copy()
data.head()


# %%
IDcol=data[["Item_Identifier","Outlet_Identifier"]]
IDcol


# %%
X=data.drop(["Item_Identifier","Outlet_Identifier","Item_Outlet_Sales"],axis=1)
Y=data["Item_Outlet_Sales"]


# %%
X.head()


# %%
model=LinearRegression(n_jobs=-1)
model.fit(X,Y)


# %%
testdata=pd.read_csv("Proccessed_testdata.csv")
testdata.head()


# %%
data1=testdata.copy()
X=data1.drop(["Item_Identifier","Outlet_Identifier"],axis=1)
X["Item_Outlet_Sales"]=0.0
X


# %%
data1["Item_Outlet_Sales"]=abs(model.predict(X))


# %%
data1["Item_Outlet_Sales"]


# %%
data1.head()


# %%
data1.to_csv("Predicted.csv",index=False)


# %%
Submission_data=data1[["Item_Identifier","Outlet_Identifier","Item_Outlet_Sales"]]
Submission_data.head()


# %%
Submission_data.to_csv("Submissionlinear3.csv",index=False)


# %%


