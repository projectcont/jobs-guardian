from setting import *
import webbrowser
import os

def result_webpage_(card_list):
    '''
    takes list of cards (type Card)
    for each card produces part of result html-page
    then put them together and produces html page, saving it in file  :
    :param card_list:
    :return:None
    '''
    str1 = '''<!doctype html><head>
            <meta name="title" content=" Scrapper of jobs.theguardian.com " />
    	    <meta name="metatitle" content="Scrapper of jobs.theguardian.com" />
    	    <meta name="description" content="Scrapper of jobs.theguardian.com" />
    	    <meta name="generator" content=" " />
    	    <title>Scrapper of jobs.theguardian.com</title>
            <link rel="stylesheet"  href="style.css"   />
            </head>
            <body > <div class="center" >
            '''
    str2 = ''' </div>   </body ></html>'''

    options=f'<h1> Program perform search vacancies  over jobs.theguardian.com </h1> <h3>Chosen options: (they are set in setting.py)</h3><p>Query phrase = "{query_phrase}" </p>'
    if query_joblevel:
        options+=f'<p>Joblevel = {" ; ".join(query_joblevel)}</p>'
    if query_hours:
        options+=f'<p>Hours = {" ; ".join(query_hours)}</p>'
    if  query_workplace:
        options += f'<p>Workplace = {" ; ".join(query_workplace)}</p>'
    if  query_type:
        options += f'<p>Type = {" ; ".join(query_type)}</p>'

    options += f'<p>Job title not contains = {jobtitle_notcontain}</p>'
    options += f'<p>Job description not contains = {jobdescr_notcontain}</p>'

    wrapper=''
    for card in card_list:
        wrapper=wrapper+card.produce_html()

    html=str1+options+wrapper+str2


    with open('result/file.html', 'w', encoding='utf-8') as file:
        file.write(html)

        webbrowser.open(os.getcwd() + '/result/file.html'.replace('/', '\\'))
        print(os.getcwd()+'/result/file.html'.replace('/', '\\'))
        print('html produced')




