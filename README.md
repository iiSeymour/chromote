# Chromote

Simple wrapper to drive Google Chrome from Python using the Remote Debugging Protocol 1.1 API

https://developer.chrome.com/devtools/docs/protocol/1.1/index

## Example

Run Google Chrome with remote debugging enabled `google-chrome -remote-debugging-port=9222`:

```python
>>> from chromote import Chromote
>>> chrome = Chromote()
>>> chrome
Chromote(host="localhost", port=9222)
>>> print chrome
[Chromote(tabs=1)]
>>> tab = chrome[0]
>>> print tab
Google - https://www.google.co.uk/
>>> tab.reload()
'{"result":{},"id":1}'
>>> tab.set_url('https://github.com/chromote')
'{"id":2,"result":{}}'
>>> tab.evaluate('alert("Remotey");')
```

## Remote Browser Control

The remote debugging port binds to localhost only so using Chromote with a remote
machine like a dashboard/kiosk setup will require tunneling to the machine first.

On the remote machine start Chrome:

    $ chromium-browser <DASHBOARD-URL> --incognito --kiosk -remote-debugging-port=9222

On the local machine set up a tunnel to map the remote debug port to 9222 on localhost:

    $ ssh remote-machine -L 9222:localhost:9222

You than can drive the browsers from a Python script:

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
