import os, secrets
import html.parser
from PIL import Image
from datetime import datetime
from flask import render_template, flash, redirect, url_for, Blueprint
from flask_weasyprint import HTML, render_pdf
from flask_login import login_required
from shipping import db
from shipping.clients.forms import ClientForm
from shipping.models import Client, Receiver


clients = Blueprint('clients', __name__)

#Create a new client
@clients.route("/client/new", methods=['GET', 'POST'])
@login_required
def new_client():
    form = ClientForm()
    if form.validate_on_submit():
        client = Client(
            id_number=form.id_number.data, 
            companyName=form.companyName.data,
            fname = form.fname.data,
            lname = form.lname.data,
            address = form.address.data,
            city = form.city.data,
            state = form.state.data,
            zip_code = form.zCode.data,
            phone_number = form.phoneNumber.data
            )
        db.session.add(client)
        db.session.commit()
        flash(f"{form.fname.data} {form.lname.data} has been added successfully!", "success")
        return redirect(url_for('clients.clients'))
    return render_template('new_client.html', form = form)

#Show all clients
@clients.route("/client/")
@login_required
def all_clients():
    clients = Client.query.all()
    return render_template('client.html', clients = clients)

#Get all packages from a particular client
@clients.route("/client/<int:client_id>/")
@login_required
def client(client_id):
    client = Client.query.filter_by(id=client_id).first()
    packages = client.packages
    receivers = Receiver.query.all()
    return render_template('packages_list.html',
        client_id = client_id,
        packages = packages,
        receivers=receivers)


