# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/17 22:57
@Auth ： 仔仔
@File ：sign.py
@Description ：
"""
import requests
import json
import time
import hmac
import hashlib
import base64
import urllib.parse


def ding_robot_request_url() -> str:
    secret = r'SECe613d7d424917da2e90502956e031ce0f4e1d3e718ebfd7b0db546ea32c9b92e'
    access_token = r'e574e4e6dc86e4de760be6ac4ea5c26a85cd1e4021a4a62c623048ea6ec4b1d9'
    sign_result = ding_robot_sign(secret)
    url = rf'https://oapi.dingtalk.com/robot/send?access_token={access_token}&timestamp={sign_result[0]}&sign={sign_result[1]}'
    return url


def ding_robot_sign(secret: str = "") -> (str, str):
    if secret == "":
        raise Exception("secret 必填")

    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return timestamp, sign


def ding_robot_send_msg(msg: str = "") -> bool:
    if msg == "":
        return True

    url = ding_robot_request_url()
    headers = {
        'Content-Type': 'application/json'
    }

    data = {
        "msgtype": "text",
        "text": {
            "content": msg
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    print("response:", response.text)
    res = json.loads(response.text)
    if res['errcode'] == 0:
        return True

    return False
