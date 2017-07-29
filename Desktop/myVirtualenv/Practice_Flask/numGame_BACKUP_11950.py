# Create a site that when a user loads it creates a random number between
# 1-100 and stores the number in session. Allow the user to guess at the number
#  and tell them when they are too high or too low. If they guess the correct
#  number tell them and offer to play again.
#
# In order to generate a random number you can use the "random" python module:




from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key ='secret'

@app.route('/')

def gameWed():
    if "counter1" not in session:
        session['counter1'] = random.randint( 1 , 100)
    return render_template('gameWeb.html')

@app.route('/gettingNum', methods=['POST'])

def the_form():
<<<<<<< HEAD
    user = int(request.form['inBox'])
    session['counter1'] = random.randint( 1 , 100)
    if user < session['counter1']:
        session['user'] = 'Your numder is to low'
        print 'Your numder is to low'
    elif user > session['counter1']:
        session['user'] = 'Your numder is to high'
        print 'Your number is to high'
    elif user is session['counter1']:
        session['user'] = 'Winner'
        print 'Winner'
    return redirect('/')

@app.route('/reset', methods = ["POST"])

def playAgain():
    session.clear
=======

    # user = int(request.form['inBox'])

    if session['counter1'] == int(request.form['inBox']):
        session['result'] = 'correct'

    elif session['counter1'] < int(request.form['inBox']):
        session['result'] = 'high'

    else:
        session['result'] = 'low'
>>>>>>> 46f67868cf29986bb23eaabd6f99c3ee786e6b50

    return redirect('/')

@app.route('/reset')

def playAgain():
    # session.clear
    session.pop('counter1')
    session.pop('result')
    return redirect('/')

app.run(debug = True)
