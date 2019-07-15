#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-07-13
# Extented Ping

import sys
import urllib.parse
import platform
import os

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: python3 {sys.argv[0]} URL')
        sys.exit(0)

    url_target = sys.argv[1].lower()
    if not url_target.startswith('http') and not url_target.startswith('https'):
        url_target = f'http://{url_target}'

    host = urllib.parse.urlparse(url_target).netloc
    if ':'in host:
        host = host.split(':')[0]
    else:
        pass
    ping_count = u'-c 4'

    if platform.system() != 'Windows':
        os.system(f'ping {host} {ping_count}')
    else:
        os.system(f'ping {host}')
