from flask import render_template, request, redirect, url_for
from app import app
from config import questions, answers, correctAnswers

points = 0;

@app.route('/')
@app.route('/index')
def index():
    global points;
    points = 0;
    return render_template('index.html')

@app.route('/startQuiz/<number>')
def startQuiz(number):
    integerNumber = int(number) - 1
    
    question = questions[integerNumber]
    options = answers[integerNumber]
    
    return render_template('startQuiz.html', question=question, options=options, questionNumber=number)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/submitAnswer', methods=['POST'])
def submitAnswer():
    global points
    answer = request.form['answer']
    questionNumber = int(request.form['questionNumber'])
    nextQuestionNumber = questionNumber + 1

    if(correctAnswers[questionNumber - 1] == int(answer)):
        points = points + 1
    if nextQuestionNumber == 6:
        return redirect(url_for('result'))
    
    return redirect(url_for('startQuiz', number=str(nextQuestionNumber)))

@app.route('/result')
def result():
    global points
    return render_template('result.html', points=points)

