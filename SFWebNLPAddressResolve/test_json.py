# -*- coding: utf-8 -*-
import json


def test_json(address: str):
    compact_data = json.dumps({"address": address}, ensure_ascii=False, separators=(',', ':'))
    print("紧凑型:", compact_data)

    pine_data = json.dumps({"address": address}, ensure_ascii=False)
    print("非紧凑型:", pine_data)


if __name__ == "__main__":
    addr = '用户 18888888888 广东省深圳市龙岗区xxx'
    test_json(addr)
