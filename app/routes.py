from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Biplab'}
    return '''
<html>
    <head>
        <title> Home Page -  Microblog </title>
    </head>
    <body>
        <h1> hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
