import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];


@app.route('/')
def renderMain():
    return render_template('SecureQuizAppHome.html')
    
@app.route('/page1')
def renderPage1():
    return render_template('SecureQuizAppPage1.html')
    
@app.route('/page2')
def renderPage2():
    return render_template('SecureQuizAppPage2.html')
    
@app.route('/page3')
def renderPage3():
    return render_template('SecureQuizAppPage3.html')
    
@app.route('/page4')
def renderPage4():
    return render_template('SecureQuizAppPage4.html')
    
@app.route('/page5')
def renderPage5():
    return render_template('SecureQuizAppPage5.html')
    
@app.route('/page6')
def renderPage6():
    return render_template('SecureQuizAppPage6.html')
    

if __name__=="__main__":
    app.run(debug=False)