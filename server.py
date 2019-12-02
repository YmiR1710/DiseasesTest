from flask import Flask, render_template, request
import pandas as pd
import warnings
from data.model import get_prognosis
from data.questions import questions
from data.gist import build_gist
from gevent.pywsgi import WSGIServer


app = Flask(__name__)
warnings.filterwarnings('ignore')
df_train = pd.read_csv("data\\Training.csv")
df_test = pd.read_csv("data\\Testing.csv")
df = df_train.append(df_test, ignore_index=True)
user_data = []

@app.route('/', methods=['GET', 'POST'])
def main():
    if len(user_data) < 132:
        question = questions[len(user_data)]
        if request.method == 'POST' and 'submit_button' in request.form:
            try:
                user_answer = request.form['answer']
            except KeyError:
                user_answer = '3'
            if user_answer == '1':
                user_data.append(1)
            elif user_answer == '2':
                user_data.append(0)
            else:
                user_data.append(None)
        else:
            user_data.append(1)
        return render_template("index.html", question=question)
    else:
        prognosis = get_prognosis(df, user_data)
        user_data.clear()
        return render_template("result.html", gist=build_gist(prognosis[1]))



if __name__ == '__main__':
    WSGIServer(('127.0.0.1', 5000), app).serve_forever()
