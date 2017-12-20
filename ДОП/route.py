from flask import Flask
from flask import url_for, render_template, request, redirect

import json

from uuid import uuid4

app = Flask(__name__)



@app.route('/')
def index():
    ...
    return ...

@app.route('/', methods=['POST'])
def process_request():
    ...
    return ...

@app.route('/translit')
def translit_news():
    ...
    return ...

@app.route('/check')
def check():
    ...
    return ...
