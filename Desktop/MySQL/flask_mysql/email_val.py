from flask import Flask, request, redirect, render_template, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'email')
# an example of running a query
print mysql.query_db("SELECT * FROM users")

@app.route('/')

def emailForm():
    return render_template('email_validation.html')


@app.route('/emailVal', methods =['POST'])

def validation():
    if len(request.form['emailVal']) < 1:
        flash ("Don't leave blank!")
    elif not EMAIL_REGEX.match(request.form['emailVal']):
        flash('Not a validation Email')
    else:
        flash('Thanks for the Email')
        query = "INSERT INTO users (email, created_at, update_at) VALUES (:email, NOW(), NOW())"
        data = {
                'email': request.form['emailVal'],
                }
        mysql.query_db(query, data)

        query = "SELECT * FROM users"
        email = mysql.query_db(query)

        return render_template('display_email.html', all_users=email)

    return redirect('/')


@app.route('/display_email')

def index():
    return redirect('/')

@app.route('/remove_friend/<users_id>', methods=['POST'])

def delete(users_id):
    query = "DELETE FROM users WHERE id = :id"
    data = {'id': request.form['users_id']}
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
