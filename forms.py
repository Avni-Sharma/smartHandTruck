from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, SubmitField
from wtforms.validators import DataRequired
from wtforms import ValidationError


class RegistrationForm(FlaskForm):

    FirstName=StringField('FirstName',validators=[DataRequired()])
    LastName=StringField('LastName',validators=[DataRequired()])
    Email=StringField('Email',validators=[DataRequired()])
    Phone=StringField('Phone',validators=[DataRequired()])
    Zip=IntegerField('Zip',validators=[DataRequired()])
    submit=SubmitField('Register')

    def check_email(self,field):

        if Customers.query.filter_by(Email=field.data).first():
            raise ValidationError('Your email has already been registered')
            


class UpdateForm(FlaskForm):

    Email=StringField('Email',validators=[DataRequired()])
    FirstName=StringField('FirstName',validators=[DataRequired()])
    LastName=StringField('LastName',validators=[DataRequired()])
    Phone=StringField('Phone',validators=[DataRequired()])
    Zip=IntegerField('Zip',validators=[DataRequired()])
    update= SubmitField('Update')

class DeleteForm(FlaskForm):

    Email=StringField('Email',validators=[DataRequired()])
    # FirstName=StringField('FirstName',validators=[DataRequired()])
    # LastName=StringField('LastName',validators=[DataRequired()])
    # Phone=StringField('Phone',validators=[DataRequired()])
    # Zip=IntegerField('Zip',validators=[DataRequired()])
    Delete= SubmitField('Delete')
