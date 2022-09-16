from modules.parse import *
from modules.make_request import *

def get_cardurls_ (url:str)-> list[str]:
    '''
    argument is full query url
    (example https://jobs.theguardian.com/searchjobs/?ListingType=101917&keywords=python&countrycode=GB&Page=2)
    function parses  webpage and returns a list of jobcard urls (which are listed on the webpage )
    '''

    try:
        html=make_request_(url)
        return  parse_(html)
    except ConnectionError as e:  # This is the correct syntax
        print (e)
        return []
    except Exception as e:
        print (e)
        return []











