from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re 
import md5
app = Flask(__name__)
mysql = MySQLConnector(app, 'thewall')
app.secret_key = "Thisismysecretkey"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('thewall.html')

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
    if len(request.form['first_name']) < 1:
        print "first name"
        flash("Please enter a First Name with at least 2 characters", 'reg')
        error += 1
    if len(request.form['last_name']) < 1:
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
        mysql.query_db(query, data)
        
        # This is how we set session['user'] and session['user_id'] if we're getting into the wall via the registration form

        test_query = "SELECT id FROM users WHERE email = :email"
        data1= {
            "email": request.form['email']
        }
        testid = mysql.query_db(test_query, data1)
        session["user"] = request.form['first_name']
        session["user_id"] = testid[0]['id']
        
        return redirect('/thewall')

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
        profile_query = "SELECT first_name, id FROM users WHERE email = :email"
        profile_data = {
            "email": request.form['email']
        }
        wall_user = mysql.query_db(profile_query, profile_data)
        # This is how we set session['user'] and session['user_id'] if we're getting into the wall via the login form
        session['user'] = wall_user[0]['first_name']
        session['user_id'] = wall_user[0]['id']
        print session['user']
        print session['user_id']
        return redirect('/thewall')
    else:
        flash("Please enter a valid username/password", 'log')
        return redirect('/')

@app.route('/messagepost', methods=['POST'])
def postmessage():
    message_query = "INSERT INTO messages (user_id, message, created_at, updated_at) Values (:user_id, :message, NOW(), NOW())"
    message_data = {
        "user_id": request.form['user_id'],
        "message": request.form['message']
    }
    mysql.query_db(message_query, message_data)
    return redirect('/thewall')

@app.route('/commentpost', methods=['POST'])
def postcomment():
    comment_query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) Values (:message_id, :user_id, :comment, NOW(), NOW())"
    comment_data = {
        "message_id": request.form['message_id'],
        "user_id": request.form['user_id'],
        "comment": request.form['comment']
    }
    mysql.query_db(comment_query, comment_data)
    return redirect('/thewall')

@app.route('/thewall')
def wall():
    message_display_query = "SELECT messages.message, messages.id, users.first_name, date_format(messages.created_at, '%M %D %Y') as created_at FROM users JOIN messages on users.id = messages.user_id ORDER BY messages.created_at DESC"
    display_message = mysql.query_db(message_display_query)

    # THIS IS WHERE I WAS.......DISPLAY THE COMMENTS UNDER THE MESSAGES

    comment_display_query = "SELECT comments.comment, users.first_name, date_format(comments.created_at, '%M %D %Y') as created_at, message_id FROM comments JOIN users on comments.user_id = users.id JOIN messages on messages.id = comments.message_id"
    display_comment = mysql.query_db(comment_display_query)
    
    
    
    return render_template('wallmessages.html', message=display_message, comment=display_comment)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


app.run(debug=True)