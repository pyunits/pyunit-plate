# !/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/6/17 下午3:27
# @Author: Jtyoui@qq.com
# @Notes : 提取车牌
import re

from .rules import *


def plate_number(number: str):
    """车牌号验证
    :param number: 车牌号
    :return: [{'address': '车属地址', 'plate': '车牌号', 'type': '车牌种类'}]
    """
    ds = []
    translate = number.translate(chinese).upper()
    match = re.finditer(MILITARY_VEHICLES, translate)
    for find in match:
        group = find.group()
        types = '97式军车牌'
        name = MILITARY_KEY[group[0]]
        two = MILITARY_KEY.get(group[1], '')
        address = name + two
        ds.append({'plate': group, 'type': types, 'address': address})

    match = re.finditer(ARMED_POLICE_VEHICLE, translate)
    for find in match:
        group = find.group()
        types = '13式武警车牌'
        province = PROVINCE_KEY[group[2]]
        two = ARMED_POLICE_KEY.get(group[-1], '')
        address = f'{province}武警{two}'
        ds.append({'plate': group, 'type': types, 'address': address})

    match = re.finditer(NEW_MILITARY_VEHICLES, translate)
    for find in match:
        group = find.group()
        types = '新军车牌'
        one = NEW_MILITARY_KEY[group[0]]
        two = ARMED_POLICE_KEY.get(group[:2], '')
        address = f'{one}{two}'
        ds.append({'plate': group, 'type': types, 'address': address})

    match = re.finditer(NEW_ENERGY_VEHICLE_RE + '|' + ORDINARY_CAR_RE, translate)
    for find in match:
        group = find.group()
        types = '民用车牌' if find.lastindex is None else '新能源车牌'
        one = PROVINCE_KEY[group[0]]
        two = ORDINARY_KEY.get(group[:2], '')
        address = f'{one}{two}'
        ds.append({'plate': group, 'type': types, 'address': address})

    match = re.finditer(CIVIL_CAR, translate)
    for find in match:
        group = find.group()
        types = '农用车牌'
        address = CIVIL_CAR_KEY.get(group[:3], '')
        province = PROVINCE_KEY.get(group[0], None)
        if province:
            address = province + address
        ds.append({'plate': group, 'type': types, 'address': address})

    return ds
