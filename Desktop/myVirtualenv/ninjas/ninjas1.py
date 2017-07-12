from flask import Flask, render_template

add = Flask (__name__)

@add.route('/ninjas')

def ninjas():
    return render_template('ninjasinfo.html')
add.run(debug = True)
