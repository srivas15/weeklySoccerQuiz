from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route('/startQuiz')
def startQuiz():
    return render_template('startQuiz.html', question="Who scored a hat-trick last gameweek?", option1="Romelu Lukaku")

@app.route('/login')
def login():
    return render_template('login.html')

