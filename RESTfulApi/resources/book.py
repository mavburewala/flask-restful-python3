#!/usr/bin/env python
# encoding: utf-8

"""
    File name: book.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Nadeem <mavburewala@gmail.com>
    
"""
from flask_restful import Resource, request, marshal_with

from RESTfulApi.handler.book import get_all_books, create_book
from RESTfulApi.handler.book import get_book_by_id, get_books, rm_book, update_book

from RESTfulApi.utils.fields import deleted_fields, pt_fields
from RESTfulApi.utils.fields.book import book_detail_fields, books_fields

from RESTfulApi.utils.parsers import token_parser
from RESTfulApi.utils.parsers.book import book_post_parser, book_put_parser


class Books(Resource):
    @marshal_with(books_fields)
    def get(self):
        token = token_parser.parse_args().token
        args = request.args
        if args:
            books = get_books(args, token=token)
        else:
            books = get_all_books(token=token)
        return {'books': books}

    @marshal_with(pt_fields)
    def post(self):
        token = token_parser.parse_args().token
        book_args = book_post_parser.parse_args()
        result = create_book(book_args.name, book_args.price, book_args.count, book_args.des, token=token)
        return result


class Book(Resource):
    @marshal_with(book_detail_fields)
    def get(self, book_id):
        token = token_parser.parse_args().token
        return get_book_by_id(book_id, token=token)

    @marshal_with(pt_fields)
    def put(self, book_id):
        token = token_parser.parse_args().token
        book_args = book_put_parser.parse_args()
        result = update_book(book_id, book_args.delta, book_args.price, book_args.des, book_args.type_ids, token=token)
        return result

    @marshal_with(deleted_fields)
    def delete(self, book_id):
        token = token_parser.parse_args().token
        result = rm_book(book_id, token=token)
        return result
