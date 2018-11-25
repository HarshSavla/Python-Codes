from flask import Flask, render_template, Response, g, current_app as app, make_response
from datetime import datetime
app = Flask(__name__)

import os 
import os.path
import requests

location = []
name = []
retu = "time"
f_location = []
tip = []
key = "jcToDuIv3S3JWlHiPokQ-miqhqDl42juP0vycC7zvEe"

def utctime():
    tim = str(datetime.now())
    return tim 

def remove(location): 
    for a in location: 
        if a not in f_location: 
            f_location.append(a) 
    return f_location  

def email_alert(key, band_id, person_name, location):
    report = {}
    report["value1"] = band_id
    report["value2"] = person_name
    report["value3"] = location
  
    requests.post("https://maker.ifttt.com/trigger/updatesheet/with/key/" + str(key), data=report)  

@app.route('/')
def homepage():

    return render_template('Today.html', location=f_location, name=name, tip=tip)
	
@app.route('/history')
def year():

    return render_template('History.html', location=f_location, name=name)

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
    remove(location)
    email_alert (key,g.bandname,ban,loc)
    tim = list(str(datetime.now()))
    tim[10] = ", "
    tim[16] = ''
    tim[17] = ''
    tim[18] = ''
    tim[19] = ''
    tim[20] = ''
    tim[21] = ''
    tim[22] = ''
    tim[23] = ''
    tim[24] = ''
    tim[25] = ''
    tim = "".join(tim)
    tip.append(tim)
    return tim

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)