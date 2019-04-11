#!/usr/bin/env python
# encoding: utf-8

"""
    File name: account.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from mongoengine import Q
from flask import abort
from RESTfulApi.models.shop_db import Account
from RESTfulApi.models.token_db import Token
from RESTfulApi.utils.authority import create_token, is_admin, is_root, is_self, is_stuff


def get_accounts(args, token=None):
    if token is None or not is_stuff(token):
        return abort(403)
    if is_admin(token):
        condition = Q(username__ne='root')
    else:
        condition = Q(username__ne='root') & Q(role='stuff')
    if 'username' in args:
        condition &= Q(username=args['username'])
    if 'nickname' in args:
        condition &= Q(nickname=args['nickname'])
    accounts = Account.objects(condition)
    return accounts


def get_all_accounts(token=None):
    if token is None or not is_stuff(token):
        return abort(403)
    if is_admin(token):
        condition = Q(username__ne='root')
    else:
        condition = Q(username__ne='root') & Q(role='stuff')
    accounts = Account.objects(condition)
    return accounts


def create_account(username, password, confirm, role, nickname, token=None):
    if token is None or not is_admin(token):
        return abort(403)

    if password != confirm:
        return {
            "message": "password not conformity"
        }
    if Account.objects(username=username).first() is not None:
        return {
            "message": "username has been register"
        }

    if str(role) == '1':
        role = 'admin'
    else:
        role = 'stuff'
    account = Account(
        username=username,
        nickname=nickname,
        password=Account.create_password(password),
        role=role,
    ).save()
    token = Token(
        user_id=str(account.id),
        token=create_token(),
    ).save()
    return {
        'id': account.id,
        'success': 1,
        'token': token.token
    }


def rm_account(account_id, token=None):
    if token is None or not is_admin(token):
        return abort(403)

    account = Account.objects(id=account_id).first()
    if account is None:
        return {'message': 'this account has been deleted'}
    if account.role == 'admin':
        if not is_root(token):
            return abort(403)
    account.delete()
    return {'success': 1}


def update_account(account_id, nickname, des, old_password, new_password, confirm, token=None):
    if token is None or not (is_admin(token) or is_self(account_id, token)):
        return abort(403)
    account = Account.objects(id=account_id).first()
    if account is None or account.username == 'root':
        return abort(403)
    if des is None:
        des = ""
    password = account.password
    if new_password or confirm:
        if new_password == confirm:
            if Account.check_password(account, old_password):
                password = Account.create_password(new_password)
            else:
                return {
                    'success': 0,
                    'message': 'wrong password'
                }
        else:
            return {
                'success': 0,
                'message': 'pwd != confirm'
            }
    account.update(
        nickname=nickname,
        description=des,
        password=password,
    )
    account.save()
    return {
        'success': 1,
        'id': account_id,
        'message': 'user\'s profile update successfully!'
    }


def get_account_by_id(account_id, token=None):
    if token is None or not is_stuff(token):
        return abort(403)
    condition = Q(id=account_id)
    if is_admin(token) and not is_root(token):
        condition &= Q(username__ne='root')
    elif not is_root(token):
        condition = Q(username__ne='root') & Q(role='stuff')
    account = Account.objects(condition).first()
    return account
