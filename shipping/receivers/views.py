import os, secrets
import html.parser
from PIL import Image
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, Blueprint
from flask_weasyprint import HTML, render_pdf
from flask.globals import current_app
from flask_login import login_user, current_user, logout_user, login_required
from shipping import db, bcrypt
from shipping.receivers.forms import ReceiverForm
from shipping.models import Client, Receiver, Package, User

receivers = Blueprint('receivers', __name__)

# Show a list of receiver
@receivers.route("/client/<int:client_id>/receiver/<int:receiver_id>")
@login_required
def creceiver(client_id, receiver_id):
    client = Client.query.filter_by(id=client_id).first()
    receiver = Receiver.query.filter_by(id=receiver_id).first()
    return render_template('creceiver.html', client_id = client_id, receiver_id = receiver_id)
@receivers.route("/client/<int:client_id>/packages")
@login_required
def packages_adm(client_id):
    client = Client.query.filter_by(id=client_id).first()
    return render_template('package_adm.html', client_id = client.id)

# Add a new receiver
@receivers.route("/receiver", methods=['GET', 'POST'])
@login_required
def receiver():
    client = Client.query.all()
    form = ReceiverForm()
    if form.validate_on_submit():
        receiver = Receiver(
            fname = form.fname.data,
            lname = form.lname.data,
            phone_number = form.phoneNumber.data
        )
        db.session.add(receiver)
        db.session.commit()
        flash("New receiver has been added.")
        return redirect(url_for('feature'))
    return render_template('new_receiver.html', form = form)

#Show receiver
@receivers.route("/receivers/")
@login_required
def all_receivers():
    receivers = Receiver.query.all()
    return render_template('receivers.html', receivers = receivers)


@receivers.route("/client/<int:client_id>/receiver")
@login_required
def view_receiver(client_id):
    client = Client.query.filter_by(id=client_id).first()
    receivers = Receiver.query.all()
    return render_template('receiver.html', client_id = client_id, receivers=receivers)

