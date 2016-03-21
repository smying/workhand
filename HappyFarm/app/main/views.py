# -*- coding:utf-8 -*-
from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from flask.ext.login import login_required, current_user
from flask.ext.sqlalchemy import get_debug_queries
from . import main
from .forms import EditProfileForm, AddShippingForm
from .. import db
from ..models import Permission,Role, User
from ..decorators import admin_required, permission_required

@main.route('/index')
def index():
	return render_template('index.html')

@main.route('/user/<int:id>')
def user(id):
	user = User.query.get_or_404(id)
	if user is None:
		abort(404)
	return render_template('user.html', user=user)

@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
	form = EditProfileForm()
	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.realname = form.realname.data
		current_user.sex = form.sex.data
		current_user.birthday = form.birthday.data
		current_user.about_me = form.about_me.data
		db.session.add(current_user)
		flash('Your Profile has been updated.')
		return redirect(url_for('.user', id=current_user.id))
	form.username.data = current_user.username
	form.realname.data = current_user.realname
	form.sex.data = current_user.sex
	form.birthday.data = current_user.birthday
	form.about_me.data = current_user.about_me
	return render_template('edit_profile.html', form=form)

@main.route('/safe')
@login_required
def safe():
	return render_template('safe.html')
	
@main.route('/shipping', methods=['GET', 'POST'])
def shipping():
	form = AddShippingForm()
	if form.validate_on_submit():
		current_user.shippingadd = form.province.data + ' ' + form.city.data + ' ' + form.detailadd.data + ' ' + form.zipcode.data + ' ' + form.phonenum.data + ' ' + form.receiver.data
		db.session.add(current_user)
	return render_template('shipping.html', form=form)

