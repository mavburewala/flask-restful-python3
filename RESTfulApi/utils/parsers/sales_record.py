#!/usr/bin/env python
# encoding: utf-8

"""
    File name: sales_record.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from flask_restful import reqparse

# ------------ sales record add parser ------------
sales_record_post_parser = reqparse.RequestParser()
sales_record_post_parser.add_argument(
    'count', dest='count',
    type=int, location='form',
    required=True, help='The sales\'s count',
)

sales_record_post_parser.add_argument(
    'seller_id', dest='seller_id',
    type=str, location='form',
    required=True, help='The sales\'s seller id',
)

sales_record_post_parser.add_argument(
    'book_id', dest='book_id',
    type=str, location='form',
    required=True, help='The sales\'s book id',
)

sales_record_post_parser.add_argument(
    'purchaser_id', dest='purchaser_id',
    type=str, location='form',
    required=False, help='The sales\'s purchaser id',
)
