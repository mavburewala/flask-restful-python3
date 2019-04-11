#!/usr/bin/env python
# encoding: utf-8

"""
    File name: sales_record.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from flask_restful import fields
from RESTfulApi.utils.fields.account import account_simple_fields
from RESTfulApi.utils.fields.book import book_simple_fields
from RESTfulApi.utils.fields.vip import vip_fields

sales_record_fields = {
    'id': fields.String,
    'seller': fields.Nested(account_simple_fields),
    'book': fields.Nested(book_simple_fields),
    'price': fields.Float,
    'count': fields.Integer,
    'sale_time': fields.DateTime,
    'purchaser': fields.Nested(vip_fields),
}

# from get /sales_records
sales_records_fields = {
    'sales_records': fields.List(fields.Nested(sales_record_fields))
}
