"""
json工具类
@Author:何同学
"""
import datetime
import json
from array import array


class Json_Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        if isinstance(obj, int):
            return int(obj)
        if isinstance(obj, float):
            return float(obj)
        if isinstance(obj, array):
            return obj.tolist()
        else:
            return super(Json_Encoder, self).default(obj)
