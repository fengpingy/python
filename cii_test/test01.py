# -*- coding:utf-8 -*-
# !/usr/bin/env python3
import requests
url = "https://www.371zhongyi.com/common/"
respones = requests.get(url)
print(respones.text)
print(respones.cookies)


