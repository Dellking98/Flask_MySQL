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

# Take the Dojo Survey assignment that you completed previously and add
# validations! The Name and Comment fields should be validated so that
# they are not blank. Also, validate that the comment field is no longer
# than 120 characters.

from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key ='secret'
@app.route('/')

def form1():
    return render_template('form_text.html')

# def errorLog():
#     if len(request.form["name"]) < 1:
#         print "You need to put a name"
#     else:
#         print 'Thank you', request.form["name"]
#     if len(request.form['comment']) < 120:
#         print 'Your oppend matters here, Please tell us in 123 words'
#     else:
#         print "Thank you for your comment"
@app.route('/User1', methods = ["POST"] )

def create_users1():
    session['name'] = request.form["name"]
    if len(session['name']) < 1:
        flash ("You need to put a name")
    else:
        flash ('Thank you', session['name'])

    session['select'] = request.form['list1']

    session['select1'] = request.form['list2']

    session['comment'] = request.form['comment']
    if len(session['comment']) < 120:
        flash ('Your opinion matters here, Please tell us in 123 words')
    else:
        flash ("Thank you for your comment")

    return redirect('/seccess')

@app.route('/seccess')

def seccess():
    return render_template('index1.html')

@app.route('/reset', methods=['POST'])

def reset():
    return redirect('/')


app.run(debug = True)




