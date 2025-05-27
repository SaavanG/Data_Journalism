from flask import Flask, render_template, request
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def home():
    return render_template('about.html')

@app.route('/city')
def citypage():
    return render_template('city.html')

@app.route('/zip')
def zip():
    return render_template('zip.html')

if __name__ == '__main__':
    app.run(debug=True)
