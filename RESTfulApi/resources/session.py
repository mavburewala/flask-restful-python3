#!/usr/bin/env python
# encoding: utf-8

"""
    File name: session.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from flask_restful import Resource, marshal_with

from RESTfulApi.handler.session import login, logout
from RESTfulApi.utils.parsers import token_parser
from RESTfulApi.utils.parsers.session import login_parser
from RESTfulApi.utils.fields import deleted_fields, pt_fields_with_token


class Session(Resource):
    @marshal_with(pt_fields_with_token)
    def post(self):
        login_args = login_parser.parse_args()
        result = login(login_args.username, login_args.password)
        return result

    @marshal_with(deleted_fields)
    def delete(self):
        token = token_parser.parse_args().token
        result = logout(token)
        return result
