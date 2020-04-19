import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("user_reviews.csv", encoding="latin1")
df = pd.concat([df.Translated_Review, df.Sentiment], axis = 1)
df.dropna(axis = 0, inplace = True)
df.Sentiment = [0 if i == "Positive" else 1 if i == "Negative" else 2 for i in df.Sentiment]

# Now lets Cleaning the Text

text_list = []
for i in df.Translated_Review :
    review = re.sub('[^a-zA-Z]', ' ', i)
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    text_list.append(review)


# Creating the Bag of Words model
cv = CountVectorizer(max_features = 1000)
x = cv.fit_transform(text_list).toarray()
y = df.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)

print(x_train.shape,x_test.shape,y_train.shape,y_test.shape)

# Now Fitting linear regression to training set
cf = linear_model.LogisticRegression()
cf.fit(x_train, y_train)
print(cf.score(x_test,y_test))
y_pred = cf.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
print(cm)
print(accuracy)

# Now Fitting Naive Bayes classifier to the Training set
cf = GaussianNB()
cf.fit(x_train, y_train)
# Predicting the Test set results
y_pred = cf.predict(x_test)

# Making the Confusion Matrix and find Accuracy
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
print(cm)
print(accuracy)

# Now Fitting Random Forest Classifier to the Traning set
cf = RandomForestClassifier(n_estimators = 10, random_state=0)
cf.fit(x_train, y_train)

# Predicting the Test set results
y_pred = cf.predict(x_test)

# Making the Confusion Matrix and find Accuracy
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
print(cm)
print(accuracy)