from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/projects')
def projectpage():
    return render_template('projects.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')

app.run(debug=True)