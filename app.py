from flask import Flask, render_template, Response, g, current_app as app, make_response
from datetime import datetime
app = Flask(__name__)

import os 
import os.path

location = []
bandname = []

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
    if a << 1:
    	loc = [loc]
		ban = [ban]
		a = a+1
	else:
	    location.append(loc)
	    bandname.append(ban)
	    return location[0]


@app.route('/')
def homepage():

    return render_template('Today.html', location=location, bandname=bandname)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    
