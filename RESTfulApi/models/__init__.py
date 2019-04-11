#!/usr/bin/env python
# encoding: utf-8

"""
    File name: __init__.py.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""


from RESTfulApi.models.shop_db import *
from mongoengine import connect


def register_database(app):
    database = app.config['MONGODB_SETTINGS']['DB']
    connect(database)
