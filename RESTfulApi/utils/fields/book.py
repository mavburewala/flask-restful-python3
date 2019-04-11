#!/usr/bin/env python
# encoding: utf-8

"""
    File name: book.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from flask_restful import fields

from RESTfulApi.utils.fields.book_type import book_type_fields

# for get /books/<book_id>
book_detail_fields = {
    'id': fields.String,
    'name': fields.String,
    'price': fields.Float,
    'remaining': fields.Integer,
    'description': fields.String,
    'sales': fields.Integer,
    'type': fields.List(fields.Nested(book_type_fields)),
}

# for get /books

book_simple_fields = {
    'id': fields.String,
    'name': fields.String,
    'price': fields.Float,
    'sales': fields.Integer,
}

books_fields = {
    'books': fields.List(fields.Nested(book_simple_fields))
}

