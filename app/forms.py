from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, EmailField, IntegerField
from wtforms.validators import ValidationError, DataRequired
from app.models import Record
from datetime import date


class RecordForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    birthday = DateField('Birthday', default=date.today)
    phone = StringField('Phone', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    note = StringField('Note', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, name):
        user = Record.query.filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError('Please use a different name.')

    def validate_phone(form, phone):
        if len(phone.data) != 12:
            raise ValidationError('Invalid phone number.')
        if not phone.data.isdigit():
            raise ValidationError('Invalid phone number.')


class EditRecordForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    birthday = DateField('Birthday', validators=[DataRequired()])
    submit = SubmitField('Edit')


class EditPhoneForm(FlaskForm):
    number = StringField('Phone')
    submit = SubmitField('Edit')

    def validate_phone(form, phone):
        if len(phone.data) != 12:
            raise ValidationError('Invalid phone number.')
        if not phone.data.isdigit():
            raise ValidationError('Invalid phone number.')


class EditEmailForm(FlaskForm):
    title = EmailField('Email')
    submit = SubmitField('Edit')


class EditAddressForm(FlaskForm):
    title = StringField('Address')
    submit = SubmitField('Edit')


class EditNoteForm(FlaskForm):
    title = StringField('Note')
    submit = SubmitField('Edit')


class AddTagForm(FlaskForm):
    title = StringField('Tag')
    submit = SubmitField('Submit')


class DeleteForm(FlaskForm):
    submit = SubmitField('Yes')
    cancel = SubmitField('No')
