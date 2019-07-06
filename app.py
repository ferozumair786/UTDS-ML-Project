

import sqlalchemy

#pip install Flask-MySQLdb
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

import json


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'cig4l2op6r0fxymw.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'qvencmith3352t7o'
app.config['MYSQL_PASSWORD'] = 'y5yh14d68ozhspvc'
app.config['MYSQL_DB'] = 'eparayipn70308ss'

mysql = MySQL(app)


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")
    


@app.route("/nutdata")
def nut_data():
    """Return Data."""
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM nut_data')
    row_headers = [x[0] for x in cur.description]
    rv=cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)


if __name__ == "__main__":
    app.run()
