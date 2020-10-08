from flask import Blueprint, render_template, url_for
from flask_login import login_required
from flask_weasyprint import render_pdf, HTML
from shipping.models import Package


report = Blueprint('report', __name__)



@report.route("/package/view/<int:package_id>")
@login_required
def report_one(package_id):
    package = Package.query.filter_by(id=package_id).first()
    return render_template('report_one.html', package = package, package_id = package_id)

# @report.route("/report_<package_id>.pdf")
# @login_required
# def report_one_pdf(package_id):
#     package = Package.query.filter_by(id=package_id).first()
#     return render_pdf(url_for('report_one', package = package, package_id = package_id))


@report.route("/report_<package_id>.pdf")
@login_required
def report_one_pdf(package_id):
    package = Package.query.filter_by(id=package_id).first()
    html= render_template('report_one.html', package = package, package_id = package_id)
    return render_pdf(HTML(string=html))

# @report.route("/package/view/<string:package_id>.pdf")
# @login_required
# def view_report(package_id):
#     package = Package.query.filter_by(id=package_id).first()
#     return render_pdf(url_for('report_one', package = package, package_id = package_id))



