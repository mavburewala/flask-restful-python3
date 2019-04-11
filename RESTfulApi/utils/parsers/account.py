#!/usr/bin/env python
# encoding: utf-8

"""
    File name: account.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Nadeem <mavburewala@gmail.com>
    
"""
from flask_restful import reqparse

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

# ------------ account update parser ------------
account_update_parser = reqparse.RequestParser()

account_update_parser.add_argument(
    'nickname', dest='nickname',
    type=str, location='form',
    required=True, help='This is new nickname',
)

account_update_parser.add_argument(
    'des', dest='des',
    type=str, location='form',
    required=False, help='The user\'s new description',
)

account_update_parser.add_argument(
    'old_password', dest='old_password',
    type=str, location='form',
    required=False, help='This is old password',
)

account_update_parser.add_argument(
    'new_password', dest='new_password',
    type=str, location='form',
    required=False, help='This is new password',
)

account_update_parser.add_argument(
    'confirm', dest='confirm',
    type=str, location='form',
    required=False, help='This is new password\'s confirm',
)
