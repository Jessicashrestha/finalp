import pickle

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns

import nltk
from sklearn import metrics
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import TweetTokenizer

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, accuracy_score, f1_score
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import confusion_matrix, roc_auc_score, recall_score, precision_score

data = pd.read_csv("test.csv", encoding='unicode_escape')
# data.sort_values("Headlines", inplace=True)

# dropping ALL duplicate values
# data.drop_duplicates(subset="Headlines",
#                      keep=False, inplace=True)
#
# print(len(data))
# print(data.head())
train, test = train_test_split(data, test_size=0.15, random_state=42)
X_train = train['Headlines'].values
y_train = train['Sentiment']

X_test = test['Headlines'].values
y_test = test['Sentiment']

en_stopwords = set(stopwords.words("english"))

vectorizer = CountVectorizer(

    analyzer='word',
    lowercase=True,
    ngram_range=(1, 1),
    stop_words=en_stopwords)

# kfolds = StratifiedKFold(n_splits=5, shuffle=True, random_state=1)

np.random.seed(1)

pipeline_svm = make_pipeline(vectorizer,
                             SVC(probability=True, kernel="linear", class_weight="balanced"))

model = GridSearchCV(pipeline_svm,
                     param_grid={'svc__C': [0.01, 0.1, 1]},
                     verbose=1,
                     n_jobs=-1)

model.fit(X_train, y_train)
print(model.score(X_test, y_test))

print(model.predict(["really bad experience death"]))

nb_predict_test = model.predict(X_test)
print("{0}".format(metrics.confusion_matrix(y_test, nb_predict_test)))
filename = 'svm_model.sav'
pickle.dump(model, open(filename, 'wb'))
