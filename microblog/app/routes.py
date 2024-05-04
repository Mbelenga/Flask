from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Terrence'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
