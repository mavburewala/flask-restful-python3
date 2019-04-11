#!/usr/bin/env python
# encoding: utf-8

"""
    File name: run.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""

from flask import Flask, g
from RESTfulApi.app import api_bp
from RESTfulApi.models import register_database


def create_app(**config):
    """
    创建并初始化一个 Flask App
    :param
    :return
    """
    app = Flask(__name__)
    register_config(app, config)
    register_database(app)
    register_routes(app)
    return app


def register_config(app, config):
    if config.get('debug') is True:
        app.debug = True

    from config import default
    app.config.from_object(default)


def register_routes(app):
    app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    create_app(debug=True).run()
