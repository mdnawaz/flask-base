from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')
app.secret_key = 'HJKabdh5676@#@$'

db = SQLAlchemy(app)

from app import views, models