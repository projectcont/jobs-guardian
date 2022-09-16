from setting import *
def card_filter(cardlist):
    print("jobtitle_notcontain",jobtitle_notcontain.split(' '))
    result=[]
    for card in cardlist:
        if jobtitle_contain in card.title:
            print('is=', card.title)
            result.append(card)
        else:
            print('not=',card.title)
    return  result
