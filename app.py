from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():

    return render_template('Today.html')

@app.route('/contact')
def contact():

    return render_template('This Month.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    
