from bs4 import BeautifulSoup
from project.setting import *
import lxml

def parse_(html:str):
    '''
    Parses  joblist webpage joblist  and returns list of  jobcard urls
    :param html:  takes html of webpage for joblist (str)
    :return: list of urls for jobcard webpages (list [str])
    '''

    soup = BeautifulSoup(html, 'lxml')
    alist = []
    for h3 in soup.find_all('h3', class_='lister__header'):
        #print(h3)
        alist_ = h3.find_all('a')
        #print(alist)
        alist.extend(alist_)

    hrefs = []
    for n in alist:
        href_ = n.get('href').strip(' ')
        href_= href_.replace("\r","")
        href_= href_.replace("\n", "")
        href_ = f"{BASEURL.strip(' ')}{href_}"
        href_=(''.join(href_.split()))
        print(href_)

        hrefs.append(href_)


    return hrefs

