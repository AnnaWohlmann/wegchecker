from flask import Flask, redirect, url_for, request, render_template
import lib.db_ops as dbOps
import lib.email_wrap as email
import json

from models.autogluon.main import train, predict
import cv2
app = Flask(__name__)
REPORT_LIMIT = 10

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

# Returns only 1 object of the type mentioned above
@app.route('/osm/<id>', methods = ['GET'])
def getOsmIssue(id):
    return (json.dumps(dbOps.get_osm_issue_by_id(id)), 200)

@app.route('/osm/<id>/validate/<username>', methods = ['GET'])
def validateOsmIssue(id, username):
    issue = dbOps.update_osm_issue_counter(id)
    dbOps.update_user_osm_score(username)

    # Send email when we get enough reports
    if issue['report_no'] + 1 >= REPORT_LIMIT:
        email.sendEmail(email.mailSubject, email.fillInEmailBody(issue['report_no']+1, "Classification error", "lat=%s lon=%s"%(issue['latitude'], issue['longitude'])))

# Only run to fill in the osm_issues database
# dbOps.init_osm_issue_db()
