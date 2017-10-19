from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def form():
    return render_template('form.html')



app.run(debug=True)