def test_chromote():
    from chromote import Chromote

    chrome = Chromote()

    tab0 = chrome.tabs[0]

    sites = [
        'https://github.com',
        'http://stackoverflow.com',
    ]

    tab0.set_url(sites[0])
    print(tab0)

    tab1 = chrome.add_tab(sites[1])
    print(tab1)
    chrome.close_tab(tab1)

    tab2 = chrome.add_tab()
    print(tab2)

if __name__ == '__main__':
    test_chromote()