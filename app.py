from flask import Flask, redirect, url_for, request, render_template
import lib.db_ops as dbOps
import json

from models.autogluon.main import train, predict
import cv2
app = Flask(__name__)

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

# Returns object of type {"score_osm": int, "score_bike": int, "avatar_path": string}
# or {} if no user was found
@app.route('/profile/<username>', methods = ['GET'])
def profile(username):
    return (json.dumps(dbOps.get_user_by_name(username)), 200)
