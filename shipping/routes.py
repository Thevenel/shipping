import os, secrets
import html.parser
from PIL import Image
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_weasyprint import HTML, render_pdf
from flask.globals import current_app
from flask_login import login_user, current_user, logout_user, login_required
from shipping import app, db, bcrypt
from shipping.forms import PackageForm, ClientForm, ReceiverForm, LoginForm, RegistrationForm, UpdatePictureForm
from shipping.models import Client, Receiver, Package, User

now = datetime.utcnow()













@app.route("/package/view/<int:package_id>")
@login_required
def report_one(package_id):
    package = Package.query.filter_by(id=package_id).first()
    return render_template('report_one.html', package = package, package_id = package_id)

# @app.route("/report_<package_id>.pdf")
# @login_required
# def report_one_pdf(package_id):
#     package = Package.query.filter_by(id=package_id).first()
#     return render_pdf(url_for('report_one', package = package, package_id = package_id))


@app.route("/report_<package_id>.pdf")
@login_required
def report_one_pdf(package_id):
    package = Package.query.filter_by(id=package_id).first()
    html= render_template('report_one.html', package = package, package_id = package_id)
    return render_pdf(HTML(string=html))

# @app.route("/package/view/<string:package_id>.pdf")
# @login_required
# def view_report(package_id):
#     package = Package.query.filter_by(id=package_id).first()
#     return render_pdf(url_for('report_one', package = package, package_id = package_id))




