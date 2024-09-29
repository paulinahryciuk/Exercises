from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return ("Home home")

@app.route('/submit', method = ["POST"])
def submit():
    return render_template('formularz.html')