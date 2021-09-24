import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from prediction_modules.logger import log_class
from flask import Flask, render_template, url_for, request
from flask_cors import CORS,cross_origin

folder_path = './log_files/'
file_name = 'log_file.txt'

logger = log_class(folder_path,file_name)


with open('Credit_Card_pickle','rb') as f:
    classifier = pickle.load(f)


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def home():
    logger.create_log_file("rendering the home page for taking user input")
    return render_template('index.html')

@app.route('/Predict', methods = ['POST'])
@cross_origin()
def check():
    logger.create_log_file("Data entered by the user successfully")
    if request.method == 'POST':
        Time = request.form['Time']
        V1 = request.form['V1']
        V2 = request.form['V2']
        V3 = request.form['V3']
        V4 = request.form['V4']
        V5 = request.form['V5']
        V6 = request.form['V6']
        V7 = request.form['V7']
        V8 = request.form['V8']
        V9 = request.form['V9']
        V10 = request.form['V10']
        V11 = request.form['V11']
        V12 = request.form['V12']
        V14 = request.form['V14']
        V16 = request.form['V16']
        V17 = request.form['V17']
        V18 = request.form['V18']
        V21 = request.form['V21']
        V27 = request.form['V27']
        V28 = request.form['V28']
        Amount = request.form['Amount']

        prediction = classifier.predict([[Time, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V14, V16, V17, V18,
                                  V21, V27, V28, Amount]])
        logger.create_log_file("Predicted the output by our model")
    return render_template('prediction.html', result = prediction)


if __name__ == '__main__':
    app.run(debug=True)