# from flask import Flask, render_template, request, redirect, session
#
# app = Flask(__name__)
# app.secret_key ='secret'
# @app.route('/')
#
#
# def counter():
#     try:
#         session['time'] += 1
#     except KeyError:
#         session['time'] =1
#
#     return render_template('counter_web.html', time = session['time'])
#
# @app.route('/reset', methods =["POST"])
#
# def counterReset():
#
#     session.clear()
#
#     return redirect('/')
#
#
# app.run(debug = True)

eight = 2 ** 3
print eight
