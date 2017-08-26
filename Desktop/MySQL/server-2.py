from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt

app = Flask(__name__)
mysql = MySQLConnector(app, 'Login_and_Registration')
bcrypt = Bcrypt(app)
app.secret_key = ('secret_key')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    errors = False

    if len(first_name) < 2:
        flash('First name is too short')
        errors = True

    if len(last_name) < 2:
        flash('Last name is too short')
        errors = True

    if len(email) < 1:
        flash('Does not meet email length requirements')
        errors = True

    if len(password) < 8:
        flash('Password has to be at least 8 characters')
        errors = True

    if request.form['confirm'] != password:
        flash('Incorrect password')
        errors = True

    if errors == True:
        return redirect('/')

    else:

        email_validate_query = ('SELECT * FROM users WHERE email = :email LIMIT 1')
        email_data = {
            'email': email
        }
        user = mysql.query_db(email_validate_query, email_data)

        if len(user) > 0:
            flash('Email is already used, please choose a new email')
            return redirect('/')

        else:
            pw_hash = bcrypt.generate_password_hash('password')
            insert_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
            query_data = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'pw_hash': pw_hash
                }

            # test = mysql.query_db = (insert_query, query_data)
            mysql.query_db(insert_query, query_data)
            # print test
            return render_template('success.html', first_name=first_name)

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    select_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = {'email': email}
    user = mysql.query_db(select_query, query_data)
    print user

    if len(user) > 0:

        if bcrypt.check_password_hash(user[0]['password'], password):
            session['user_id'] = user[0]['id']
            return render_template('success.html')

        else:
            flash('Email/Password combination does not match')
            return redirect('/')


app.run(debug=True)
