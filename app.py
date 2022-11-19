from flask import Flask, redirect, url_for, request, render_template
from models.autogluon.main import train, predict
app = Flask(__name__)

@app.route("/model")
def train_model():
    training = True
    train()
    training = False
    return render_template('templates/index.html', training = training) 

@app.route("/model_predict", methods = ['POST'])
def predict_model():
    img = request.form['img']
    prediction = predict(img)
    return prediction

@app.route("/")
def home():
    return "homie home"

