# Chromote

Simple wrapper to drive Google Chrome from Python using the Remote Debugging Protocol 1.1 API

https://developer.chrome.com/devtools/docs/protocol/1.1/index

## Example

Google Chrome needs to be running with the `-remote-debugging-port` option set:

    $ google-chrome -remote-debugging-port=9222

    $ python
    >>> from chromote import Chromote
    >>> chrome = Chromote()
    >>> chrome
    Chromote(localhost, 9222)
    >>> print chrome
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
