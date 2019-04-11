#!/usr/bin/env python
# encoding: utf-8

"""
    File name: init.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from mongoengine import connect
from werkzeug import security
from RESTfulApi.models.shop_db import Account
from RESTfulApi.models.token_db import Token
from RESTfulApi.utils.authority import create_token


connect('library')


def create_password(raw):
    pwd = '{old}{new}'.format(old=raw, new='secret_for_ensure_password_security')
    return security.generate_password_hash(pwd)


# 因代码需要，用户名必须为root
def create_root(username='root', password='password', role='admin', nickname='Super'):
    account = Account(
        username=username,
        nickname=nickname,
        password=create_password(password),
        role=role,
    ).save()
    token = Token(
        user_id=str(account.id),
        token=create_token(),
    ).save()
    return token.token

if __name__ == '__main__':
    print create_root()

