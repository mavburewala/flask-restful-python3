#!/usr/bin/env python
# encoding: utf-8

"""
    File name: book_type.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from flask import abort
from mongoengine import Q, OperationError
from RESTfulApi.models.shop_db import Type
from RESTfulApi.utils.authority import is_admin, is_stuff


def get_all_types(token=None):
    if token is None or not is_stuff(token):
        return abort(403)
    types = Type.objects()
    return types


def create_book_type(name, token=None):
    if token is None or not is_stuff(token):
        return abort(403)
    if Type.objects(name=name).first() is not None:
        return {'message': 'This type has been exist'}
    book_type = Type(name=name).save()
    return {
        'id': book_type.id,
        'success': 1,
    }


def get_book_types(args, token=None):
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
    types = Type.objects(condition)
    return types


def rm_book_type(book_type_id, token=None):
    if token is None or not is_admin(token):
        return abort(403)
    book_type = Type.objects(id=book_type_id)
    try:
        book_type.delete()
    except OperationError:
        return {
            "message": "please dereference before delete the type."
        }
    else:
        return {'success': 1}
