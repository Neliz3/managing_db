from config import conn_row
from app import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = conn_row
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'necamkoedm3kdcda9ewjedecd'

db = SQLAlchemy(app)


from . import models
