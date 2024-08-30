# -*- coding: utf-8 -*-
import hashlib
import json


def test_get_sign_dict(body: str):
    app_id = 'sHu1R65iomBa'
    app_secret = "71fa384d863f683f5079aaaab29c45e5"
    timestamp = "1723280613774"
    nonce = 'PMmOA1'
    sign = f'appId={app_id}&appSecret={app_secret}&body={body}&nonce={nonce}&timestamp={timestamp}'

    # 采用MD5算法，日后可能会变
    md5_hash = hashlib.md5()
    md5_hash.update(sign.encode('utf-8'))
    md5_sign = md5_hash.hexdigest()

    res = {
        'nonce': nonce,
        'timestamp': timestamp,
        'sign': md5_sign,  # MD5算法得出
        'app_id': app_id,
        'app_secret': app_secret,
    }

    print('res:', res)


if __name__ == "__main__":
    address = '用户 18888888888 广东省深圳市龙岗区xxx'
    param = json.dumps({"address": address}, ensure_ascii=False, separators=(',', ':'))
    test_get_sign_dict(param)
