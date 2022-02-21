import pickle
from sklearn.feature_extraction.text import CountVectorizer
vec = pickle.load(open("vectorizer.pickle", 'rb'))
model_bayes = pickle.load(open('finalized_model.sav', 'rb'))
model_svm = pickle.load(open('svm_model.sav', 'rb'))
print(model_bayes.predict(vec.transform(['not a good day for nepal'])))
classes = ['neutral', 'positive', 'negative']
def predict_svm(headings):
    print(headings)
    predections = []
    for heading in headings:
        if model_svm.predict([heading[1]])[0] == 0:
            predections.append("Neutral")
        elif model_svm.predict([heading[1]])[0] == 1:
            predections.append("Positive")
        else:
            predections.append("Negative")
    return predections
def predict_bayes(headings):
    print(headings)
    predections = []
    for heading in headings:
        if model_bayes.predict(vec.transform([heading[1]]))[0] == 0:
            predections.append("Neutral")
        elif model_bayes.predict(vec.transform([heading[1]]))[0] == 1:
            predections.append("Positive")
        else:
            predections.append("Negative")
    return predections
newsPapers = [["The Himalayan Times", "tht"], ["SetoPati","setopati"]]

with open('THT.pkl', 'rb') as f:
    THTLinks = pickle.load(f)

with open('setopati.pkl', 'rb') as f:
    setopatiLinks = pickle.load(f)


def getSetoPatiLinks(setopatiLinks, type):
    # preds = predict_bayes(setopatiLinks)
    preds = predict_svm(setopatiLinks)
    print(preds)
    links = []
    i = 0
    for data in setopatiLinks:
        if type == preds[i]:
            links.append([data[0], str(data[1]), str(preds[i])])
        elif type == "all":
            links.append([data[0], str(data[1]), str(preds[i])])


        i = i + 1
    return links

def getThtLinks(THTLinks, type):
    # preds = predict_bayes(THTLinks)
    preds = predict_svm(THTLinks)
    print(preds)
    links = []
    i = 0
    for data in THTLinks:

        if type == preds[i]:
            links.append([data[0], str(data[1]), str(preds[i])])
        elif type == "all":
            links.append([data[0], str(data[1]), str(preds[i])])

        i = i + 1

    print(links)
    return links
from flask import Flask, render_template, request

# app = Flask(__name__, instance_relative_config=True)
app = Flask(__name__)

@app.route("/tht", methods = ['GET'])
def tht():
    if request.method == 'GET':
        type = request.args.get('type')

    return render_template('sentiment.html', content = getThtLinks(THTLinks, type))


@app.route("/setopati", methods = ['GET'])
def setopati():
    if request.method == 'GET':
        type = request.args.get('type')
    return render_template('sentiment.html', content = getSetoPatiLinks(setopatiLinks, type))

@app.route("/test")
def test():
    return render_template('home.html', content = newsPapers)
@app.route("/")
def home():
    return render_template('home.html', content = newsPapers)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/analysis", methods = ['POST','GET'])
def analysis():
    if request.method == 'POST':

        userHeadline = request.form.get('userHeadline')
        print(userHeadline)
        svm = model_svm.predict([userHeadline])
        bayes = model_bayes.predict(vec.transform([userHeadline]))


        return render_template('analysis.html', content = ["Result of svm is " + classes[svm[0]], "Result of bayes is "+classes[bayes[0]]])
    return render_template('analysis.html', content = ["",""])
if __name__ == '__main__':
   app.run()

# print(results)