#!/usr/bin/env python
# encoding: utf-8

"""
    File name: vip.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Nadeem <mavburewala@gmail.com>
    
"""
from flask_restful import reqparse


# ------------ vip add parser ------------
vip_post_parser = reqparse.RequestParser()
vip_post_parser.add_argument(
    'username', dest='username',
    type=str, location='form',
    required=True, help='The vip\'s username',
)

vip_post_parser.add_argument(
    'nickname', dest='nickname',
    type=str, location='form',
    required=True, help='The vip\'s nickname',
)

vip_post_parser.add_argument(
    'phone', dest='phone',
    type=str, location='form',
    required=False, help='The vip\'s phone',
)
