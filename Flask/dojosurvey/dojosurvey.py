from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "Thisismysecretkey"

@app.route('/')
def homepage():
    return render_template('dojosurvey.html')

@app.route('/survey', methods=['Post'])
def info():
    x = 'true'
    if len(request.form['name']) < 1:
        flash("Name cannot be empty")
        x = 'false'
    if len(request.form['comment']) < 1 or len(request.form['comment']) > 120:
        flash("Comment area must be between 1 and 120 characters")
        x = 'flase'
    
    if x == 'true':
        return render_template('submit.html', name = request.form['name'], location = request.form['location'], language = request.form['language'], comment = request.form['comment'] )
    else:
        return redirect('/')







    



app.run(debug=True)