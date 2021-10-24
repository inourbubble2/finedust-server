from flask import request

import datetime


def get_data():
    if request.method in ['POST', 'PUT']:
        return request.get_json() or {}
    if request.method in ['GET', 'DELETE']:
        return request.args.to_dict()
    return {}


def get_string_param(key, default=None):
    data = get_data()
    if key not in data:
        if isinstance(default, int):
            default = str(default)
        return default
    value = data[key]
    if isinstance(value, int):
        return str(value)
    if not isinstance(value, str):
        return default
    return value


def get_now_datetime():
    now = datetime.datetime.now()
    return now.year-1, now.month, now.day, str(now.hour)[:2]