from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():

    return render_template('Today.html')

@app.route('/month')
def month():

    return render_template('This Month.html')
	
@app.route('/year')
def month():

    return render_template('This Year.html')

@app.route('/register')
def month():

    return render_template('Register.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    
