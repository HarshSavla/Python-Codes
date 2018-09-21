from flask import Flask, render_template, Response, g, current_app as app, make_response
from datetime import datetime
app = Flask(__name__)

import os 
import os.path
import requests

c = 0
location = []
name = []
f_location = [] 
key = "jcToDuIv3S3JWlHiPokQ-miqhqDl42juP0vycC7zvEe"

def email_alert(key, band_id, person_name, location):
    report = {}
    report["value1"] = band_id
    report["value2"] = person_name
    report["value3"] = location
  
    requests.post("https://maker.ifttt.com/trigger/updatesheet/with/key/" + str(key), data=report)  

@app.route('/')
def homepage():

    return render_template('Today.html', f_location=location, name=name)
	
@app.route('/history')
def year():

    return render_template('History.html', f_location=location, name=name)

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
    for num in location: 
        if num not in f_location: 
            f_location.append(num) 
    email_alert (key,g.bandname,ban,loc)
    return "OK"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    
