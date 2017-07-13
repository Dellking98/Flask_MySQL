from flask import Flask, render_template, request, redirect

add = Flask(__name__)

@add.route('/')

def form1():
    return render_template('form_text.html')

@add.route('/User1', methods = ["POST"] )

def create_users1():
    return render_template('/index1.html')

    print "Got Post info"

    Name = request.form["name"]
    select = request.form['list']
    comment = request.form['comment']

    return redirect('/')
add.run(debug = True)
