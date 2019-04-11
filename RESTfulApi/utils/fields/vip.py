#!/usr/bin/env python
# encoding: utf-8

"""
    File name: vip.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Nadeem <mavburewala@gmail.com>
    
"""
from flask_restful import fields


vip_fields = {
    'id': fields.String,
    'username': fields.String,
    'nickname': fields.String,
    'phone': fields.String,
}

# for get /vips
vips_fields = {
    'vips': fields.List(fields.Nested(vip_fields))
}
