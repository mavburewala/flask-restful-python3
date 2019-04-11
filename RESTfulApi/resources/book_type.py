#!/usr/bin/env python
# encoding: utf-8

"""
    File name: book_type.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""

from flask_restful import Resource, request, marshal_with

from RESTfulApi.handler.book_type import get_all_types, create_book_type, get_book_types, rm_book_type

from RESTfulApi.utils.parsers import token_parser
from RESTfulApi.utils.parsers.book_type import book_type_post_parser

from RESTfulApi.utils.fields import pt_fields, deleted_fields
from RESTfulApi.utils.fields.book_type import book_types_fields


class BookTypes(Resource):
    @marshal_with(book_types_fields)
    def get(self):
        token = token_parser.parse_args().token
        args = request.args
        if args:
            books_types = get_book_types(args, token=token)
        else:
            books_types = get_all_types(token=token)
        return {'books_types': books_types}

    @marshal_with(pt_fields)
    def post(self):
        token = token_parser.parse_args().token
        book_args = book_type_post_parser.parse_args()
        result = create_book_type(book_args.name, token=token)
        return result


class BookType(Resource):
    @marshal_with(deleted_fields)
    def delete(self, book_type_id):
        token = token_parser.parse_args().token
        result = rm_book_type(book_type_id, token=token)
        return result
