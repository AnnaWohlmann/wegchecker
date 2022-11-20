from flask import Flask, redirect, url_for, request, render_template
# from models.autogluon.main import train, predict
import lib.db_ops as dbOps
import json

app = Flask(__name__)

# @app.route("/model")
# def train_model():
#     training = True
#     train()
#     training = False
#     return render_template('templates/index.html', training = training) 

# @app.route("/model_predict", methods = ['POST'])
# def predict_model():
#     img = request.form['img']
#     prediction = predict(img)
#     return prediction

@app.route("/")
def home():
    return "homie home"

# Returns object of type {"score_osm": int, "score_bike": int, "avatar_path": string}
# or {} if no user was found
@app.route('/profile/<username>', methods = ['GET'])
def profile(username):
    return (json.dumps(dbOps.get_user_by_name(username)), 200)

# Returns list of objects with the following structure:
# {
#     'db_id': int,
#     'image_id': string,
#     'longitude': string,
#     'latitude': string,
#     'osm_way_id': string,
#     'current_classif': string,
#     'correction_classif': string,
#     'reports_no': int
# }
@app.route('/osm', methods=['GET'])
def osmIssues():
    return (json.dumps(dbOps.get_all_osm_issues()), 200)

# Only run to fill in the osm_issues database
# dbOps.init_osm_issue_db()
