# You're going to create a mini-game that helps a ninja make some
# money! When you start the game, your ninja should have 0 gold.
# The ninja can go to different places (farm, cave, house, casino)
# and earn different amounts of gold. In the case of a casino,
# your ninja can earn or LOSE up to 50 golds. Your job is to
# create a web app that allows this ninja to earn gold and to
# display past activities of this ninja.

# Guidelines
# Refer to the wireframe below.
# Have the four forms appear when the user goes to
# http://localhost:5000.
# For the farm, your form would look something like
# <form action="/process_money" method="post">
#   <input type="hidden" name="building" value="farm" />
#   <input type="submit" value="Find Gold!"/>
# </form>
# In other words include a hidden value in the form and have
# each form submit the form information to /process_money.
# Have /process_money determine how much gold the user should have.
# You should only have 2 routes -- '/' and '/process_money'
# (reset can be another route if you implement this feature).

from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key ='secret'

@app.route('/')

def index():
    return render_template('ninjaWeb.html')

@app.route("/process_money", methods = ["POST"])

def building():
    session['gold'] = 0
    session['activity'] = list()

    if request.form["building"] is 'farm':
        gold = random.randint(10, 20)
        session["gold"] += gold
        activity = "Earned" + str(session["gold"]) + "from the farm"
        session['activity'].append(activity)

    elif request.form["building"] is "cave":
        gold = random.randint(5, 10)
        session['gold'] += gold
        activity = "Earned" + str(session["gold"]) + "from the cave"
        session['activity'].append(activity)

    elif request.form["building"] is "house":
        gold = random.randint(2, 5)
        session['gold'] += gold
        activity = "Earned" + str(session["gold"]) + "from the house"
        session['activity'].append(activity)

    elif request.form["building"] is "casino":
        gold = random.randint(0, 50)
        if gold < 30 :
            session['gold'] += gold
            activity = "Earned" + str(session["gold"]) + "from the casino"
            session['activity'].append(activity)
        else:
            session['gold'] -= gold
            activity = "Lost" + str(session["gold"]) + "from the casino"
            session['activity'].append(activity)
    return redirect('/')

app.run(debug = True)
