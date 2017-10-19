from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = ("CodingDojo")
mysql = MySQLConnector(app,'listserv')

@app.route('/')
def index():
    if session.get('emailval') == None:
        session['emailval'] = True
    emails = mysql.query_db("SELECT * FROM listserv")
    return render_template('index.html', all_emails = emails)

@app.route('/process', methods=['POST'])
def create():
    email = request.form['email']
    if re.match(r"[^@]+@[^@]+\.[^@]+",email):
        query = "INSERT INTO listserv (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
                'email': request.form['email']
            }
        mysql.query_db(query, data)
        session['emailval'] = True
    else:
        session['emailval'] = False
    return redirect('/')

@app.route('/check', methods=['POST'])
def check():
    email = request.form['emailcheck']
    query = "SELECT email from listserv WHERE email = :email_check"
    data = {
        'email_check':email
    }
    emailcheck = mysql.query_db(query, data)
    print emailcheck
    if emailcheck:
        flash("Valid Email")
        return redirect('/success')
    else:
        flash("Not Valid")
        return redirect('/')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/goback')
def goback():
    return redirect('/')
app.run(debug=True)