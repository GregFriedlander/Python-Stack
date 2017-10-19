from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re 
import md5
app = Flask(__name__)
mysql = MySQLConnector(app, 'login_reg_assign')
app.secret_key = "Thisismysecretkey"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    print "something else"
    return render_template('logreg.html')

@app.route('/register', methods=['POST'])
def register():

    # This is checking to see if the email being registered is already in the database

    check_query = "SELECT * FROM users WHERE email = :email"
    check_data = {
        "email" : request.form['email']
    }
    exists = mysql.query_db(check_query, check_data)
    if len(exists) > 0:
        flash("That email is already is in use", 'reg')
        return redirect('/')

    # This is checking to make sure that the registration fields are all correct

    error = 0
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Yo, That's Not Even an Email", 'reg')
        error += 1
    if len(request.form['first_name']) < 3:
        print "first name"
        flash("Please enter a First Name with at least 2 characters", 'reg')
        error += 1
    if len(request.form['last_name']) < 3:
        flash("Please enter a Last Name with at least 2 characters", 'reg')
        error += 1
    if len(request.form['password']) < 8 and len(request.form['password']) > 0:
        flash("Password must be at least 8 characters long", 'reg')
        error += 1
    if request.form['confirm_password'] != request.form['password']:
        flash("Please confirm password correctly!", 'reg')
        error += 1
    if error > 0:
        flash("Please re-enter all of you information", 'reg')
        return redirect('/')
    else:
        # This is putting the new user into the database

        password = md5.new(request.form['password']).hexdigest()
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "password": password
        }
        create_user = mysql.query_db(query, data)
        
        # "user" below can be anything, it just has to be consistent throughout the code

        if "user" not in session:
            session["user"] = create_user
        return render_template('success.html')

@app.route('/login', methods=['POST'])
def login():
     
    #  This is checking to see if the login info matches up to data in the database

    login_query = "SELECT * FROM users WHERE email = :email AND password = :password"
    login_password = md5.new(request.form['password']).hexdigest()
    login_data = {
        "email": request.form['email'],
        "password": login_password
    }
    login_exists = mysql.query_db(login_query, login_data)
    if len(login_exists) > 0:
        if "user" not in session:
            session["user"] = login_exists
        return render_template('success.html')
    else:
        flash("Please enter a valid username/password", 'log')
        return redirect('/')

    
    
    
app.run(debug=True)