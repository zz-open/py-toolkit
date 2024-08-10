# -*- coding: utf-8 -*-
"""
@author 仔仔
@date 2024-03-05 23:25:52
@describe 顺丰官网地址智能解析
"""
import json
import random
import time
import hashlib
import requests


def generate_random_string(length=6):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(letters) for _ in range(length))


def get_sign_dict(data: dict):
    if data is None:
        data = {}
    # 下方计算sign的时候要求body参数是紧凑型的，key: value中间不能有空格
    body = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    print("body:", body)

    app_id = 'sHu1R65iomBa'  # 从官网逆向获取，固定值，跟设备端有关，与app_secret成对出现
    app_secret = "71fa384d863f683f5079aaaab29c45e5"  # 从官网逆向获取，固定值
    timestamp = str(int(time.time() * 1000))  # 当前时间的毫秒时间戳
    nonce = generate_random_string()  # 6位长度随机字符串

    # 按照固定顺序，参与编码
    sign = f"appId={app_id}&appSecret={app_secret}&body={body}&nonce={nonce}&timestamp={timestamp}"

    # 采用MD5算法，日后可能会变
    md5_hash = hashlib.md5()
    md5_hash.update(sign.encode('utf-8'))
    md5_sign = md5_hash.hexdigest()

    res = {
        "nonce": nonce,
        "timestamp": timestamp,
        "sign": md5_sign,  # MD5算法得出
        "app_id": app_id,
        "app_secret": app_secret,
    }

    # sign = 'appId=占位&appSecret=占位&body={"address":"占位"}&nonce=占位&timestamp=占位'
    print('res:', res)
    return res


def nlp_address_resolve(address: str):
    # 全部参数
    cookie = 'i18n_redirected=sc; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221913b2bb4912b60-0ad1d89a549f76-26001e51-2073600-1913b2bb4923986%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%221913b2bb4912b60-0ad1d89a549f76-26001e51-2073600-1913b2bb4923986%22%7D; sajssdk_2015_cross_new_user=1; HWWAFSESID=a523f97f8401baab65; HWWAFSESTIME=1723274638148; OWFSESSION=3b186b7605534d22a43551cb3eaa75e2; loginUser=18810951239; remember-me=ZWIxOTNiYjI1M2QxNDYxYzhiZjI4ZDM1MTg2OTNjNzU6MTcxODJjNmU0YmY0NDQzODhjMjRmZTZhN2VkYjc1ODk=; 1859fdaa-8db4-4197-99e9-067feedf835d=fdb51876a0fccf27449acc7febcd8d94; tgw_l7_route=21578487d8864a4303cdd1694d8e8ed3'  # 请替换成你的cookie
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    data = {"address": address}

    # 直接传入序列化后的参数
    sign_dict = get_sign_dict(data)

    common_headers = {
        "nonce": sign_dict.get('nonce'),
        "timestamp": sign_dict.get('timestamp'),
        "app_id": sign_dict.get('app_id'),
        "sign": sign_dict.get('sign'),
        "cookie": cookie,
        "ua": ua,
    }
    print('common_headers:', common_headers)

    headers = {
        "Cookie": common_headers.get("cookie"),
        "User-Agent": common_headers.get("ua"),
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Host": "www.sf-express.com",
        "Content-Type": "application/json",
        "Origin": "https://www.sf-express.com",
        "Referer": "https://www.sf-express.com/chn/sc/address-book?from=page",
        "ReferrerPolicy": "strict-origin-when-cross-origin",
        "Sec-Ch-Ua": '"Not)A;Brand";v = "99", "Google Chrome";v = "127", "Chromium";v = "127"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "Windows",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "appId": common_headers.get("app_id"),
        "nonce": common_headers.get("nonce"),
        "sign": common_headers.get("sign"),
        "timestamp": common_headers.get("timestamp"),
    }

    url = ('https://www.sf-express.com/sf-service-core-web/service/nlp/address/mainlandChina/resolve?lang=sc&region=cn'
           '&translate=sc')
    # 此处的data参数放在body体中，不能是紧凑型的，key value 冒号后边必须有空格
    resp = requests.post(url, headers=headers, data=json.dumps(data))
    json_data = resp.json()
    print("原始响应:", json_data)
    if json_data.get("code") != 0:
        print("解析失败")
        return

    result = json_data.get("result")[0]
    resolve_data = {
        "name": result.get("name"),
        "mobile": result.get("mobile"),
        "province": result.get("province"),
        "city": result.get("city"),
        "district": result.get("district"),
        "address": result.get("address"),
    }
    print(resolve_data)


def test_get_sign_dict(data):
    app_id = 'sHu1R65iomBa'
    app_secret = "71fa384d863f683f5079aaaab29c45e5"
    timestamp = "1723280613774"
    nonce = "PMmOA1"
    sign = f"appId={app_id}&appSecret={app_secret}&body={data}&nonce={nonce}&timestamp={timestamp}"

    # 采用MD5算法，日后可能会变
    md5_hash = hashlib.md5()
    md5_hash.update(sign.encode('utf-8'))
    md5_sign = md5_hash.hexdigest()

    res = {
        "nonce": nonce,
        "timestamp": timestamp,
        "sign": md5_sign,  # MD5算法得出
        "app_id": app_id,
        "app_secret": app_secret,
    }

    print('res:', res)


def test(address: str):
    data = json.dumps({"address": address}, ensure_ascii=False, separators=(',', ':'))
    test_get_sign_dict(data)


if __name__ == "__main__":
    address = "用户 18888888888 广东省深圳市龙岗区xxx"
    # test(address)
    nlp_address_resolve(address)
