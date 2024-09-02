# Data Processing
import pandas as pd
import numpy as np
import ssl

# Modelling
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split

# Importing the dataset
df = pd.read_csv('/Users/lucy/sstp/human_annotations_same.csv')
df = df.dropna(how='any')
df = df.drop(['id', 'full_link', 'human_label2'], axis=1)

# Cleaning the texts
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

corpus = []
for i in range(0,6726):
    post = re.sub('[^a-zA-Z]',' ',df['text'][i])
    post = post.lower()
    post = post.split() #convert into list
    ps = PorterStemmer()
    post = [ps.stem(word) for word in post if not word in set(stopwords.words('english'))]
    post = ' '.join(post)
    corpus.append(post)

# Creating the bag of Word Model
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features = 100)
X=cv.fit_transform(corpus).toarray()
y=df["human_label1"]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, shuffle=False)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, shuffle=False)
# Fitting classifier to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(criterion='entropy', bootstrap=False, n_estimators=500, min_samples_split=5, max_depth=400, min_samples_leaf=2)
classifier.fit(X_train,y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))