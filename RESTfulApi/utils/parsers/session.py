#!/usr/bin/env python
# encoding: utf-8

"""
    File name: session.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Nadeem <mavburewala@gmail.com>
    
"""
from flask_restful import reqparse


# ------------ login parser ------------
login_parser = reqparse.RequestParser()
login_parser.add_argument(
    'username', dest='username',
    type=str, location='form',
    required=True, help='This is username',
)

login_parser.add_argument(
    'password', dest='password',
    type=str, location='form',
    required=True, help='This is password',
)
