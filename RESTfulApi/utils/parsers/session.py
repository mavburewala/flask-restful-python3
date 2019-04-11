#!/usr/bin/env python
# encoding: utf-8

"""
    File name: session.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
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
