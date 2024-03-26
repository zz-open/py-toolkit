# -*- coding: utf-8 -*-
"""
@author 仔仔
@date 2024-03-05 23:25:52
@describe 顺丰官网地址智能解析
"""
import json

import requests


def main():
    cookie='' # 请替换成你的cookie
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    headers = {
        "Cookie": cookie,
        "Host": "www.sf-express.com",
        "Content-Type": "application/json",
        "Origin": "https://www.sf-express.com",
        "Referer": "https://www.sf-express.com/chn/sc/address-book?from=page",
        "User-Agent": ua
    }

    address = "北京市天安门 张三 18888888888"
    data = json.dumps({"address": address})
    url = 'https://www.sf-express.com/sf-service-core-web/service/nlp/address/mainlandChina/resolve?lang=sc&region=cn&translate=sc'
    resp = requests.post(url, headers=headers, data=data)
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


if __name__ == "__main__":
    main()
