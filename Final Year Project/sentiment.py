import pandas as pd
from nltk.corpus import stopwords
from sklearn import metrics
from sklearn.model_selection import train_test_split
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
sdata = pd.read_csv('test.csv', encoding= 'unicode_escape')
# sdata.sort_values("Headlines", inplace=True)

# # dropping ALL duplicate values
# sdata.drop_duplicates(subset="Headlines",
#                      keep=False, inplace=True)
#
# print(len(sdata))
# print(sdata.head())
# print()
# print(sdata.head())


# Split into training and testing data
x = sdata['Headlines']
y = sdata['Sentiment']

x, x_test, y, y_test = train_test_split(x, y, stratify=y, test_size=0.2, random_state=42)


# Vectorize text reviews to numbers
en_stopwords = set(stopwords.words("english"))
vec = CountVectorizer(stop_words=en_stopwords)
x = vec.fit_transform(x).toarray()
# print(x)
x_test = vec.transform(x_test).toarray()



smodel = MultinomialNB()
smodel.fit(x, y)
nb_predict_test = smodel.predict(x_test)
print("{0}".format(metrics.confusion_matrix(y_test, nb_predict_test)))
print(smodel.score(x_test, y_test))
# print(smodel.predict(vec.transform(['not a good day for nepal'])))

filename = 'finalized_model.sav'
pickle.dump(smodel, open(filename, 'wb'))

pickle.dump(vec, open("vectorizer.pickle", "wb"))
