#!/usr/bin/env python
# encoding: utf-8

"""
    File name: fields.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Nadeem <mavburewala@gmail.com>
    
"""
from flask_restful import fields


# ------------ book ------------
types_fields = {
    'id': fields.String,
    'name': fields.String,
}

book_fields = {
    'id': fields.String,
    'name': fields.String,
    'price': fields.Float,
    'remaining': fields.Integer,
    'description': fields.String,
    'sales': fields.Integer,
    'type': fields.List(fields.Nested(types_fields)),
}

books_fields = {
    'books': fields.List(fields.Nested(book_fields))
}

# ------------ book type ------------
book_type_fields = {
    'id': fields.String,
    'name': fields.String,
}

book_types_fields = {
    'books_types': fields.List(fields.Nested(book_type_fields))
}


# ------------ account ------------
token_fields = {
    'token': fields.String,
    'message': fields.String,
}

account_fields = {
    'id': fields.String,
    'username': fields.String,
    'nickname': fields.String,
    'role': fields.String,
    'description': fields.String,
    'created': fields.DateTime,
}

accounts_fields = {
    'accounts': fields.List(fields.Nested(account_fields))
}


# ------------ vip ------------
vip_fields = {
    'id': fields.String,
    'username': fields.String,
    'nickname': fields.Float,
    'phone': fields.String,
}

vips_fields = {
    'vips': fields.List(fields.Nested(vip_fields))
}

# ------------ sale_record ------------
sales_record_fields = {
    'id': fields.String,
    'seller': fields.List(fields.Nested(account_fields)),
    'book': fields.List(fields.Nested(book_fields)),
    'count': fields.Integer,
    'sale_time': fields.DateTime,
    'price': fields.Float,
    'purchaser': fields.List(fields.Nested(vip_fields)),
    'message': fields.String,
}

sales_records_fields = {
    'sales_records': fields.List(fields.Nested(sales_record_fields))
}
