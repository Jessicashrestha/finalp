import pickle

import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from statsmodels.stats.contingency_tables import mcnemar

vec = pickle.load(open("vectorizer.pickle", 'rb'))
model_bayes = pickle.load(open('finalized_model.sav', 'rb'))
model_svm = pickle.load(open('svm_model.sav', 'rb'))
# print(model_bayes.predict(vec.transform(['not a good day for nepal'])))

TsTb = 0
TsFb = 0
FsTb = 0
FsFb = 0

sdata = pd.read_csv('test.csv', encoding='unicode_escape')

x = sdata['Headlines']
y = sdata['Sentiment']
x, x_test, y, y_test = train_test_split(x, y, stratify=y, test_size=0.2, random_state=42)


def predict_svm(headings):
    # print(headings)
    predections = []
    for heading in headings:
        if model_svm.predict([heading])[0] == 0:
            predections.append(0)
        elif model_svm.predict([heading])[0] == 1:
            predections.append(1)
        else:
            predections.append(2)
    return predections


def predict_bayes(headings):
    # print(headings)
    predections = []
    for heading in headings:
        print(heading)
        if model_bayes.predict(vec.transform([heading]))[0] == 0:
            predections.append(0)
        elif model_bayes.predict(vec.transform([heading]))[0] == 1:
            predections.append(1)
        else:
            predections.append(2)
    return predections


svm_pred = predict_svm(x_test)
bayes_pred = predict_bayes(x_test)

print(bayes_pred)
print(svm_pred)

i = 0
for actual in y_test:
    if bayes_pred[i] == svm_pred[i] and bayes_pred[i] == actual and svm_pred[i] == actual:
        TsTb = TsTb + 1
    elif (bayes_pred[i] != svm_pred[i]) and (bayes_pred[i] == actual):
        FsTb = FsTb + 1
    elif bayes_pred[i] == svm_pred[i] and bayes_pred[i] != actual and svm_pred[i] != actual:
        FsFb = FsFb + 1
    elif (bayes_pred[i] != svm_pred[i]) and (svm_pred[i] == actual):
        TsFb = TsFb + 1

    i = i + 1
#
table = [[TsTb, FsTb],
         [TsFb, FsFb]]
print(table)

result = mcnemar(table, exact=False, correction=True)
# summarize the finding
print('statistic=%.3f, p-value=%.9f' % (result.statistic, result.pvalue))
# interpret the p-value
alpha = 0.05

if result.pvalue > alpha:
    print('Same proportions of errors (fail to reject H0)')
else:
    print('Different proportions of errors (reject H0)')

svm_acc = (TsFb + TsTb) / len(x_test)
bayes_acc = (TsTb + FsTb) / len(x_test)

print("Acc of SVM: ", svm_acc)
print("Acc of Bayes: ", bayes_acc)
