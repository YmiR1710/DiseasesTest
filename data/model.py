import pandas as pd
import warnings
from sklearn.naive_bayes import MultinomialNB


def get_prognosis(data_frame, user_data):
    warnings.filterwarnings('ignore')
    model_input = list()
    columns = list(data_frame.columns)
    for i in range(len(user_data)):
        if user_data[i] is not None:
            model_input.append(user_data[i])
        else:
            columns.remove(data_frame.columns[i])
    data_frame = data_frame[columns]
    x = data_frame.drop(['prognosis'], axis=1)
    y = data_frame['prognosis']
    model_input = pd.DataFrame([model_input], columns=columns.remove('prognosis'))
    mnb = MultinomialNB()
    mnb = mnb.fit(x, y)
    prediction = str(mnb.predict(model_input)[0])
    probabilities = mnb.predict_proba(model_input)
    prob_dictionary = dict(zip(mnb.classes_, probabilities[0]))
    return [prediction, prob_dictionary]
