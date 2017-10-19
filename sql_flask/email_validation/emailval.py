from flask import Flask, render_template, request, redirect, flash
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'email_validation_assign')
app.secret_key = "Thisisthesecret key"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('emailval.html')

@app.route('/verification', methods=['POST'])
def validate():
    query = "SELECT email FROM users WHERE email = :email_check"
    data = {
        'email_check': request.form['email']
    }
    emailcheck = mysql.query_db(query, data)
    email = mysql.query_db("SELECT * FROM users")
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Yo, That ain't even an email address")
    if emailcheck:
       flash("Valid Email")
       return render_template('/success.html', all_emails=email)
    else:
        flash("Please enter a Valid email address")
        return redirect('/')


app.run(debug=True)