import os, secrets
import html.parser
from PIL import Image
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, Blueprint
from flask_weasyprint import HTML, render_pdf
from flask.globals import current_app
from flask_login import login_user, current_user, logout_user, login_required
from shipping import db, bcrypt
from shipping.packages.forms import PackageForm
from shipping.models import Client, Package

packages = Blueprint('packages', __name__)

@packages.route("/client/<int:client_id>/receiver/<int:receiver_id>/package/new", methods=['GET', 'POST'])
@login_required
def new_package(client_id, receiver_id):      
    form = PackageForm()
    if form.validate_on_submit():
        package = Package(
            description = form.description.data,
            weight = form.weight.data,
            dimension = form.dimension.data,
            value = form.value.data,
            price = form.price.data,
            via = form.via.data,
            sender_id = client_id,
            receiver_id = receiver_id
        )
        db.session.add(package)
        db.session.commit()
        return redirect(url_for('clients.client', client_id = client_id, receiver_id=receiver_id))
    return render_template('new_package.html', form = form, client_id = client_id, receiver_id=receiver_id)

@packages.route("/package/view")
@login_required
def package():
    page = request.args.get('page', 1, type=int)
    client = Client.query.all()
    packages = Package.query.order_by(Package.date.desc()).paginate(page = page, per_page=10)
    return render_template('package.html', packages = packages, client_id = client)