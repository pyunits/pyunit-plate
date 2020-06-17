# !/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/6/17 下午2:50
# @Author: Jtyoui@qq.com
# @Notes :  测试文件
import pprint

from pyunit_plate import plate_number


def plate_number_test():
    p = plate_number('我家的车牌是贵A12345,他家的车牌是语粤B12345D,我家农用车贵0688110,我家爸的车是wj粤8888X')
    pprint.pprint(p)
    """
    [{'address': '广东省武警消防部队', 'plate': 'WJ粤8888X', 'type': '13式武警车牌'},
    {'address': '贵州省贵阳市', 'plate': '贵A12345', 'type': '民用车牌表'},
    {'address': '广东省深圳市', 'plate': '粤B12345D', 'type': '新能源车牌'}]
    """


if __name__ == '__main__':
    plate_number_test()
