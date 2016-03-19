# -*- coding:utf-8 -*-
import os
from flask import render_template, redirect, flash, session, url_for, current_app, request
from .. import db
from .forms import LoginForm, RegistrationForm
from flask.ext.login import login_user, logout_user, login_required
from ..models import User
from . import auth
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import StringIO

#随机字母
#def rndChar():
#	return chr(random.randint(65, 90))

#随机颜色1:
#def rndColor():
#	return(random.randint(64, 255),random.randint(64, 255),random.randint(64, 255))

#随机颜色2:
#def rndColor2():
	#return(random.randint(32, 127),random.randint(32, 127),random.randint(32, 127))

#240x60:
#width = 60*4
#height = 60
#image = Image.new('RGB',(width,height),(255,255,255))
#创建Font对象
#font = ImageFont.truetype('/Library/Fonts/Arial.ttf',36)
#创建Draw对象:
#draw = ImageDraw.Draw(image)
#填充每个像素:
#for x in range(width):
#	for y in range(height):
#		draw.point((x,y),fill=rndColor())
#输出文字
#for t in range(4):
#	draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
#模糊:
#image = image.filter(ImageFilter.BLUR)
#image.save('code.jpg','jpeg');


@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email=form.email.data, phonenum=form.phonenum.data, password=form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('you have successfully register.')
		return redirect(url_for('.login'))
	return render_template('auth/register.html', form=form)

'''@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data is not None:
			user = User.query.filter_by(email=form.email.data).first()
		else:
			user = User.query.filter_by(phonenum=form.phonenum.data).first()
	if user:
		if 'code_text' in session and session['code_text'] != form.verification_code.data:
			code_img, code_text = generate_verification_code()
			session['code_text'] = code_text
			return render_template('user/login.html', form=form, code_img=code_img)
	code_img, code_text = generate_verification_code()
	session['code_text'] = code_text
	return render_template('user/login.html', form=form, code_img=code_img)
	if user is not None and user.verify_password(form.password.data):
		login_user(user)
		return redirect(url_for('main.index'))
	flash('Invalid username or password.')
	code_img, code_text = generate_verification_code()
	session['code_text'] = code_text
	return render_template('user/register.html', form=form, code_img=code_img)

{% if form.errors.verification_code %}
        <div class="form-group has-error required">
            {{ form.verification_code.label(class="control-label") | safe }}
            {{ form.verification_code(class="form-control", required=True) }}
            {% for error in form.errors.verification_code %}
                <p class="help-block">{{ error }}</p>
            {% endfor %}
        </div>
        {% else %}
        <div class="form-group required">
            {{ form.verification_code.label(class="control-label") | safe }}
            <label class="control-label"><img src="{{ url_for('static', filename='image/code/'+code_img) }}"></label>
            {{ form.verification_code(class="form-control", required=True) }}
        </div>
        {% endif %}'''

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		email = form.email.data
		if email:
			user = User.query.filter_by(email=form.email.data).first()
		else:
			user = User.query.filter_by(phonenum=form.phonenum.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(url_for('main.index'))
		flash('Invalid username or password.')
	return render_template('auth/login.html', form=form)
