from modules.form_query import  *
from modules.get_cardurls import  *
from modules.parse_card import  *
from modules.result_webpage import *
from modules.filters import  *

def go():
    print('root folder=', os.getcwd())

    card_urls_full = []
    for page in range(1, 4):
        query_url = form_query_url(page)
        print('page= ', page)
        print('query_url=', query_url)
        cardurls=(get_cardurls_(query_url))
        card_urls_full.extend(cardurls)

    card_list=[]
    for url in card_urls_full:
        print('card_url=', url)
        card=parse_card_(url)
        card_list.append(card)

    print('Number of vacancies = ',len(card_list))

    for card in card_list:
        #card.produce_citation()
        print('card_url= ', card.card_url)

    print("len_card_list=",len(card_list))
    for n in card_list: print(n)

    for card in card_list:
        card.produce_citation()
    card_list_filtered = filters_(card_list)
    result_webpage_(card_list_filtered)

    '''
    with open('structure\cards_pickle.txt', 'wb') as file:
        pickle.dump(card_list, file)
        print('cards_pickle.txt dumped')
    '''




















#https://python.hotexamples.com/ru/examples/jsonpickle.pickler/Pickler/-/python-pickler-class-examples.html
''' 


https://www.eurotechjobs.com/job_search/keyword/python
'''






