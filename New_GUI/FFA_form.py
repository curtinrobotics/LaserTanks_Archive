from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import Required
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField

from wtforms import validators, ValidationError

class MultiCheckboxField(SelectMultipleField):
	widget			= ListWidget(prefix_label=False)
	option_widget	= CheckboxInput()

class FFAF(Form):
   name = TextField("Name Of Student",[validators.Required("Please enter your name.")])
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   Address = TextAreaField("Address")
   
   email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])
   
   Age = IntegerField("age")
   
   project = RadioField('Project', choices = [('LT', 'Laser Tank'), 
      ('CC', 'Climbing Clock')])

   language = MultiCheckboxField('Languages', choices = [('cpp', 'C++'), 
      ('py', 'Python'),('c89', 'C89'),('c99', 'C99')])
   
   submit = SubmitField("Send")