import datetime
from os import environ as env

from flask import Flask
from flask import render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy

from forms import StateForm
from config import Config

application = Flask(__name__)
application.config.from_object(Config)


application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///state.db' \
    if env.get("FLASK_DEBUG") is not None \
    else f"mysql://{env['RDS_USERNAME']}:{env['RDS_PASSWORD']}@{env['RDS_HOSTNAME']}/{env['RDS_DB_NAME']}"
db = SQLAlchemy(application)


class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(120), nullable=False)
    symptons = db.Column(db.UnicodeText(), nullable=True)
    age = db.Column(db.Integer(), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    zip_code = db.Column(db.String(120), nullable=False)
    country_code = db.Column(db.String(2), nullable=False)
    added = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<State {self.email} {self.added} {self.status}>'

    def save(self):
        db.session.add(self)
        db.session.commit()


@application.before_first_request
def create_tables():
    db.create_all()


@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html', title='Home')


@application.route('/collect', methods=['GET', 'POST'])
def collect():
    form = StateForm()
    if form.validate_on_submit():
        flash(f'Data collected for user {form.email.data}')
        State(email=form.email.data, status=form.status.data, symptons=form.symptoms.data, age=form.age.data,
              gender=form.gender.data, zip_code=form.zip_code.data, country_code=form.country_code.data.lower(),
              added=datetime.datetime.utcnow()).save()
        return redirect('/index')
    return render_template('collect.html', title='Collect', form=form)


if __name__ == '__main__':
    application.run()
