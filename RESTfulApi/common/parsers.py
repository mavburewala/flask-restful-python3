#!/usr/bin/env python
# encoding: utf-8

"""
    File name: parsers.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Nadeem <mavburewala@gmail.com>
    
"""
from flask_restful import reqparse

# ------------ book parser ------------
book_parser = reqparse.RequestParser()
book_parser.add_argument(
    'name', dest='name',
    type=str, location='form',
    required=True, help='The book\'s name',
)

book_parser.add_argument(
    'count', dest='count',
    type=int, location='form',
    required=True, help='The book\'s count',
)

book_parser.add_argument(
    'price', dest='price',
    type=float, location='form',
    required=True, help='The book\'s price',
)

book_parser.add_argument(
    'des', dest='des',
    type=str, location='form',
    required=False, help='The book\'s description',
)

# ------------ book_update parser ------------
book_update_parser = reqparse.RequestParser()
book_update_parser.add_argument(
    'delta', dest='delta',
    type=int, location='form',
    required=True, help='The book\'s deviation',
)

book_update_parser.add_argument(
    'price', dest='price',
    type=float, location='form',
    required=True, help='The book\'s new price',
)

book_update_parser.add_argument(
    'des', dest='des',
    type=str, location='form',
    required=False, help='The book\'s new description',
)

book_update_parser.add_argument(
    'type_id', dest='types_id', action='append',
    type=str, location='form',
    required=True, help='The book\'s new list of type id',
)


# ------------ book_type parser ------------
book_type_parser = reqparse.RequestParser()
book_type_parser.add_argument(
    'name', dest='name',
    type=str, location='form',
    required=True, help='The book_type\'s name',
)


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

# ------------ logout parser ------------
token_parser = reqparse.RequestParser()
token_parser.add_argument('token', location='headers', required=True)

# ------------ register parser ------------
register_parser = reqparse.RequestParser()
register_parser.add_argument(
    'username', dest='username',
    type=str, location='form',
    required=True, help='This is username',
)

register_parser.add_argument(
    'nickname', dest='nickname',
    type=str, location='form',
    required=True, help='This is nickname',
)

register_parser.add_argument(
    'password', dest='password',
    type=str, location='form',
    required=True, help='This is password',
)

register_parser.add_argument(
    'confirm', dest='confirm',
    type=str, location='form',
    required=True, help='This is password\'s confirm',
)
register_parser.add_argument(
    'role', dest='role',
    type=int, location='form',
    required=True, help='This is user\'s role',
)

# ------------ register parser ------------
account_update_parser = reqparse.RequestParser()

account_update_parser.add_argument(
    'nickname', dest='nickname',
    type=str, location='form',
    required=True, help='This is new nickname',
)

book_update_parser.add_argument(
    'des', dest='des',
    type=str, location='form',
    required=False, help='The account description',
)

# ------------ vip parser ------------
vip_parser = reqparse.RequestParser()
vip_parser.add_argument(
    'username', dest='username',
    type=str, location='form',
    required=True, help='The vip\'s username',
)

vip_parser.add_argument(
    'nickname', dest='nickname',
    type=str, location='form',
    required=True, help='The vip\'s nickname',
)

vip_parser.add_argument(
    'phone', dest='phone',
    type=str, location='form',
    required=False, help='The vip\'s phone',
)

# ------------ sales record parser ------------
sales_record_parser = reqparse.RequestParser()
sales_record_parser.add_argument(
    'count', dest='count',
    type=int, location='form',
    required=True, help='The sales\'s count',
)

sales_record_parser.add_argument(
    'seller_id', dest='seller_id',
    type=str, location='form',
    required=True, help='The sales\'s seller id',
)

sales_record_parser.add_argument(
    'book_id', dest='book_id',
    type=str, location='form',
    required=True, help='The sales\'s book id',
)

sales_record_parser.add_argument(
    'purchaser_id', dest='purchaser_id',
    type=str, location='form',
    required=False, help='The sales\'s purchaser id',
)
