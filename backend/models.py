from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(120), nullable=False)
email = db.Column(db.String(120), unique=True, nullable=False)
password = db.Column(db.String(200), nullable=False)


class Location(db.Model):
id = db.Column(db.Integer, primary_key=True)models.py


user_id = db.Column(db.Integer, nullable=False)
latitude = db.Column(db.String(50))
longitude = db.Column(db.String(50))
created_at = db.Column(db.DateTime, server_default=db.func.now())
