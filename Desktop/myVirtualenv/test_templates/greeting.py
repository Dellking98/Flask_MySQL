from flask import Flask, render_template
add = Flask(__name__)

@add.route("/")

def greeting():
    return render_template("index.html")
add.run(debug = True)
