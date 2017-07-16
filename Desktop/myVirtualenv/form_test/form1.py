from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key ='secret'
@app.route('/')

def form1():
    return render_template('form_text.html')

@app.route('/User1', methods = ["POST"] )

def create_users1():

    print "Got Post info"

    session['name'] = request.form["name"]

    session['select'] = request.form['list1']

    session['select1'] = request.form['list2']

    session['comment'] = request.form['comment']

    return redirect('/seccess')

@app.route('/seccess')

def seccess():
    return render_template('index1.html')

@app.route('/reset', methods=['POST'])

def reset():
    return redirect('/')

app.run(debug = True)

