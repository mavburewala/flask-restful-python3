#!/usr/bin/env python
# encoding: utf-8

"""
    File name: app.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""

from flask import Blueprint
from flask_restful import Api

from RESTfulApi.resources.session import Session

from RESTfulApi.resources.account import Accounts, Account

from RESTfulApi.resources.book import Books, Book

from RESTfulApi.resources.vip import Vips, Vip

from RESTfulApi.resources.book_type import BookTypes, BookType

from RESTfulApi.resources.sales_record import SalesRecords

from RESTfulApi.resources.reference import ReferenceBook2Type, ReferenceSaleRecord2Account
from RESTfulApi.resources.reference import ReferenceSaleRecord2Book, ReferenceSale2Vip

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Session, '/session')

api.add_resource(Accounts, '/accounts')
api.add_resource(Account, '/accounts/<account_id>')

api.add_resource(Books, '/books')
api.add_resource(Book, '/books/<book_id>')

api.add_resource(Vips, '/vips')
api.add_resource(Vip, '/vips/<vip_id>')

api.add_resource(BookTypes, '/types')
api.add_resource(BookType, '/types/<book_type_id>')

api.add_resource(SalesRecords, '/sales_records')

api.add_resource(ReferenceBook2Type, '/references/book2type/<book_type_id>')
api.add_resource(ReferenceSaleRecord2Account, '/references/record2account/<account_id>')
api.add_resource(ReferenceSaleRecord2Book, '/references/record2book/<book_id>')
api.add_resource(ReferenceSale2Vip, '/references/record2vip/<vip_id>')
