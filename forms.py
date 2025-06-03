from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, RadioField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileAllowed
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])

class RegistrationForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])

class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField('Содержание', validators=[DataRequired()])
    location = StringField('Местоположение')
    file = FileField('Прикрепить файл')

class TravelerForm(FlaskForm):
    name = StringField('Ваше имя', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    country = SelectField('Страна проживания', choices=[
        ('', 'Выберите страну'),
        ('Россия', 'Россия'),
        ('США', 'США'),
        ('Германия', 'Германия'),
        ('Франция', 'Франция'),
        ('Япония', 'Япония')
    ], validators=[DataRequired()])
    experience = RadioField('Опыт путешествий', choices=[
        ('beginner', 'Начинающий (1-5 поездок)'),
        ('experienced', 'Опытный (5-20 поездок)'),
        ('expert', 'Эксперт (20+ поездок)')
    ], default='beginner')
    newsletter = BooleanField('Подписаться на рассылку')
    submit = SubmitField('Отправить')

class UploadForm(FlaskForm):
    photo = FileField('Выберите фото', validators=[
        DataRequired(),
        FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Только изображения!')
    ])
    submit = SubmitField('Загрузить')

