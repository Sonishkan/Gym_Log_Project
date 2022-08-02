from flask import Blueprint, render_template, request, flash, redirect, url_for
import requests
from .models import *
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.loggedin'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('There is not an account registered with that email', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        

        response = requests.get("https://isitarealemail.com/api/email/validate",
        params = {'email': email})

        status = response.json()['status']
        if user:
            flash('Email already exists.', category='error')
        elif status == "invalid":
            flash('Email seems to be invalid according to isitarealemail.com', category='error')
            pass
        elif len(first_name)<2:
            flash('First name must be greater than 1 character', category='error')
            pass
        elif password1 != password2:
            flash('Passwords do not match', category='error')
            pass
        elif len(password1)<7:
            flash('Password must be greater than 6 character', category='error')
            pass
        else:
            
            ## add user to database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=True, ) ##### issue due to this

            flash('Account successfully created', category='success')
            return redirect(url_for('views.loggedin'))

    return render_template("sign_up.html", user=current_user)

## 
@auth.route('/createworkout', methods=['GET', 'POST'])
@login_required
def createworkout():

    if request.method == 'POST':
        workoutname = request.form.get('workoutname')
        workoutdescription = request.form.get('workoutdescription')
        numberofexercise = request.form.get('numberofexercise')

        i = 0
        new_workout = Workout(name=workoutname, description=workoutdescription, user_id = current_user.id)
        db.session.add(new_workout)
        db.session.commit()
        print("number of exercises "+numberofexercise)
        while i < int(numberofexercise):
            exercise_name = request.form.get('Exercise'+str(i))
            print(exercise_name)
            new_exercise = Exercise(name=exercise_name,workout_id=new_workout.id, user_id = current_user.id)
            db.session.add(new_exercise)
            db.session.commit()
            
            i=i+1
        
        flash('Workout added to database', category='success')
        
    return render_template("createworkout.html", user=current_user)

@auth.route('/makeanentry', methods=['GET', 'POST'])
@login_required
def makeanentry():
    workout_id = ""
    if request.method == 'POST':
        if 'submitOption' in request.form:
            workout_id = request.form.get('field_6')
            #return(str(select)) # just to see what select is
        

            return render_template("makeanentry.html", user=current_user, workout_id=workout_id)
        elif 'submitWorkout' in request.form:

            flash('Workout session added to database', category='success')

            return render_template("makeanentry.html", user=current_user, workout_id=workout_id)

    return render_template("makeanentry.html", user=current_user, workout_id=workout_id)
