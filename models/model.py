from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.String(10))
    skin_type = db.Column(db.String(50))
    concerns = db.Column(db.String(100))
    lifestyle = db.Column(db.String(100))
    allergies = db.Column(db.String(100))
