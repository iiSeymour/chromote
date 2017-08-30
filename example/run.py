#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example script demostrating the use of Chromote to
update a remote browser periodically from a list of sites
"""

from time import sleep
from chromote import Chromote

chrome = Chromote()
print(chrome)

tab = chrome.tabs[0]

sites = [
    'https://github.com',
    'http://stackoverflow.com',
]

for site in sites:
    tab.set_url(site)
    sleep(30)
