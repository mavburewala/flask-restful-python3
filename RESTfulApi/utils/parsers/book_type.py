#!/usr/bin/env python
# encoding: utf-8

"""
    File name: book_type.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Nadeem <mavburewala@gmail.com>
    
"""
from flask_restful import reqparse


# ------------ book_type add parser ------------
book_type_post_parser = reqparse.RequestParser()
book_type_post_parser.add_argument(
    'name', dest='name',
    type=str, location='form',
    required=True, help='The book_type\'s name',
)
