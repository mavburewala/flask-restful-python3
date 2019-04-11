#!/usr/bin/env python
# encoding: utf-8

"""
    File name: account.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Nadeem <mavburewala@gmail.com>
    
"""
from flask_restful import Resource, request, marshal_with

from RESTfulApi.handler.account import get_accounts, get_all_accounts
from RESTfulApi.handler.account import create_account, rm_account, update_account, get_account_by_id

from RESTfulApi.utils.fields import deleted_fields, pt_fields, pt_fields_with_token
from RESTfulApi.utils.fields.account import account_detail_fields, accounts_fields

from RESTfulApi.utils.parsers import token_parser
from RESTfulApi.utils.parsers.account import register_parser, account_update_parser


class Accounts(Resource):
    @marshal_with(accounts_fields)
    def get(self):
        token = token_parser.parse_args().token
        args = request.args
        if args:
            accounts = get_accounts(args, token=token)
        else:
            accounts = get_all_accounts(token=token)
        return {'accounts': accounts}

    @marshal_with(pt_fields_with_token)
    def post(self):
        token = token_parser.parse_args().token
        account_args = register_parser.parse_args()
        result = create_account(
            account_args.username, account_args.password, account_args.confirm, account_args.role,
            account_args.nickname, token=token
        )
        return result


class Account(Resource):
    @marshal_with(account_detail_fields)
    def get(self, account_id):
        token = token_parser.parse_args().token
        return get_account_by_id(account_id, token=token)

    @marshal_with(pt_fields)
    def put(self, account_id):
        token = token_parser.parse_args().token
        account_args = account_update_parser.parse_args()
        result = update_account(account_id, account_args.nickname, account_args.des, account_args.old_password,
                                account_args.new_password, account_args.confirm, token=token)
        return result

    @marshal_with(deleted_fields)
    def delete(self, account_id):
        token = token_parser.parse_args().token
        result = rm_account(account_id, token=token)
        return result