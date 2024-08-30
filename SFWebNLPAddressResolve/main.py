# -*- coding: utf-8 -*-
"""
@author 仔仔
@date 2024-03-05 23:25:52
@describe 顺丰官网地址智能解析api
"""
import requests

from sign import *


def nlp_address_resolve(params: dict):
    if params is None:
        params = {}

    body = params.get('body', {})
    headers = {
        "Cookie": params.get("cookie"),
        "User-Agent": params.get("ua"),
        "appId": params.get("app_id"),
        "nonce": params.get("nonce"),
        "sign": params.get("sign"),
        "timestamp": params.get("timestamp"),
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
    }

    url = ('https://www.sf-express.com/sf-service-core-web/service/nlp/address/mainlandChina/resolve?lang=sc&region=cn'
           '&translate=sc')
    # 此处的data参数放在body体中，不能是紧凑型的，key value 冒号后边必须有空格
    resp = requests.post(url, headers=headers, data=json.dumps(body))
    json_data = resp.json()
    print('原始响应:', json_data)
    if json_data.get("code") != 0:
        print('解析失败')
        return

    result = json_data.get("result")[0]
    resolve_data = {
        'name': result.get('name'),
        'mobile': result.get('mobile'),
        'province': result.get('province'),
        'city': result.get('city'),
        'district': result.get('district'),
        'address': result.get('address'),
    }
    print('响应结果:', resolve_data)


if __name__ == "__main__":
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    # 替换成自己的cookie
    cookie = 'i18n_redirected=sc; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221913b2bb4912b60-0ad1d89a549f76-26001e51-2073600-1913b2bb4923986%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%221913b2bb4912b60-0ad1d89a549f76-26001e51-2073600-1913b2bb4923986%22%7D; sajssdk_2015_cross_new_user=1; HWWAFSESID=a523f97f8401baab65; HWWAFSESTIME=1723274638148; OWFSESSION=3b186b7605534d22a43551cb3eaa75e2; loginUser=18810951239; remember-me=ZWIxOTNiYjI1M2QxNDYxYzhiZjI4ZDM1MTg2OTNjNzU6MTcxODJjNmU0YmY0NDQzODhjMjRmZTZhN2VkYjc1ODk=; 1859fdaa-8db4-4197-99e9-067feedf835d=fdb51876a0fccf27449acc7febcd8d94; tgw_l7_route=21578487d8864a4303cdd1694d8e8ed3'

    body = {'address': '用户 18888888888 广东省深圳市龙岗区xxx'}
    sign_dict = get_sign_dict(body)

    fn_params = {**sign_dict, 'cookie': cookie, 'ua': ua, 'body': body}
    print('fn_params:', fn_params)
    nlp_address_resolve(fn_params)
