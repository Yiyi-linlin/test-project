#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time  : 2019/03/27 15:25
# @Author  : Yiyilinlin
# @Software: PyCharm

# regex-exercise

import re


def is_valid_email(addr):
    if re.match(r'[0-9a-zA-Z\_\.]+@[0-9a-zA-Z\_]+\.com', addr):
        return True


# 测试
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
