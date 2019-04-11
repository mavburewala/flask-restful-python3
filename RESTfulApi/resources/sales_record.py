#!/usr/bin/env python
# encoding: utf-8

"""
    File name: sales_record.py
    Function Des: ...
    ~~~~~~~~~~

    author: Nadeem <mavburewala@gmail.com>

"""
from flask_restful import Resource, marshal_with

from RESTfulApi.handler.sales_record import get_all_sales_records, create_sales_record
from RESTfulApi.utils.parsers import token_parser
from RESTfulApi.utils.parsers.sales_record import sales_record_post_parser
from RESTfulApi.utils.fields import pt_fields
from RESTfulApi.utils.fields.sales_record import sales_records_fields


class SalesRecords(Resource):
    @marshal_with(sales_records_fields)
    def get(self):
        token = token_parser.parse_args().token
        sales_records = get_all_sales_records(token=token)
        return {'sales_records': sales_records}

    @marshal_with(pt_fields)
    def post(self):
        token = token_parser.parse_args().token
        sales_args = sales_record_post_parser.parse_args()
        result = create_sales_record(sales_args.count, sales_args.seller_id,
                                     sales_args.book_id, sales_args.purchaser_id, token=token)
        return result
