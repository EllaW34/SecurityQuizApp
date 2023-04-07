import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];


@app.route('/')
def renderMain():
    return render_template('SecureQuizAppHome.html')
    
@app.route('/startOver')
def startOver():
    session.clear()
    return redirect(url_for('renderMain'))
    
@app.route('/page1', methods=['GET', 'POST'])
def renderPage1():
    print("a1" in session)
    if "a1" in session:
        return redirect("/page2")
    return render_template('SecureQuizAppPage1.html')
    
@app.route('/page2', methods=['GET', 'POST'])
def renderPage2():
    if "a1" in request.form:
        session["a1"]=request.form['a1']
    print(session)
    return render_template('SecureQuizAppPage2.html')
    
@app.route('/page3', methods=['GET', 'POST'])
def renderPage3():
    session["a2"]=request.form['a2']
    return render_template('SecureQuizAppPage3.html')
    
@app.route('/page4', methods=['GET', 'POST'])
def renderPage4():
    session["a3"]=request.form['a3']
    return render_template('SecureQuizAppPage4.html')
    
@app.route('/page5', methods=['GET', 'POST'])
def renderPage5():
    session["a4"]=request.form['a4']
    return render_template('SecureQuizAppPage5.html')
    
@app.route('/page6', methods=['GET', 'POST'])
def renderPage6():
    session["a5"]=request.form['a5']
    score = 0;
    an1 = "Incorrect"
    an2 = "Incorrect"
    an3 = "Incorrect"
    an4 = "Incorrect"
    an5 = "Incorrect"
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
    
    return render_template('SecureQuizAppPage6.html', score = score, an1 = an1, an2 = an2, an3 = an3, an4 = an4, an5 = an5)
    

if __name__=="__main__":
    app.run(debug=True)