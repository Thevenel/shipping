from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ReceiverForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    phoneNumber = StringField('Phone Number', validators=[DataRequired()])
    submit = SubmitField('Save')