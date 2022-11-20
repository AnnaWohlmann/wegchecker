import mysql.connector 

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
