from flask import render_template, request, flash, redirect, url_for, session
from app import app, db
from app.models import *

@app.route('/add', methods=['POST','GET'])
def add():
	if request.method == 'POST':
		post = Post(request.form['title'], request.form['body'])
		db.session.add(post)
		db.session.commit()
		flash('New entry was successfully added')

	return render_template('add.html')

@app.route('/')
def index():
	post = Post.query.all()
	return render_template('index.html', post=post)



@app.route('/login', methods=['POST','GET'])
def login():
	if request.method == 'POST':
		user = Users.query.filter_by(name=request.form['uname']).filter_by(password=request.form['password']).first()
		if user:
			flash('U wer js logged in')
			session['uname'] = request.form['uname']
			return redirect(url_for('index'))
		else:
			flash('Wrong details')
	return render_template('login.html') 

@app.route('/register', methods=['POST','GET'])
def register():
	if request.method == 'POST':
		reguser = Users(request.form['uname'], request.form['password'])
		db.session.add(reguser)
		db.session.commit()
		flash("User created")
	return render_template('register.html')

@app.route('/logout')
def logout():
	session.pop('uname',None)
	flash("You wer jst logged out")
	return redirect(url_for('login'))
