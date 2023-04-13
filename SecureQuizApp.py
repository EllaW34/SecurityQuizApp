import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session
from timeit import default_timer as timer
import time

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];


@app.after_request
def add_header(response):
    if 'Chache-Control' not in response.headers:
        response.headers ['Cache-Control'] = 'no-store'
    return response

@app.route('/')
def renderMain():
    return render_template('SecureQuizAppHome.html')
    
@app.route('/startOver')
def startOver():
    session.clear()
    return redirect(url_for('renderMain'))
    
@app.route('/page1', methods=['GET', 'POST'])
def renderPage1():
    session["start"] = timer()
    print(session["start"])
    print("a1" in session)
    if "a1" in session:
        return redirect("/page2", code=307)
    return render_template('SecureQuizAppPage1.html')
    
@app.route('/page2', methods=['GET', 'POST'])
def renderPage2():
    if "a1" in request.form and 'a1' not in session:
        session["a1"]=request.form['a1']
    if "a2" in session:
        return redirect("/page3", code=307)
    print(session)
    return render_template('SecureQuizAppPage2.html')
    
@app.route('/page3', methods=['GET', 'POST'])
def renderPage3():
    if "a2" in request.form and 'a2' not in session:
        session["a2"]=request.form['a2']
    if "a3" in session:
        return redirect("/page4", code=307)
    return render_template('SecureQuizAppPage3.html')
    
@app.route('/page4', methods=['GET', 'POST'])
def renderPage4():
    if "a3" in request.form and 'a3' not in session:
        session["a3"]=request.form['a3']
    if "a4" in session:
        return redirect("/page5", code=307)
    return render_template('SecureQuizAppPage4.html')
    
@app.route('/page5', methods=['GET', 'POST'])
def renderPage5():
    if "a4" in request.form and 'a4' not in session:
        session["a4"]=request.form['a4']
    if "a5" in session:
        return redirect("/page6", code=307)
    return render_template('SecureQuizAppPage5.html')
    
@app.route('/page6', methods=['GET', 'POST'])
def renderPage6():
    end = timer()
    if "a5" in request.form and 'a5' not in session:
        session["a5"]=request.form['a5']
    score = 0;
    an1 = "Incorrect"
    an2 = "Incorrect"
    an3 = "Incorrect"
    an4 = "Incorrect"
    an5 = "Incorrect"
    ans1 = session['a1']
    ans2 = session['a2']
    ans3 = session['a3']
    ans4 = session['a4']
    ans5 = session['a5']
    if(session['a1'] == "Their" or session['a1'] == "their"):
        score += 1;
        an1 = "Correct"
    if(session['a2'] == "1.9" or session['a2'] == "less than 2" or session['a2'] == "Less than 2"):
        score += 1;
        an2 = "Correct"
    if(session['a3'] == "Fleshy" or session['a3'] == "fleshy"):
        score += 1;
        an3 = "Correct"
    if(session['a4'] == "Rhode Island" or session['a4'] == "rhode island" or session['a4'] == "Rhode island"):
        score += 1;
        an4 = "Correct"
    if(session['a5'] == "True" or session['a5'] == "true"):
        score += 1;
        an5 = "Correct"
        
    clock = end-session['start']
    
    return render_template('SecureQuizAppPage6.html', ans1 = ans1, ans2 = ans2, ans3 = ans3, ans4 = ans4, ans5 = ans5, score = score, an1 = an1, an2 = an2, an3 = an3, an4 = an4, an5 = an5, clock = str(clock)[:-12])
    

if __name__=="__main__":
    app.run(debug=True)