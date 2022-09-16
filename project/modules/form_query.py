from project.setting  import *
import sys

def form_query_url (page:int) -> str:
    '''
    arg page is  page number in vacancies listing :param
    function returns full query url (basing on options шт setting.py file)
    example of returns url string:
    https://jobs.theguardian.com/searchjobs/?ListingType=101917&keywords=python&countrycode=GB&Page=2
    '''

    joblevel = {
                'Apprenticeship': '600353',
               'Entry level': '22',
               'Graduate': '18',
               'Junior': '6496751',
               'Experienced (non manager)': '19',
               'Management': '20',
               'Senior management': '6496753',
               'Senior executive': '21',
               'Board / Trustee': '6496755',
    }

    hours = {
        'not chosen': '0',
        'Flexible' : '6496726',
        'Full time' : '29',
        'Full time or Part time' : '6496728',
        'Part time': '30',
    }

    workplace = {
                'No remote option': '6496781',
                'Part-remote option': '6496782',
                'Fully remote option': '6496783',
    }

    type = {
        'Job vacancy': '101917',
        'Graduate scheme': '101920',
        'Internship': '101921',
        'Course': '101919',

    }

    def formoption (opt_list,opt_dict, option  ):
        line=[]

        for str_ in opt_list:
            try:
                line.append(option+opt_dict[str_])
            except KeyError:
                print('Error in setting options')
                sys.exit()
        line=''.join(line);
        # print('line=',line)

        return  line


    str_phrase = 'keywords=' + '+'.join(query_phrase.split());
    # print  ( str_phrase  )

    str_hours = formoption (query_hours,hours,'&Hours=')
    # print  ( str_hours  )

    str_workplace = formoption(query_workplace, workplace, '&Workplace=')
    # print(str_workplace)

    str_joblevel = formoption(query_joblevel, joblevel, '&JobLevel=')
    # print(str_joblevel)

    str_type = formoption(query_type, type, '&ListingType=')
    # print(str_type)


    url_query_ = f'{str_hours}&{str_phrase}&countrycode=GB&Page={page}{str_workplace}{str_joblevel}{str_type}'
    lq=list(url_query_)
    if  lq[0]=='&' : lq=lq[1:]
    url_query_=''.join(lq)

    url_query = f'{BASEURL}/searchjobs/?{url_query_}'
    #str_typeprint(url_query)

    return url_query


