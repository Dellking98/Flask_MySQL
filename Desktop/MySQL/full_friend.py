from flask import Flask, request, redirect, render_template, session, flash
from flask import Flask
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'Full_friend')
# an example of running a query
print mysql.query_db("SELECT * FROM friends")

@app.route('/')

def friendForm():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template("fullFriendWeb.html", all_friends = friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email']
           }
    mysql.query_db(query, data)
    return redirect('/')


@app.route('/friends/<friends_id>/delete', methods=['POST'])
def delete(friends_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friends_id}
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<friends_id>/edit')
def edit(friends_id):
    query = "SELECT * FROM friends WHERE id = :id"
    data = {
        'id': friends_id
    }
    results = mysql.query_db(query, data)
    return render_template('editPage.html', friends = results)

@app.route('/friends/<friends_id>', methods = ['POST'])

def update(friends_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email'],
             'id': friends_id
           }
    mysql.query_db(query, data)
    return redirect('/')



app.run(debug=True)
