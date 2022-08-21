from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from requests import request
from .models import *

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route('/loggedin')
@login_required
def loggedin():
    return render_template("loggedin.html", user=current_user)
    

#@views.route('/viewstats')
#@login_required
#def viewstats():
#    return render_template("viewstats.html", user=current_user)




