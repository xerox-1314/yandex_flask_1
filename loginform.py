from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    user_id = StringField('id астронавта', validators=[DataRequired()])
    user_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    cap_id = StringField('id капитана', validators=[DataRequired()])
    cap_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')