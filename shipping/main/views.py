from flask import Blueprint, render_template
from flask_login import login_required

main = Blueprint('main', __name__)



@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')


@main.route("/feature")
@login_required
def feature():
    return render_template('feature.html')
