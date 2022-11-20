import mysql.connector 
from csv import reader

OSM_COUNTER = 0

# Database details
mydb = mysql.connector.connect(
  host="localhost",
  user="aster",
  password="password",
  db="wegchecker"
)

mycursor = mydb.cursor()

def get_user_by_name(username):
    sql = "select * from users where username = '" + username + "'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    # User does not exist
    if myresult == []:
        return {}
    
    user = {
        'score_osm': myresult[0][2],
        'score_bike': myresult[0][3],
        'avatar_path': myresult[0][4]
    }
    return user

# Only for ease of access later. Not used by the app.
# Reads the csv file into the database
def init_osm_issue_db():
    global OSM_COUNTER
    sql = "insert into osm_issues (db_id, image_id, longitude, latitude, osm_way_id, current_classif, correction_classif, reports_no) values (%s, %s, %s, %s, %s, %s, %s, %s)"

    with open('../resources/issues.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            correction = 'primary'
            if row[4] == 'primary':
                correction = 'footwalk'
            vals = (OSM_COUNTER, row[0], row[1], row[2], row[3], row[4], correction, 1)
            mycursor.execute(sql, vals)
            OSM_COUNTER += 1
    mydb.commit()

def get_all_osm_issues():
    sql = "select * from osm_issues"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    if myresult == []:
        return []

    issues = []
    for row in myresult:
        issues.append({
            'db_id': row[0],
            'image_id': row[1],
            'longitude': row[2],
            'latitude': row[3],
            'osm_way_id': row[4],
            'current_classif': row[5],
            'correction_classif': row[6],
            'reports_no': row[7]
        })

    return issues

# CREATE DATABASE wegchecker
# USE wegchecker

# CREATE TABLE users(
#     username VARCHAR(255) PRIMARY KEY,
#     email VARCHAR(255),
#     score_osm INT NOT NULL,
#     score_bike INT NOT NULL,
#     avatar VARCHAR(255)
#     );

# Default user
# insert into users (username, email, score_osm, score_bike, avatar) values ("aster", "chireamihaela99@gmail.com", 0, 0, "avatars/cat.jpg");

# CREATE TABLE osm_issues(
#     db_id INT PRIMARY KEY,
#     image_id VARCHAR(255),
#     longitude VARCHAR(255),
#     latitude VARCHAR(255),
#     osm_way_id VARCHAR(255),
#     current_classif VARCHAR(255),
#     correction_classif VARCHAR(255),
#     reports_no INT
#     );
