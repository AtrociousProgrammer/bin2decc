from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired

class ConversionForm(FlaskForm):
    decimal = DecimalField('Decimal: ', validators=[DataRequired()], places=None)
    binary = DecimalField('Binary: ', places=None, validators=[DataRequired()])
    submit = SubmitField('Convert')
