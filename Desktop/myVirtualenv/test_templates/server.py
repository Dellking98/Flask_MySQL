from flask import Flask, render_template
add = Flask (__name__)

@add.route("/style")

def index():
    return render_template("style.html")
add.run(debug = True)
