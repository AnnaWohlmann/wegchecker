from flask import Flask, redirect, url_for, request, render_template
from models.autogluon.main import train, predict
import cv2
app = Flask(__name__)

@app.route("/model")
def train_model():
    training = True
    train()
    training = False
    return render_template('templates/index.html', training = training) 

@app.route("/model_predict", methods = ['GET'])
def predict_model():
    # image has to be numpy array.
    # image always named predict image.
    img = "data/predict_image.jpg"
    prediction = predict(img)
    return str(prediction["label_str"]) +" "+ str(prediction["label"])+" "+  str(prediction["prec"]) +" hi"

@app.route("/")
def home():
    return "homie home"

