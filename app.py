from flask import Flask, render_template, g, Response
from datetime import datetime
app = Flask(__name__)
location = ""
bandname = ""
@app.route('/')
def homepage():

    return render_template('Today.html', location = location, bandname = bandname)

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
    bandname = os.environ.get(g.person_id)
    location = os.environ.get(g.device_id)
    return render_template("OK")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    
