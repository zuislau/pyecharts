# coding=utf-8
from __future__ import unicode_literals

import codecs
import datetime
import os
import json


def get_resource_dir(*paths):
    """

    :param path:
    :return:
    """
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, *paths)
    return resource_path


def write_utf8_html_file(file_name, html_content):
    """

    :param file_name:
    :param html_content:
    :return:
    """
    with codecs.open(file_name, 'w+', encoding='utf8') as f:
        f.write(html_content)


class UnknownTypeEncoder(json.JSONEncoder):
    """
    UnknownTypeEncoder`类用于处理数据的编码，使其能够被正常的序列化
    """

    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        else:
            # Pandas and Numpy lists
            try:
                return obj.astype(float).tolist()
            except Exception:
                try:
                    return obj.astype(str).tolist()
                except Exception:
                    return json.JSONEncoder.default(self, obj)


def json_dumps(data, indent=0):
    """ json 序列化编码处理

    :param data: 字典数据
    :param indent: 缩进量
    """
    return json.dumps(data, indent=indent, cls=UnknownTypeEncoder)
