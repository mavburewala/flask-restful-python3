#!/usr/bin/env python
# encoding: utf-8

"""
    File name: shop_db.py
    Function Des: MongoDB数据库映射
    ~~~~~~~~~~

    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>

"""

from datetime import datetime
from mongoengine import *
from werkzeug import security
from flask import current_app


__all__ = ['Type', 'Book', 'SalesRecord', 'Vip', 'Account']


class Vip(Document):
    username = StringField(required=True, max_length=5, unique=True)
    nickname = StringField(required=True, max_length=40)
    phone = StringField(max_length=15)
    register_time = DateTimeField(default=datetime.today)


class Type(Document):
    name = StringField(required=True, unique=True)


class Book(Document):
    name = StringField(required=True, max_length=40, unique=True)
    price = FloatField(required=True)
    sales = IntField(default=0)
    remaining = IntField(required=True)
    description = StringField(default='', max_length=400)
    type = ListField(ReferenceField(Type, reverse_delete_rule=DENY))


class Account(Document):
    username = StringField(required=True, max_length=10, unique=True)
    password = StringField(required=True, max_length=100)
    nickname = StringField(required=True, max_length=10)
    role = StringField(max_length=10, default='stuff')
    description = StringField(default='', max_length=400)

    created = DateTimeField(default=datetime.today)

    @staticmethod
    def create_password(raw):
        pwd = '{old}{new}'.format(old=raw, new=current_app.config['PASSWORD_SECRET'])
        return security.generate_password_hash(pwd)

    @staticmethod
    def is_admin(self):
        return self.role == 'admin'

    @staticmethod
    def check_password(user, raw):
        pwd = '{old}{new}'.format(old=raw, new=current_app.config['PASSWORD_SECRET'])
        return security.check_password_hash(user.password, pwd)


class SalesRecord(Document):
    seller = ReferenceField(Account, required=True)
    book = ReferenceField(Book, required=True)
    price = FloatField(required=True)
    count = IntField(default=1)
    sale_time = DateTimeField(default=datetime.today)
    purchaser = ReferenceField(Vip, required=False)

