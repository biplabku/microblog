from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Biplab'}
    return render_template('index.html',title='Home', user=user)
