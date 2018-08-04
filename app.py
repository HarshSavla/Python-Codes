from flask import Flask, render_template, Response, g, current_app as app, make_response
from datetime import datetime
app = Flask(__name__)

import os 
import os.path

location = []
bandname = []
L = [1, 2, 3, 4, 5, 6, 7]

@app.route('/month')
def month():

    return render_template('This Month.html')
	
@app.route('/year')
def year():

    return render_template('This Year.html')

@app.route('/register')
def register():

    return render_template('Register.html')

@app.route('/<device_id>/<person_id>')
def trackPerson(device_id, person_id):
    g.location = device_id
    g.bandname = person_id
    loc = os.environ.get(g.location)
    ban = os.environ.get(g.bandname)
    location.append([loc])
    bandname.append([ban])

    return "OK"

length = len(location) - 1

@app.route('/')
def homepage():

    return render_template('Today.html', location=location, bandname=bandname, length = length, L=l)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    
