# !/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time  : 2020/5/7 上午11:27
# @Author: Jtyoui@qq.com
# @Notes :  flask 启动
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

from pyunit_plate import plate_number, __names__

app = Flask(__name__)


def flask_content_type(requests):
    """根据不同的content_type来解析数据"""
    if requests.method == 'POST':
        if 'application/x-www-form-urlencoded' == requests.content_type:
            data = requests.form
        else:  # 无法被解析出来的数据
            raise Exception('POST的Content-Type必须是:application/x-www-form-urlencoded')
    elif requests.method == 'GET':
        data = requests.args
    else:
        raise Exception('只支持GET和POST请求')
    return data


@app.route('/', methods=['GET'])
def hello():
    return jsonify(code=200, result='welcome to ' + __names__)


@app.route('/pyunit/plate', methods=['POST', 'GET'])
def supplement():
    try:
        data = flask_content_type(request)
        word = data['data']
        find = plate_number(word)
        return jsonify(code=200, result=find)
    except HTTPException:
        return jsonify(code=500, error='解析参数错误')
    except Exception as e:
        return jsonify(code=400, error=str(e))


if __name__ == '__main__':
    app.run(port=5000)
