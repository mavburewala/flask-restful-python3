#!/usr/bin/env python
# encoding: utf-8

"""
    File name: account.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from flask_restful import fields

# for get /accounts/<account_id>
account_detail_fields = {
    'id': fields.String,
    'username': fields.String,
    'nickname': fields.String,
    'role': fields.String,
    'description': fields.String,
    'created': fields.DateTime,
}

# for get /accounts
account_simple_fields = {
    'id': fields.String,
    'nickname': fields.String,
    'role': fields.String,
}

accounts_fields = {
    'accounts': fields.List(fields.Nested(account_simple_fields))
}
