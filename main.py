from flask import Flask, request
from flask.templating import render_template

import status

app = Flask(__name__)

@app.route('/')
def home_page():
    gsuite = status.get_google()
    gevents = status.get_gsuite()
    zoom = status.get_zoom()
    apple = status.get_apple()
    return render_template('home.html', gsuite=gsuite, zoom=zoom, apple=apple, gevents=gevents)
