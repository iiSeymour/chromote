# -*- coding: utf-8 -*-

"""
Chromote

Python wrapper for Google Chrome Remote Debugging Protocol 1.1

https://developer.chrome.com/devtools/docs/protocol/1.1/index
"""

import json
import requests
import websocket
from requests.exceptions import ConnectionError

version = 0.1
__version__ = version
__all__ = ['Chromote', 'ChromeTab']


class ChromeTab(object):

    def __init__(self, title, url, websocketURL):
        self.title = title
        self.url = url
        self.websocketURL = websocketURL
        self.message_id = 0

    def _send(self, request):
        self.message_id += 1
        request['id'] = self.message_id
        ws = websocket.create_connection(self.websocketURL)
        ws.send(json.dumps(request))
        res = ws.recv()
        ws.close()
        return res

    def reload(self):
        """
        Reload the page
        """
        return self._send({"method": "Page.reload"})

    def set_url(self, url):
        """
        Navigate the tab to the URL
        """
        return self._send({"method": "Page.navigate", "params": {"url": url}})

    def evalute(self, javascript):
        """
        Evaluate JavaScript on the page
        """
        return self._send({"method": "Runtime.evaluate", "params": {"expression": javascript}})

    def __str__(self):
        return '%s - %s' % (self.title, self.url)

    def __repr__(self):
        return 'ChromeTab(%s, %s, %s)' % (self.title, self.url, self.websocketURL)


class Chromote(object):

    def __init__(self, host='localhost', port=9222):
        self.host = host
        self.port = port
        self.url = 'http://%s:%d' % (self.host, self.port)
        self.errmsg = "Connect error! Is Chrome running with -remote-debugging-port=%d" % self.port
        self._connect()
        self.tabs = self._get_tabs()

    def _connect(self):
        """
        Test connection to browser
        """
        try:
            requests.get(self.url)
        except ConnectionError:
            raise ConnectionError(self.errmsg)

    def _get_tabs(self):
        """
        Get browser tabs
        """
        res = requests.get(self.url + '/json')
        tabs = []
        for tab in res.json():
            if tab['type'] == 'page':
                tabs.append(ChromeTab(tab['title'], tab['url'], tab['webSocketDebuggerUrl']))

        return tabs

    def __len__(self):
        return len(self.tabs)

    def __str__(self):
        return '[Chromote(tabs=%d)]' % len(self)

    def __repr__(self):
        return 'Chromote(%s, %s)' % (self.host, self.port)

    def __getitem__(self, i):
        return self.tabs[i]

    def __iter__(self):
        return iter(self.tabs)
