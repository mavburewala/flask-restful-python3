#!/usr/bin/env python
# encoding: utf-8

"""
    File name: book.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from flask import abort
from mongoengine import Q, ValidationError
from RESTfulApi.models.shop_db import Book, Type
from RESTfulApi.utils.authority import is_admin, is_stuff


def get_all_books(token=None):
    if token is None or not is_stuff(token):
        return abort(403)
    books = Book.objects()
    return books


def create_book(name, price, count, description, token=None):
    if token is None or not is_admin(token):
        return abort(403)
    if Book.objects(name=name).first() is not None:
        return {
            'message': 'this book has been existed'
        }
    book = Book(
        name=name,
        price=price,
        remaining=count,
        description=description,
    )
    book = book.save()
    return {
        'success': 1,
        'id': book.id
    }


def get_book_by_id(book_id, token=None):
    if token is None or not is_stuff(token):
        return abort(403)
    book = Book.objects(id=book_id).first()
    return book


def get_books(args, token=None):
    if token is None or not is_stuff(token):
        return abort(403)
    condition = None
    if 'id' in args:
        condition = Q(id=args['id'])
    if 'name' in args:
        if condition is None:
            condition = Q(name=args['name'])
        else:
            condition &= Q(name=args['name'])
    books = Book.objects(condition)
    return books


def rm_book(book_id, token=None):
    if token is None or not is_admin(token):
        return abort(403)
    book = Book.objects(id=book_id)
    book.delete()
    return {'success': 1}


def update_book(book_id, delta, price, des, type_id_list, token=None):
    if token is None or not is_admin(token):
        return abort(403)
    book = Book.objects(id=book_id).first()
    if book is None:
        return {'message': 'This book does not exist.'}
    remaining = book.remaining
    if des is None:
        des = ""
    book.update(
        price=price,
        remaining=remaining+delta,
        description=des,
    )
    del book.type[:]
    if type_id_list is not None:
        for i in type_id_list:
            try:
                term = Type.objects(id=i).first()
            except ValidationError:
                continue
            if term is None:
                continue
            book.type.append(term)
    book.save()
    return {
        'success': 1,
        'id': book_id,
    }
