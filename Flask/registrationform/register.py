from flask import Flask, render_template, request, redirect, session, flash
import re
from datetime import datetime
date_time = datetime.now()
date = date_time.date()
app = Flask(__name__)
app.secret_key = "Thisismysecretkey"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def homepage():
    return render_template('register.html')

@app.route('/register', methods=['Post'])
def register():
    error = 0
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        error += 1
    if len(request.form['first_name']) < 1:
        flash("Please enter a First Name!")
        error += 1
    if len(request.form['last_name']) < 1:
        flash("Please enter a Last Name!")
        error += 1
    if len(request.form['password']) < 1:
        flash("Please enter a Password!")
        error += 1
    if len(request.form['password']) < 8 and len(request.form['password']) > 0:
        flash("Password must be at least 8 characters long")
        error += 1
    if re.search('[0-9]', str(request.form['password'])) is None and re.search('[A-Z]', str(request.form['password'])) is None:
        flash("Your password must contain at least one Uppercase letter and one Number")
        error += 1 
    if request.form['confirmpassword'] != request.form['password']:
        flash("Please confirm password correctly!")
        error += 1
    if str(request.form['birthday']) > str(date):
        flash("Your birthday must be in the past!")
        error += 1
    if error > 0:
        flash("Please re-enter all of you information")
    else:
        flash("Success! Thanks for registering!")
    return redirect('/')





app.run(debug=True)
