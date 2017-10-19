from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def ninja_color(color):
    if color == "purple":
        return render_template('donny.html')
    elif color == "blue":
        return render_template('leo.html')
    elif color == "red":
        return render_template('raphael.html')
    elif color == "orange":
        return render_template('michelangelo.html')
    return render_template('notapril.html')

app.run(debug=True)
    
