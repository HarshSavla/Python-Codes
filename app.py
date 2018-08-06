from flask import Flask, render_template, Response, g, current_app as app, make_response
from datetime import datetime
app = Flask(__name__)

import os 
import os.path

location = []
name = []
L = [1,2,3,4,5,6,7,8,9]

@app.route('/')
def homepage():

    return render_template('Today.html', location=location, name=name, L=L)

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
    location.append(loc)
    name.append(ban)
    return "OK"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    
