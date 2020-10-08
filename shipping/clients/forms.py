import us
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired



class ClientForm(FlaskForm):
    id_number = StringField('Identification Number', validators=[DataRequired()])
    companyName = StringField('Company Name', validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = SelectField('State', validators=[DataRequired()], choices=us.STATES)
    zCode = StringField('Zip Code', validators=[DataRequired()])
    phoneNumber = StringField('Phone Number', validators=[DataRequired()])
    submit = SubmitField('Create')