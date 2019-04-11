#!/usr/bin/env python
# encoding: utf-8

"""
    File name: common.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Nadeem <mavburewala@gmail.com>
    
"""
from flask_restful import reqparse


token_parser = reqparse.RequestParser()
token_parser.add_argument('token', location='headers', required=True)


