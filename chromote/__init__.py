# -*- coding: utf-8 -*-

"""
Chromote

Python wrapper for Google Chrome Remote Debugging Protocol 1.2

https://chromedevtools.github.io/devtools-protocol/1-2
"""


import json
from base64 import b64decode

import requests
import websocket
from requests.exceptions import ConnectionError


version = "0.4.0"
__version__ = version
__all__ = ['Chromote', 'ChromeTab']


class ChromeTab(object):

    def __init__(self, id, title, url, websocketURL):
        self.id = id
        self._title = title
        self._url = url
        self._websocketURL = websocketURL
        self._message_id = 0

    def _send(self, request):
        self._message_id += 1
        request['id'] = self._message_id
        ws = websocket.create_connection(self.websocketURL)
        ws.send(json.dumps(request))
        res = ws.recv()
        ws.close()
        return res

    @property
    def title(self):
        return self._title

    @property
    def url(self):
        return self._url

    @property
    def websocketURL(self):
        return self._websocketURL

    @property
    def html(self):
        result = json.loads(self.evaluate('document.documentElement.outerHTML'))
        value = result['result']['result']['value']
        return value.encode('utf-8')

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

    def set_zoom(self, scale):
        """
        Set the page zoom
        """
        return self.evaluate("document.body.style.zoom={}".format(scale))

    def evaluate(self, javascript):
        """
        Evaluate JavaScript on the page
        """
        return self._send({"method": "Runtime.evaluate", "params": {"expression": javascript}})

    def screenshot(self, format='png', quality=85, fromSurface=False):
        """
        Take a screenshot of the page
        """
        args = {
            "method": "Page.captureScreenshot",
            "params": {
                "format":      format,
                "quality":     quality,
                "fromSurface": fromSurface
            }
        }
        result = self._send(args)
        data = json.loads(result)
        if 'error' in data:
            raise ValueError(data['error']['data'])
        return b64decode(data.get('result', {}).get('data', ''))

    def __str__(self):
        return '%s - %s' % (self.title, self.url)

    def __repr__(self):
        return 'ChromeTab("%s" "%s", "%s", "%s")' % (self.id, self.title, self.url, self.websocketURL)


class Chromote(object):

    def __init__(self, host='localhost', port=9222):
        self._host = host
        self._port = port
        self._url = 'http://%s:%d' % (self.host, self.port)
        self._errmsg = "Connect error! Is Chrome running with -remote-debugging-port=%d" % self.port
        self._connect()

    def _connect(self):
        """
        Test connection to browser
        """
        try:
            requests.get(self.url)
        except ConnectionError:
            raise ConnectionError(self._errmsg)

    def _get_tabs(self):
        """
        Get all open browser tabs that are pages tabs
        """
        res = requests.get(self.url + '/json')
        for tab in res.json():
            if tab['type'] == 'page':
                yield ChromeTab(tab['id'], tab['title'], tab['url'], tab['webSocketDebuggerUrl'])

    def add_tab(self, url=None):
        tab = requests.get(self.url + '/json/new').json()
        if url is not None:
            ChromeTab(tab['id'], tab['title'], tab['url'], tab['webSocketDebuggerUrl']).set_url(url)
            tab = requests.get(self.url + '/json').json()[0]

        return ChromeTab(tab['id'], tab['title'], tab['url'], tab['webSocketDebuggerUrl'])

    def activate_tab(self, tab):
        requests.get('{}/json/activate/{}'.format(self.url, tab.id))

    def close_tab(self, tab):
        requests.get('{}/json/close/{}'.format(self.url, tab.id))

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def url(self):
        return self._url

    @property
    def tabs(self):
        return tuple(self._get_tabs())

    def __len__(self):
        return len(self.tabs)

    def __str__(self):
        return '[Chromote(tabs=%d)]' % len(self)

    def __repr__(self):
        return 'Chromote(host="%s", port=%s)' % (self.host, self.port)

    def __getitem__(self, i):
        return self.tabs[i]

    def __iter__(self):
        return iter(self.tabs)
