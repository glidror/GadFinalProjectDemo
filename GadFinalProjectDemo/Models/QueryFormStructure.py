
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class QueryFormStructure(FlaskForm):
    """This class is the list of the fields that will participate in our form"""
    name   = StringField('Country Name?)' , validators = [DataRequired()])
    submit = SubmitField('Submit')