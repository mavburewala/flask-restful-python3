#!/usr/bin/env python
# encoding: utf-8

"""
    File name: reference.py
    Function Des: ...
    ~~~~~~~~~~

    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>

"""
from flask import abort
from RESTfulApi.models.shop_db import Type, Book, Account, Vip, SalesRecord
from RESTfulApi.utils.authority import is_admin, is_stuff


def get_books_by_type(type_id, token=None):
    if token is None or not is_stuff(token):
        return abort(403)
    the_type = Type.objects(id=type_id).first()
    books = Book.objects(type__in=[the_type])
    return books


def rm_ref_book2type(type_id, token=None):
    if token is None or not is_admin(token):
        return abort(403)
    the_type = Type.objects(id=type_id).first()
    all_books = Book.objects()
    for book in all_books:
        if the_type in book.type:
            book.type.remove(the_type)
        book.save()
    return {'success': 1}


def get_sales_records_by_account(account_id, token=None):
    if token is None or not is_stuff(token):
        return abort(403)
    account = Account.objects(id=account_id).first()
    sales_records = SalesRecord.objects(seller=account)
    return sales_records


def get_sales_records_by_book(book_id, token=None):
    if token is None or not is_stuff(token):
        return abort(403)
    book = Book.objects(id=book_id).first()
    sales_records = SalesRecord.objects(book=book)
    return sales_records


def get_sales_records_by_vip(vip_id, token=None):
    if token is None or not is_stuff(token):
        return abort(403)
    vip = Vip.objects(id=vip_id).first()
    sales_records = SalesRecord.objects(purchaser=vip)
    return sales_records

