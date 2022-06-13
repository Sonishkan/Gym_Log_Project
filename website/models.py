from tkinter import INSERT
from sqlalchemy import insert
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))

    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id')) ## workout id as foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) ## user id as foreign key

    
class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(1000))

    workoutExercises = db.relationship('Exercise')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) ## user id as foreign key


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float)
    reps = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id')) ## workout id as foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) ## user id as foreign key
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id')) ## exercise id as foreign key


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

    logs = db.relationship('Log') ## stores all the logs the user has created
    exercises = db.relationship('Exercise')
    workouts = db.relationship('Workout')

