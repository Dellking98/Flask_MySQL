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

# def counter():
#     session['counter1'] = random.randint( 1 , 100)

@app.route('/')

def gameWed():
    return render_template('gameWeb.html')

@app.route('/gettingNum', methods=['POST'])

def the_form():
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

    return redirect('/')

app.run(debug = True)
