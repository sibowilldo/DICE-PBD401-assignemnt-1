from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from app import db
from services.forms import RegisterForm
from services.forms import LoginForm
from database.models import User
from flask_login import login_required, logout_user

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    form = LoginForm.LoginForm()
    return render_template('auth/login.html', form=form)


@auth.route('/login', methods=['POST'])
def handle_login():

    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=True)
    return redirect(url_for('routes.home'))


@auth.route('/register')
def register():
    form = RegisterForm.RegisterForm()
    return render_template('auth/register.html', form=form)


@auth.route('/register', methods=['POST'])
def handle_register():

    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(
        email=email).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.register'))

    user = User()
    user.email = email
    user.password = generate_password_hash(password, method='sha256')

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.home'))
