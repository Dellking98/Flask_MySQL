from flask import Flask, render_template
add = Flask(__name__)


@add.route('/dojo')

def dojoNew():
     return render_template('dojos_action.html', words = "What's the world?!?")
add.run(debug = True)
