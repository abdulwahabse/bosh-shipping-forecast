from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)