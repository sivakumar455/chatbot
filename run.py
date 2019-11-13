import flask

from flask import render_template, Flask, request

from joblib import dump, load
import pandas as pd

import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

app = Flask(__name__)

def tokenize(text):
    print(text)
    word = re.sub(r'[^A-Za-z0-9\s]', '',text)
    words = word_tokenize(word)
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    words = [lemmatizer.lemmatize(w.lower(),pos="v") for w in words if w not in stop_words]
    return words

model = load('chatbot.pkl')

res_cols = ['query','output']

df = pd.DataFrame(columns=res_cols)

df.to_csv("recent_msgs.csv",sep=',')

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')

@app.route('/go')
def go():
    query = request.args.get('query', '')
    #print("Query",query)

    pred = model.predict([query])
    res = pred[0]
    #print("Pred",res)
    #print(type(res))

    df1 = pd.DataFrame({'query':query,'output':res},index=[1],columns = res_cols)
    with open('recent_msgs.csv', 'a') as f:
        df1.to_csv(f, header=False)

    dff = pd.read_csv("recent_msgs.csv")

    recent_msgs = dff.query
    recent_output = dff.output
    print(recent_msgs)
    length = dff.shape[0]
    print(length)

    return render_template('go.html',query=query, predicted=res,recent_msgs=recent_msgs,recent_output=recent_output,length=length)

app.run(host='localhost',port=3001,debug=True)

