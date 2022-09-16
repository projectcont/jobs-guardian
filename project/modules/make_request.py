import requests
def make_request_ (url:str) ->str :
    '''
    make a request on url (str argument)
    and returns html of webpage  (str)
    if error -  returns 0
    '''

    headers = {"Accept": "*/*",
               "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
               "upgrade-insecure-requests": "1",
               }
    try:
        # print('req.headers      = ', req.headers)
        # print('url      = ', url)
        # print('url_redir= ', req.url)
        # print('status_code= ',req.status_code)
        # print('req_text= ', req.text)

        req=requests.get(url,headers=headers)
        if req.status_code < 400:
            return req.text
        else:
            return 0

    except ConnectionError as e:  # This is the correct syntax
        print("ConnectionError")
        print (e)
        return 0
    except Exception as e:
        print("AccessError")
        print (e)
        return 0