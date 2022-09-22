import pandas as pd
import joblib
import os
import sklearn
import lxml
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt
from flask import send_file
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

beats = {0: "ecotic beats", 1: "Supraventricular ectopic beats ", 2: "Ventricular ectopic beats",
         3: "Fusion Beats", 4: " Unknown Beats"}


def read_Data(csv_location):
    data = pd.read_csv(csv_location)

    picture_name = []
    for i in range(len(data.index)):
        box = []
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(0, 190)
        ax.set_ylim(0, 1)

        ax.xaxis.set_major_locator(MultipleLocator(10))
        ax.yaxis.set_major_locator(MultipleLocator(0.2))

        ax.xaxis.set_minor_locator(AutoMinorLocator(1))
        ax.yaxis.set_minor_locator(AutoMinorLocator(0.02))

        ax.grid(which='major', color='#2a3439')
        ax.grid(which='minor', color='#000000', linestyle=':')
        ax.tick_params(
            axis='x',  # changes apply to the x-axis
            which='both',  # both major and minor ticks are affected
            bottom=False,  # ticks along the bottom edge are off
            top=False,  # ticks along the top edge are off
            labelbottom=False)

        ax.plot(data.iloc[i, :186])
        name = str(i) + '.png'
        name_id = 'id : ' + str(i)
        box.append(name)
        box.append(name_id)
        picture_name.append(box)

        name = 'D:/User Files/Downloads/ECGwebAPP-master/ECGwebAPP-master/static/graphs/' + name
        fig.savefig(name)
        plt.close()

    return data, picture_name


def read_Model(model_location):
    model = joblib.load(model_location)
    return model


def predict(data, model):
    prediction = model.predict(data.iloc[0:, :186])
    prob = model.predict_proba(data.iloc[0:, :186])
    probabilities = []
    for proba in prob:
        probabilities.append(max(proba))
    output = []
    for value in prediction:
        text = beats.get(value)
        output.append(text)

    return output, probabilities


def create_csv(data, prediction, prob):
    output = pd.DataFrame({'id': [i for i in range(len(data.index))], "prediction": prediction, "probability": prob})
    output.to_csv('output.csv', index=False)
    return output


def delete_csv():
    os.remove('output.csv')


def give_prediction(csv_location, model_location):
    data, pictures_name = read_Data(csv_location)
    all_data = []
    model = read_Model(model_location)
    pred, prob = predict(data, model)
    output = create_csv(data, pred, prob)
    for i in range(0, len(data.index)):
        some_data = [output.iloc[i]['id'], output.iloc[i]['prediction'], output.iloc[i]['probability'],
                     pictures_name[i]]
        all_data.append(some_data)
    return output, all_data
