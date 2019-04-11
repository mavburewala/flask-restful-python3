#!/usr/bin/env python
# encoding: utf-8

"""
    File name: run.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Nadeem <mavburewala@gmail.com>
    
"""

from flask import Flask, g
from RESTfulApi.app import api_bp
from RESTfulApi.models import register_database


def create_app(**config):
    """
    Create and initialize a Flask App
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
