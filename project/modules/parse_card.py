from bs4 import BeautifulSoup
import lxml
from modules.make_request import *
from modules.card import *

def parse_card_(url:str):
    '''
        Parses  jobcard webpage and returns list of  jobcard urls
        :param url:  takes jobcard url (str)
        :return: instance of Card (which contains parsed info about the vacancy)
        '''

    html=make_request_(url)
    soup = BeautifulSoup(html, 'lxml')
    card=Card()
    h1=soup.find('h1').text
    card.title=h1
    attr={}
    attrkeys=list(soup.find_all('dt', class_='mds-list__key'))
    attrvalues=list(soup.find_all('dd', class_='mds-list__value'))
    attrkeys_= [item.text for item in attrkeys]
    attrvalues_ =  [item.text for item in attrvalues]

    if len(attrkeys_)==len(attrvalues_):

        for i in range(0,len(attrkeys)):

            localkey=attrkeys_[i];
            localvalue=attrvalues_[i];
            localvalue=localvalue.replace('\n','')
            localvalue = localvalue.replace('/n', '')
            localvalue = localvalue.strip(' ')

            #print("key=", localkey)
            #print("val=", localvalue )
            attr[localkey]=localvalue
    else:
        print('error')
    card.attr=attr
    card.description = str(soup.find('div', class_='mds-edited-text'))

    card.card_url=url


    return  card










