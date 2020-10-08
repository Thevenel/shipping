from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired




class PackageForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    weight = StringField('Weight', validators=[DataRequired()])
    dimension = StringField('Dimension', validators=[DataRequired()])
    value = StringField('Value', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    via = SelectField('Via', validate_choice=True, choices=[('Ocean'), ('Air')])
    submit = SubmitField('Next')