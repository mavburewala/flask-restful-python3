#!/usr/bin/env python
# encoding: utf-8

"""
    File name: authority.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""

from werkzeug import security

from RESTfulApi.models.token_db import Token
from RESTfulApi.models.shop_db import Account


def create_token(length=16):
    return security.gen_salt(length)


def is_root(token):
    token = Token.objects(token=token).first()
    if token is None:
        return False
    account = Account.objects(id=token.user_id).first()
    if account is None:
        return False
    if account.username == 'root':
        return True
    return False


def is_admin(token):
    token = Token.objects(token=token).first()
    if token is None:
        return False
    account = Account.objects(id=token.user_id).first()
    if account is None:
        return False
    if account.role == 'stuff':
        return False
    return True


def is_stuff(token):
    token = Token.objects(token=token).first()
    if token is None:
        return False
    account = Account.objects(id=token.user_id).first()
    if account is None:
        return False
    return True


def is_self(account_id, token):
    token = Token.objects(token=token).first()
    if token is None:
        return False
    if account_id != token.user_id:
        return False
    return True
