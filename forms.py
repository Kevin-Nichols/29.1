from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, TextAreaField
from wtforms.validators import InputRequired, URL, Length, Optional, NumberRange

class AddPetForm(FlaskForm):
    """Form to add pets."""
    
    name = StringField('Pet name', validators=[InputRequired()])
    
    species = SelectField('species', choices=[('cat', 'Cat'), 
                                              ('dog', 'Dog'), 
                                              ('porcupine', 'Porcupine')
                                              ])
    
    photo_url = StringField('Photo URL', validators=[URL(), Optional()])
    
    age = IntegerField('Age', validators=[NumberRange(min=0, max=30), Optional()])
    
    notes = TextAreaField('Notes', validators=[Optional()])
    

class EditPetForm(FlaskForm):
    """Form to edit pets."""
    
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    
    notes = TextAreaField('Notes', validators=[Optional()])
    
    available = BooleanField('Pet available?')