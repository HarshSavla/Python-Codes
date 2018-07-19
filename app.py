from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():

    return render_template('navbar.html')

@app.route('/contact')
def contact():

    return "cont num; 1234, EMILID;fere"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    
