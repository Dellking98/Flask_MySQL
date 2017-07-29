# Create a simple registration page with the following fields:
# email first_name last_name password confirm_password

# Here are the validations you must include:
# All fields are required and must not be blank
# First and Last Name cannot contain any numbers
# Password should be more than 8 characters
# Email should be a valid email
# Password and Password Confirmation should match
# When the form is submitted, make sure the user submits
# appropriate information. If the user did not submit appropriate
# information, return the error(s) above the form that asks the user to
# correct the information.
# Message Flashing with Categories
# For this, you will need to use flash messages at the very least.
# You may have to take this one step further and add categories to the
# flash messages. You can learn that from the flask doc: flash messages
# with categories
# If the form with all the information is submitted properly,
# simply have it say a message "Thanks for submitting your information."

# Ninja Version:
# Add the validation that requires a password to have at least 1
# uppercase letter and 1 numeric value.
# Hacker Version:
# Add a birth-date field that must be validated as a valid date
# (and must be from the past).

# from flask import Flask, render_template, session, redirect, request, flash
# app = Flask(__name__)
# app.secret_key = 'KeepItSecretKeepItSafe'
# @app.route('/')
#
# def formWeb():
#     return render_template('regFormWeb.html')
#
# @app.route('/user2', methods = ["POST"])
#
# def viewForm():
#     session['fName'] = request.form['fName']
#     session['lName'] = request.form['lName']
#     session['eMail'] = request.form['eMail']
#     session['pWord'] = request.form['pWord']
#     session['confPworld'] = request.form['confPworld']
#
#     # if len(request.form) == " ":
#     #     print 'You need to fill out the whole form'
#     #     flash ('You need to fill out the whole form')
#     # else:
#     #     print "Thank you for Filling it out"
#     #     flash ('Thank you for filling it out')
#
#     return redirect('/viewForm')
#
# @app.route('/viewForm')
#
# def view():
#     return render_template('index2.html')
#
#
#
# app.run(debug = True)

from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key ='secret'
@app.route('/')

def form1():
    return render_template('regFormWeb.html')

@app.route('/User1', methods = ["POST"] )

def create_users1():
    session['fName'] = request.form['fName']
    session['lName'] = request.form['lName']
    session['eMail'] = request.form['eMail']
    session['pWord'] = request.form['pWord']
    #session['confPworld'] = request.form['confPworld']

    if session['fName'].isalpha() != True or session['lName'].isalpha() != True or len(session['pWord']) < 9 or EMAIL_REGEX.match(session['eMail']) or session['pWord'] == request.form['confPworld']:
         error = 'Invalid credentials'
         flash(error)
    else:
        flash('Thank you for submitting')


    return redirect('/seccess')

@app.route('/seccess')

def seccess():
    return render_template('index2.html')

@app.route('/reset', methods=['POST'])

def reset():
    return redirect('/')


app.run(debug = True)
