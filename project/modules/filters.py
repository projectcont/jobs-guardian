from setting import jobtitle_notcontain, jobdescr_notcontain

def filters_(card_list):
    '''
    Takes the list of Cards  (jobcard:Card )
    and filters them by conditions, specified in setting.py
    param card_list: list of Cards
    return: list of Cards (filtered)
    For example, it excludes cards which contain phrases in jobtitle_notcontain jobdescr_notcontain
    '''

    card_list_filtered=[]
    print("jobtitle  not contain= ", jobtitle_notcontain)
    print("jobdescription not contain= ", jobdescr_notcontain)
    excluded=0
    included = 0
    for card in  card_list:
        exclude=0
        for n in jobdescr_notcontain.split(','):
            if n in card.description: exclude = 1

        for n in jobtitle_notcontain.split(','):
            if n in card.title:
                exclude = 1

        if exclude==0:
            card_list_filtered.append(card);
            included += 1;
        else:
            excluded+=1; #print("excluded= ",card.title)

    print(f" {excluded} vacancies excluded")
    print(f" {included} vacancies left")
    return card_list_filtered
