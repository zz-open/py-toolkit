# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/17 23:28
@Auth ： 仔仔
@File ：ding_robot.py
@Description ：
"""
from abc import ABC, abstractmethod


class DingRobot(ABC):
    @abstractmethod
    def send_msg(self, msg: str = ""):
        pass
