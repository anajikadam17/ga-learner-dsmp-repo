# --------------
# import packages
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

# Load the dataset
df = pd.read_csv(path, sep = '\t')

# Converting date attribute from string to datetime.date datatype 
pd.to_datetime(df['date'])

# calculate the total length of word
df['length'] = df['verified_reviews'].apply(lambda x: len(str(x)))



# --------------
## Rating vs feedback

# set figure size
sns.countplot(x = 'rating', hue = 'feedback', data = df)

# generate countplot
sns.barplot(x = 'rating',y = "variation", hue = 'feedback', data = df)

# display plot


## Product rating vs feedback

# set figure size


# generate barplot


# display plot




# --------------
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus=[]
for i in range(0,3150):
    review = re.sub('[^a-zA-Z]', ' ', df['verified_reviews'][i] )
    review=review.lower()
    review=review.split()
    ps=PorterStemmer()
    review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review=' '.join(review)
    corpus.append(review)


# --------------
# import libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# Instantiate count vectorizer
cv = CountVectorizer(max_features = 1500)

# Independent variable
X = cv.fit_transform(corpus)

# dependent variable
y = df['feedback']

# Counts
count = y.value_counts()

# Split the dataset
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)





# --------------
# import packages
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, f1_score

# Instantiate calssifier
rf = RandomForestClassifier(random_state=2)

# fit model on training data
rf.fit(X_train,y_train)

# predict on test data
y_pred = rf.predict(X_test)

# calculate the accuracy score
score = accuracy_score(y_test, y_pred)

# calculate the precision
precision = precision_score(y_test,y_pred)


# display 'score' and 'precision'



# --------------
# import packages
from imblearn.over_sampling import SMOTE

# Instantiate smote
smote = SMOTE(random_state = 9)

# fit_sample onm training data
X_train, y_train = smote.fit_sample(X_train,y_train)

# fit modelk on training data
rf.fit(X_train,y_train)

# predict on test data
y_pred = rf.predict(X_test)

# calculate the accuracy score
score = accuracy_score(y_test, y_pred)

# calculate the precision
precision = precision_score(y_test,y_pred)


# y_pred = rf.predict(y_test)
# # calculate the accuracy score
# score = accuracy_score(y_test,y_pred)

# # calculate the precision
# precision = precision_score(y_test,y_pred)

# display precision and score



