import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as ms
import plotly.graph_objects as go

# to browse csv file
df = pd.read_csv("googleplaystore.csv")

# meta data of csv file content
df.info()

#to print no. of null elements
print(df.isnull().sum())
ms.matrix(df)
# plt.show()

df.columns = [each.replace(" ", "_") for each in df.columns]
print(df.columns)
# Data Cleaning like removing $ from category and blank
df["Category"] = [each.replace("_", " ") for each in df.Category]
df["Price"] = [each.replace("$", " ") for each in df.Price]


df.Reviews = pd.to_numeric(df.Reviews, errors='coerce')
df.Price = pd.to_numeric(df.Price, errors='coerce')
df.Rating = pd.to_numeric(df.Rating, errors='coerce')

# Seaborn Bar Plot for category vs count
df2 = pd.DataFrame(columns=['Category'])
df2["Category"] = [each for each in df.Category.unique()]
df2["Count"] = [len(df[df.Category == each]) for each in df2.Category]
df2 = df2.sort_values(by=['Count'], ascending=False)

plt.figure(figsize=(25, 10))
sns.barplot(x=df2.Category, y=df2.Count)
plt.xticks(rotation=90)
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

# Google Play Apps Android Version Ratio
labels = df.Android_Ver.unique()
values = []
for each in labels:
    values.append(len(df[df.Android_Ver == each]))

# Use `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
fig.show()


# Game, Family and Medical Category (min,q1,median,q3,max value)
# Interactive Box plot
Category1 = df[df.Category == "GAME"].Rating
Category2 = df[df.Category == "FAMILY"].Rating
Category3 = df[df.Category == "MEDICAL"].Rating

fig1 = go.Figure()
# Using x instead of y argument for horizontal plot
fig1.add_trace(go.Box(x=Category1, name='GAME'))
fig1.add_trace(go.Box(x=Category2, name='FAMILY'))
fig1.add_trace(go.Box(x=Category3, name='MEDICAL'))
fig1.show()

df.Content_Rating.unique()
df.Content_Rating.value_counts().plot(kind='bar')
plt.yscale('log')
plt.show()