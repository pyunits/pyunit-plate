# !/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/6/17 下午3:25
# @Author: Jtyoui@qq.com
# @Notes :  车牌规则信息
import os

DIRS = os.path.dirname(__file__)
chinese = {
    ord('一'): '1',
    ord('二'): '2',
    ord('三'): '3',
    ord('四'): '4',
    ord('五'): '5',
    ord('六'): '6',
    ord('七'): '7',
    ord('八'): '8',
    ord('九'): '9',
    ord('幺'): '1',
    ord('拐'): '7',
    ord('洞'): '0',
    ord('两'): '2',
    ord('勾'): '9'
}

# 97式军车牌格式
MILITARY_VEHICLES = r'[甲乙丙己庚壬壬寅辰午未申][A-Z]\d{5}'
MILITARY_KEY = {
    '甲': '解放军总部',
    '乙': '集团军',
    '丙': '通信和运输',
    '己': '沈阳军区',
    '庚': '北京军区',
    '辛': '兰州军区',
    '壬': '济南军区',
    '寅': '南京军区',
    '辰': '成都军区',
    '戌': '广州军区',
    '午': '空军',
    '未': '海军',
    '申': '总装备部',
    'A': '司令部',
    'B': '政治部',
    'C': '后勤部',
    'D': '装备部',
    'G': '省军区',
    'H': '仓库',
    'K': '驻当地铁路',
    'P': '医院及医卫院校',
    'S': '后勤工厂'
}

# 13式武警车牌
ARMED_POLICE_VEHICLE = r'WJ[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼]\d{4}[XBTSGJD]'
ARMED_POLICE_KEY = {
    'X': '消防部队',
    'B': '边防部队',
    'T': '交通部队',
    'S': '森林部队',
    'G': '黄金部队',
    'J': '警卫部队',
    'D': '水电部队'
}

# 新军车牌照
NEW_MILITARY_VEHICLES = r'[ABCGNJLSHK][A-Z]\d{5}'
NEW_MILITARY_KEY = {
    'A': '军委四总部以及大区级军直单位',
    'K': '空军',
    'H': '海军',
    'B': '北京军区',
    'S': '沈阳军区',
    'L': '兰州军区',
    'J': '济南军区',
    'N': '南京军区',
    'G': '广州军区',
    'C': '成都军区',
    'AA': '军委总参',
    'AB': '总政治部',
    'AC': '总后勤部',
    'AD': '总装备部',
    'AE': '军事科学院',
    'AF': '国防大学',
    'AG': '国防科技大学',
    'AT': '总参三部',
    'AV': '第二炮兵司令部',
    'KA': '司令部',
    'KB': '空防部',
    'KC': '后勤部',
    'KD': '装备部',
    'KE': '军车监理',
    'KF': '北京军区',
    'KK': '成都军区',
    'KU': '南京军区',
    'HA': '司令部',
    'HB': '政治部',
    'HC': '后勤部',
    'HD': '装备部',
    'HE': '北海舰队',
    'HF': '东海舰队',
    'HG': '南海舰队',
    'HL': '东海舰队航空兵部',
    'HO': '军事监理',
    'HR': '军事院校',
}

# 民用车牌
ORDINARY_CAR_RE = '[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领][A-Z][A-HJ-NP-Z0-9]{4}[A-HJ-NP-Z0-9挂学警港澳]'
ORDINARY_KEY = eval(open(os.path.join(DIRS, '民用车牌.json')).read())

# 新能源车牌
NEW_ENERGY_VEHICLE_RE = '[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领][A-Z](([0-9]{5}[DF])|([DF][A-HJ-NP-Z0-9][0-9]{4}))'
# 车牌省简称
PROVINCE_KEY = {'京': '北京市',
                '津': '天津市',
                '沪': '上海市',
                '渝': '重庆市',
                '宁': '宁夏回族自治区',
                '新': '新疆维吾尔自治区',
                '藏': '西藏自治区',
                '桂': '广西壮族自治区',
                '蒙': '内蒙古自治区',
                '辽': '辽宁省',
                '吉': '吉林省',
                '黑': '黑龙江省',
                '冀': '河北省',
                '晋': '山西省',
                '苏': '江苏省',
                '浙': '浙江省',
                '皖': '安徽省',
                '闽': '福建省',
                '赣': '江西省',
                '鲁': '山东省',
                '豫': '河南省',
                '鄂': '湖北省',
                '湘': '湖南省',
                '粤': '广东省',
                '琼': '海南省',
                '川': '四川省',
                '贵': '贵州省',
                '云': '云南省',
                '陕': '陕西省',
                '甘': '甘肃省',
                '青': '青海省'}

# 农用车牌
CIVIL_CAR_ONE = r'[鄂甘赣渝津苏京豫黑冀琼云吉沪鲁闽贵蒙晋湘浙皖粤桂青新藏川宁陕辽][0-5][0-9]\d{5}'
CIVIL_CAR_TWO = r'(湖北|云南|北京|甘肃|黑龙江|吉林|重庆|湖南|广东|辽宁|河北|宁夏|山东|四川|西藏|新疆|江西|陕西|江苏|上海|天津|内蒙古|海南|山西|福建|广西|青海|贵州|河南|浙江|安徽)[A-Z]\d{5}'
CIVIL_CAR = CIVIL_CAR_ONE + '|' + CIVIL_CAR_TWO
CIVIL_CAR_KEY = eval(open(os.path.join(DIRS, '农用车牌.json')).read())