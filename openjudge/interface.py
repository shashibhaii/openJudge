import bottle
from openjudge import tools, config

app = bottle.Bottle()


@app.get('/')
def home():
    return tools.render('home.html')


@app.get('/static/<path:path>')
def static_server(path):
    root = config.static_root
    return bottle.static_file(path, root=root)