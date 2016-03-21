# -*- coding:utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, DataRequired
from wtforms import ValidationError, SelectField, DateField, IntegerField
from flask.ext.pagedown.fields import PageDownField
from ..models import Role, User

class EditProfileForm(Form):
	username = StringField('username', validators=[Length(0,64)])
	realname = StringField('real name', validators=[Length(0,64)])
	sex = SelectField(u'性别', choices=[('female','female'), ('male', 'male')], validators=[DataRequired()], coerce=str)
	birthday = DateField('birthday')
	about_me = TextAreaField('About me')
	submit = SubmitField('submit')

class BusinessProfileForm(Form):
	location = StringField('location', validators=[Required(), Length(0,64)])
	storename = StringField('store name', validators=[Required(), Length(0,64)])
	introduce = TextAreaField('breif introduce')
	submit = SubmitField('submit')

class AddShippingForm(Form):
	province = StringField('province', validators=[Required(), Length(0,64)])
	city = StringField('city', validators=[Required(), Length(0,64)])
	detailadd = StringField('detail address', validators=[Required(), Length(0,64)])
	zipcode = StringField('zip code', validators=[Required(), Length(0,64)])
	phonenum = StringField('phone number', validators=[Required(), Length(0,64)])
	receiver = StringField('receiver name', validators=[Required(), Length(0,64)])
	submit = SubmitField('submit')
	
