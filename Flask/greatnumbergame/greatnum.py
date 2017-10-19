from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "9r09230rh2hsodigah"

@app.route('/')
def index():
    random.randrange(0, 101)
    session['message'] = ""
    session['number'] = random.randrange(0, 101)
    print session['number']

    return render_template('greatnum.html')

@app.route('/process', methods=['POST'])
def process():
    print request.form['number']
    if int(request.form['number']) > session['number']:
        session['message'] = "Your guess is too high"
    elif int(request.form['number']) < session['number']:
        session['message'] = "Your guess is too low"
    else:
        session['message'] = "Nice Job!"

    return render_template('greatnum.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


app.run(debug=True)