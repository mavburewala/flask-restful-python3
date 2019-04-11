#!/usr/bin/env python
# encoding: utf-8

"""
    File name: session.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from RESTfulApi.models.shop_db import Account
from RESTfulApi.models.token_db import Token
from RESTfulApi.utils.authority import create_token


def login(username, password):
    account = Account.objects(username=username).first()
    if account is None:
        return {'message': 'this account does not exist'}
    if Account.check_password(account, password):
        new_token = create_token()
        token = Token.objects(user_id=str(account.id)).first()
        if token is None:
            Token(user_id=str(account.id), token=new_token).save()
        else:
            token.update(token=new_token)
        return {
            'id': account.id,
            'success': 1,
            'token': new_token
        }
    else:
        return {
            'message': 'password is wrong.'
        }


def logout(token):
    token = Token.objects(token=token).first()
    token.delete()
    return {'success': 1}
