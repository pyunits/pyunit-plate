# **PyUnit-Plate** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 基于规则抽取车牌号实体：包括种类、地址、数值。各种各样的车牌信息。
[![](https://img.shields.io/badge/Python-3.7-green.svg)](https://pypi.org/project/pyunit-address/)

## 安装
    pip install pyunit-plate

## 车牌种类
    97式军车牌
    13式武警车牌
    新军车牌照
    民用车牌
    新能源车牌
    农用车牌
  
## 使用
```python
import pprint

from pyunit_plate import plate_number

if __name__ == '__main__':
    p = plate_number('我家的车牌是贵A12345,他家的车牌是粤B12345D,我家农用车贵0688110,我家爸的车是wj粤8888X')
    pprint.pprint(p)
    """
    [{'address': '广东省武警消防部队', 'plate': 'WJ粤8888X', 'type': '13式武警车牌'},
    {'address': '贵州省贵阳市', 'plate': '贵A12345', 'type': '民用车牌'},
    {'address': '广东省深圳市', 'plate': '粤B12345D', 'type': '新能源车牌'},
    {'address': '贵州省毕节', 'plate': '贵0688110', 'type': '农用车牌'}]
    """
```

## 返回参数
```json
[
  {"address": "车牌地址", "plate": "车牌号", "type" : "车牌类型"}
]
```

## Docker部署
    docker pull jtyoui/pyunit-plate
    docker run -d -P pyunit-plate

### 车牌号规则提取
|**参数名**|**类型**|**是否可以为空**|**说明**|
|------|------|-------|--------|
|data|string|YES|输入一句话|

### 请求示例
> #### Python3 Requests测试
```python
import requests

url = "http://127.0.0.1:32768/pyunit/plate"
data = {
    'data': '我家的车牌是贵A12345,他家的车牌是语粤B12345D,我家农用车贵0688110,我家爸的车是wj粤8888X',
}
headers = {'Content-Type': "application/x-www-form-urlencoded"}
response = requests.post(url, data=data, headers=headers).json()
print(response)
``` 

> #### 返回结果
```json
{
    "code": 200,
    "result": [
        {
            "address": "广东省武警消防部队",
            "plate": "WJ粤8888X",
            "type": "13式武警车牌"
        },
        {
            "address": "贵州省贵阳市",
            "plate": "贵A12345",
            "type": "民用车牌"
        },
        {
            "address": "广东省深圳市",
            "plate": "粤B12345D",
            "type": "新能源车牌"
        },
        {
            "address": "贵州省毕节",
            "plate": "贵0688110",
            "type": "农用车牌"
        }
    ]
}
```

***
[1]: https://blog.jtyoui.com