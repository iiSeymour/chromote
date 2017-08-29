# Chromote

Simple wrapper to drive Google Chrome from Python using the [Remote Debugging Protocol 1.2 API](https://chromedevtools.github.io/devtools-protocol/1-2)

## Installation

    $ sudo pip3 install git+https://github.com/marshygeek/chromote

## API

```python
>>> from chromote import Chromote
>>> chrome = Chromote()
>>> chrome
Chromote(host="localhost", port=9222)
>>> print chrome
[Chromote(tabs=1)]
>>> tab = chrome.tabs[0]
>>> print tab
Google - https://www.google.co.uk/
>>> print tab.url
https://www.google.co.uk/
>>> tab.reload()
'{"result":{},"id":1}'
>>> tab.set_url('https://github.com/chromote')
'{"id":2,"result":{}}'
>>> tab.set_zoom(1.2)
'{"id":1,"result":{"result":{"type":"number","value":1.2,"description":"1.2"},"wasThrown":false}}'
>>> tab.evaluate('alert("Remotey");')
```

Note: Google Chrome needs starting with the `--remote-debugging-port=<PORT>` option to be controlled remotely.

## Remote Browser Control

The remote debugging port binds to localhost only so using chromote with a remote
machine like a dashboard/kiosk setup will require tunneling to the machine first.

On the remote machine start Google Chrome:

    $ chromium-browser <URL> --incognito --kiosk --remote-debugging-port=9222

On the local machine set up a tunnel to map the remote debugging port to 9222 on localhost:

    $ ssh remote-machine -L 9222:localhost:9222

You can then drive your dashboard/kiosk machine remotely to display the content you want.

```python
from time import sleep
from chromote import Chromote

chrome = Chromote()
tab = chrome.tabs[0]

sites = [
    'https://github.com',
    'http://stackoverflow.com',
]

while True:
    for site in sites:
        tab.set_url(site)
        sleep(30)
```

## License

MIT Copyright (c) 2016 Chris Seymour
