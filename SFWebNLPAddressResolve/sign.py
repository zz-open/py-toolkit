# -*- coding: utf-8 -*-

import json
import random
import time
import hashlib


def get_common_params():
    return {
        'app_id': 'sHu1R65iomBa',  # 从官网逆向获取，固定值，跟设备端有关，与app_secret成对出现
        'app_secret': '71fa384d863f683f5079aaaab29c45e5',  # 从官网逆向获取，固定值
    }


def generate_random_string(length=6):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(letters) for _ in range(length))


def get_sign_dict(body: dict):
    if body is None:
        body = {}
    # 下方计算sign的时候要求body json是紧凑型的，key: value中间不能有空格
    body_json = json.dumps(body, ensure_ascii=False, separators=(',', ':'))
    print('body_json:', body_json)

    common_params = get_common_params()
    app_id = common_params.get('app_id')
    app_secret = common_params.get('app_secret')
    timestamp = str(int(time.time() * 1000))  # 当前时间的毫秒时间戳
    nonce = generate_random_string()  # 6位长度随机字符串

    # 按照固定顺序，参与编码
    sign = f'appId={app_id}&appSecret={app_secret}&body={body_json}&nonce={nonce}&timestamp={timestamp}'

    # 采用MD5算法，日后可能会变
    md5_hash = hashlib.md5()
    md5_hash.update(sign.encode('utf-8'))
    md5_sign = md5_hash.hexdigest()

    res = {
        'nonce': nonce,
        'timestamp': timestamp,
        'sign': md5_sign,  # MD5算法得出
        'app_id': app_id
    }

    # 结果: sign = 'appId=占位&appSecret=占位&body={"address":"占位"}&nonce=占位&timestamp=占位'
    print('加密相关参数:', res)
    return res
