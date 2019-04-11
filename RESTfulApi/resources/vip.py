#!/usr/bin/env python
# encoding: utf-8

"""
    File name: vip.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Nadeem <mavburewala@gmail.com>
    
"""
from flask_restful import Resource, request, marshal_with

from RESTfulApi.handler.vip import get_all_vips, create_vip, get_vips, rm_vip

from RESTfulApi.utils.parsers import token_parser
from RESTfulApi.utils.parsers.vip import vip_post_parser
from RESTfulApi.utils.fields import deleted_fields, pt_fields
from RESTfulApi.utils.fields.vip import vips_fields


class Vips(Resource):
    @marshal_with(vips_fields)
    def get(self):
        token = token_parser.parse_args().token
        args = request.args
        if args:
            vips = get_vips(args, token=token)
        else:
            vips = get_all_vips(token=token)
        return {'vips': vips}

    @marshal_with(pt_fields)
    def post(self):
        token = token_parser.parse_args().token
        vip_args = vip_post_parser.parse_args()
        result = create_vip(vip_args.username, vip_args.nickname, vip_args.phone, token=token)
        return result


class Vip(Resource):
    @marshal_with(deleted_fields)
    def delete(self, vip_id):
        token = token_parser.parse_args().token
        result = rm_vip(vip_id, token=token)
        return result
