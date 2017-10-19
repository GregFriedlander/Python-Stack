from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "234fsdjfali234234"

@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 0
    return render_template('counter.html', count=session['visits'])

@app.route('/+2')
def plustwo():
    session['visits'] += 1
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


app.run(debug=True)