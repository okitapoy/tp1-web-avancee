#/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask import render_template
from flask import make_response
from flask import g
from flask import request
from flask import redirect
from flask import Response
#from .database import Database
#import uuid

app = Flask(__name__)



@app.route('/')
def page_acceuil():
    return ("page acceuil")


