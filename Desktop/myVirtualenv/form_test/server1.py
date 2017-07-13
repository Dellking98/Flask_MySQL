from flask import Flask, render_template, request, redirect
add = Flask(__name__)
@add.route('/')

def index():
    return render_template('index1.html')

@add.route('/users', methods =["POST"])

def create_users():
    print "Got Post info"

    name = request.form['name']
    email = request.form['email']
    return redirect('/')
add.run(debug = True)
