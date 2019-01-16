from flask import render_template, flash, redirect
from app import app

from app.forms import LoginForm, AddUrlToQueue, ViewData

app.debug = True

from flask_sqlalchemy import SQLAlchemy

# from app import tables
from app.tables import *

from app import urlupsert
from app.urlupsert import urlUpsert
from app.get_crawl_data import getData



@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Joe'}
    return render_template('index.html', title='Home', user=user)

@app.route('/hello/<anything>')
def hello(anything=None):
	# return f"hello wurld {anything}"
    return render_template('index.html', title='hay gurl', name=anything)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(form.username)
    print(form.password)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/add_url', methods=['GET', 'POST'])
def add_url():
    form = AddUrlToQueue()
    if form.url.data and form.url.data != "":
    	urlUpsert(form.url.data)
    return render_template('add_url.html', title='Add a URL to the Queue', form=form)


@app.route('/view_data', methods=['GET', 'POST'])
def view_data():
    form = ViewData()
    data_result = {'results': [], 'static_data': {}}
    print(data_result)
    if form.url.data and form.url.data != "":
        data_result = getData(form.url.data)
        print(data_result)
    return render_template('view_data.html', title='ayy check out this data bro lmao', form=form, data_result=data_result.return_data[0], dyn_result=data_result.return_data[1])
