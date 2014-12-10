#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from chromote import Chromote

chrome = Chromote()
print chrome

for tab in chrome:
    tab.set_url('https://www.github.com')
    sleep(1)
    tab.evalute('document.title = "Chromoted"')
