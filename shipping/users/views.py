import os, secrets
from PIL import Image
from flask import render_template, flash, redirect, url_for, request, Blueprint
from flask.globals import current_app
from flask_login import login_user, current_user, logout_user, login_required
from shipping import db, bcrypt
from shipping.users.forms import LoginForm, RegistrationForm, UpdatePictureForm
from shipping.models import User

users = Blueprint('users', __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('mian.feature'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f"Account for {user.username} has been created.")
        return redirect(url_for('users.login'))
    return render_template('register.html', form = form)
        

@users.route("/login/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.feature'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.feature'))
        else:
            flash("Login unsuccessfull! Please check for your username and password", "danger")
    return render_template("login.html", form = form)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn 


@users.route("/account/", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdatePictureForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        db.session.commit()
        flash("You picture has been updated successfully.", "success")
        return redirect(url_for('users.account'))
    image_file = url_for('static', filename='/profile_pics/' + current_user.image_file)
    return render_template('account.html', image_file = image_file, form = form)

@users.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for('main.home'))