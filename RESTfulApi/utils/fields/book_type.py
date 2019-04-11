#!/usr/bin/env python
# encoding: utf-8

"""
    File name: book_type.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Nadeem <mavburewala@gmail.com>
    
"""
from flask_restful import fields

book_type_fields = {
    'id': fields.String,
    'name': fields.String,
}

# for get /types
book_types_fields = {
    'books_types': fields.List(fields.Nested(book_type_fields))
}
