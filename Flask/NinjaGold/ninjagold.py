from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = "ThisissecretThisissafe"

@app.route('/')
def index():
    if not 'gold' in session:
        session['gold'] = 0
    if not 'message' in session:
        session['message'] = []

    return render_template('ninjagold.html')

@app.route('/process_money', methods=['POST'])
def process():
    temparr = session['message']
    now = datetime.now()
    if str(request.form['building']) == 'farm':
        gold = random.randrange(10,21)
        session['gold'] += gold
        temparr.insert(0, "Earned " + str(gold) + " golds from the farm " + str(now.strftime("%Y-%m-%d %I:%M %p")))
    elif str(request.form['building']) == 'cave':
        gold = random.randrange(5,11)
        session['gold'] += gold
        temparr.insert(0, "Earned " + str(gold) + " golds from the cave " + str(now.strftime("%Y-%m-%d %I:%M %p")))
    elif str(request.form['building']) == 'house':
        gold = random.randrange(2,6)
        session['gold'] += gold
        temparr.insert(0, "Earned " + str(gold) + " golds from the house " + str(now.strftime("%Y-%m-%d %I:%M %p")))
    else:
        gold = random.randrange(0,51)
        win = random.randrange(0,2)
        if win == 0:
            gold = -gold
            session['gold'] += gold
            temparr.insert(0, "Entered a casino and lost " + str(-gold) + " golds.....Damn!" + str(now.strftime("%Y-%m-%d %I:%M %p")))
        else:
            session['gold'] += gold
            temparr.insert(0, "Entered a casino and won " + str(gold) + " golds.....Hell Yeah! " + str(now.strftime("%Y-%m-%d %I:%M %p")))

    session['message'] = temparr

    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


app.run(debug=True)