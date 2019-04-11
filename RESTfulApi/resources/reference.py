#!/usr/bin/env python
# encoding: utf-8

"""
    File name: reference.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Nadeem <mavburewala@gmail.com>
    
"""
from flask_restful import Resource, marshal_with
from RESTfulApi.utils.fields import deleted_fields
from RESTfulApi.utils.parsers import token_parser
from RESTfulApi.utils.fields.book import books_fields
from RESTfulApi.utils.fields.sales_record import sales_records_fields
from RESTfulApi.handler.reference import get_sales_records_by_book, get_sales_records_by_vip
from RESTfulApi.handler.reference import get_books_by_type, rm_ref_book2type, get_sales_records_by_account


class ReferenceBook2Type(Resource):
    @marshal_with(books_fields)
    def get(self, book_type_id):
        token = token_parser.parse_args().token
        books = get_books_by_type(book_type_id, token=token)
        return {'books': books}

    @marshal_with(deleted_fields)
    def delete(self, book_type_id):
        token = token_parser.parse_args().token
        result = rm_ref_book2type(book_type_id, token=token)
        return result


class ReferenceSaleRecord2Account(Resource):
    @marshal_with(sales_records_fields)
    def get(self, account_id):
        token = token_parser.parse_args().token
        sales_records = get_sales_records_by_account(account_id, token=token)
        return {'sales_records': sales_records}


class ReferenceSaleRecord2Book(Resource):
    @marshal_with(sales_records_fields)
    def get(self, book_id):
        token = token_parser.parse_args().token
        sales_records = get_sales_records_by_book(book_id, token=token)
        return {'sales_records': sales_records}


class ReferenceSale2Vip(Resource):
    @marshal_with(sales_records_fields)
    def get(self, vip_id):
        token = token_parser.parse_args().token
        sales_records = get_sales_records_by_vip(vip_id, token=token)
        return {'sales_records': sales_records}

