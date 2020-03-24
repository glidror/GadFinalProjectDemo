
### ----------------------------------------------------------- ###
### --- include all software packages and libraries needed ---- ###
### ----------------------------------------------------------- ###
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import TextField, TextAreaField, SelectField, SelectMultipleField, DateField, DateTimeField
from wtforms import StringField, PasswordField, HiddenField, SubmitField
from wtforms import IntegerField, DecimalField, FloatField, RadioField, BooleanField

from wtforms import validators, ValidationError
from wtforms.validators import DataRequired
from wtforms.validators import InputRequired

from wtforms.fields.html5 import DateField
### ----------------------------------------------------------- ###





## This class have the fields that are part of the Country-Capital demonstration
## You can see two fields:
##   the 'name' field - will be used to get the country name
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
class QueryFormStructure(FlaskForm):
    name   = StringField('Country Name:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')




## This class have the fields that are part of the Login form.
##   This form will get from the user a 'username' and a 'password' and sent to the server
##   to check if this user is authorised to continue
## You can see three fields:
##   the 'username' field - will be used to get the username
##   the 'password' field - will be used to get the password
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
class LoginFormStructure(FlaskForm):
    username   = StringField('User name:  ' , validators = [DataRequired()])
    password   = PasswordField('Pass word:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')



## This class have the fields of a registration form
##   This form is where the user can register himself. It will have sll the information
##   we want to save on a user (general information) and the username ans PW the new user want to have
## You can see three fields:
##   the 'FirstName' field - will be used to get the first name of the user
##   the 'LastName' field - will be used to get the last name of the user
##   the 'PhoneNum' field - will be used to get the phone number of the user
##   the 'EmailAddr' field - will be used to get the E-Mail of the user
##   the 'username' field - will be used to get the username
##   the 'password' field - will be used to get the password
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
class UserRegistrationFormStructure(FlaskForm):
    FirstName  = StringField('First name:  ' , validators = [DataRequired()])
    LastName   = StringField('Last name:  ' , validators = [DataRequired()])
    PhoneNum   = StringField('Phone number:  ' , validators = [DataRequired()])
    EmailAddr  = StringField('E-Mail:  ' , validators = [DataRequired()])
    username   = StringField('User name:  ' , validators = [DataRequired()])
    password   = PasswordField('Pass word:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')

## This class have the fields that the user can set, to have the query parameters for analysing the data
##   This form is where the user can set different parameters, depand on your project,
##   that will be used to do the data analysis (using Pandas etc.)
## You can see three fields:
##   The fields that will be part of this form are specific to your project
##   Please complete this class according to your needs
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
## class DataParametersFormStructure(FlaskForm):
class Covid19DayRatio(FlaskForm):
    countries = SelectMultipleField('Select Multiple:' , validators = [DataRequired] )
    start_date = DateField('Start Date (1/22/20 onwards):' , format='%Y-%m-%d' , validators = [DataRequired])
    end_date = DateField('Start Date (Yesterday backwards):' , format='%Y-%m-%d' , validators = [DataRequired])
    subnmit = SubmitField('submit')    

class SinglePresidentForm(FlaskForm):
    president = SelectField('President' , validators = [DataRequired] , choices=[('trump', 'Trump'), ('obama', 'Obama'), ('bush', 'Bush') , ('clinton', 'Clinton')])
    start_date = DateField('Start Date' , format='%Y-%m-%d' , validators = [DataRequired])
    end_date = DateField('End Date' , format='%Y-%m-%d' , validators = [DataRequired])
    kind = SelectField('Chart Kind' , validators = [DataRequired] , choices=[('line', 'line'), ('bar', 'bar')])
    subnmit = SubmitField('הצג')



### ----------------------------------------------------------- ###
###      Action Buttons
### ----------------------------------------------------------- ###
class ExpandForm(FlaskForm):
    submit1 = SubmitField('Expand')
    name="Expand" 
    value="Expand"
### ----------------------------------------------------------- ###
class CollapseForm(FlaskForm):
    submit2 = SubmitField('Collapse')
    name="Collapse" 
    value="Collapse"
### ----------------------------------------------------------- ###



### ----------------------------------------------------------- ###
###     Demo for using differnt field types
### ----------------------------------------------------------- ###
class AllOfTheAboveForm(FlaskForm):
    string_field_entry = StringField('Enter a String:' , validators = [DataRequired])
    text_area_field_entry = TextAreaField('Enter Text:' , validators = [DataRequired])
    password_field_entry = PasswordField('Enter Password:' , validators = [DataRequired])
    date_field_entry = DateField('Enter Date:' , format='%Y-%m-%d' , validators = [DataRequired])
    integer_field_entry = IntegerField('Enter an Integer:' , validators = [DataRequired])
    decimal_field_entry = DecimalField('Enter a Decimal:' , validators = [DataRequired])
    boolean_field_entry = BooleanField('Enter a Boolean:' , validators = [DataRequired])
    radio_field_entry = RadioField('Choose one of:' , validators = [DataRequired] , choices=[('1', 'A'), ('2', 'B'), ('3', 'C') , ('4', 'D')])
    select_field_entry = SelectField('Select:' , validators = [DataRequired] , choices=[('trump', 'Trump'), ('obama', 'Obama'), ('bush', 'Bush') , ('clinton', 'Clinton')])
    select_field_multiple_entry = SelectMultipleField('Select Multiple:' , validators = [DataRequired] , choices=[('trump', 'Trump'), ('obama', 'Obama'), ('bush', 'Bush') , ('clinton', 'Clinton')])
    subnmit = SubmitField('submit')


