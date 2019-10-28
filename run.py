import flask

from flask import render_template, Flask, request

from joblib import dump, load

app = Flask(__name__)


def tokenize(text):
    print(text)
    word = re.sub(r'[^A-Za-z0-9\s]', '',text)
    #print(word)
    words = word_tokenize(word)
    #print(words)
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    words = [lemmatizer.lemmatize(w.lower(),pos="v") for w in words if w not in stop_words]
    #print(words)
    return words

model = load('chatbot.pkl')

@app.route('/')
@app.route('/index')
def index():


    return render_template('index.html')

@app.route('/go')
def go():
    query = request.args.get('query', '')
    print(query)

    return render_template('go.html')

app.run(host='localhost',port=3001,debug=True)

