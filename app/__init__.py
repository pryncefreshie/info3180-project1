from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from subprocess import call

app = Flask(__name__)
app.config['SECRET_KEY'] = "you know nothing Jon Snow"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://icmysushcyvrax:9dd778aa5f4376c4884e8b776c6fbe2cdef16515061aff155be4153daf60c9e4@ec2-50-17-227-28.compute-1.amazonaws.com:5432/dav3d5eun2sbm3"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://icmysushcyvrax:9dd778aa5f4376c4884e8b776c6fbe2cdef16515061aff155be4153daf60c9e4@ec2-50-17-227-28.compute-1.amazonaws.com:5432/dav3d5eun2sbm3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/profilephotos'
db = SQLAlchemy(app)

allowed_exts = ["jpg", "jpeg", "png"]

from app import views