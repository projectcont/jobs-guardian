from bs4 import BeautifulSoup
import lxml

class Card:

    '''
    A class to represent the vacancy info (job card)
    '''

    def __init__(self):
        self.card_url: str=''#
        self.card_url_redirected: str = ''#
        self.title: str = '' #
        self.description: str = '' #
        self.citation: str = ''
        self.attr :dict ={}
        self.id: str = ''  #


    def __eq__(self, other):
        return ((self.title == other.title) and (self.title == other.title))

    def __repr__(self):
        str=f'title= {self.title} company={self.attr["Employer"]}'
        return str

    def __str__(self):
        str=f'title= {self.title} company={self.attr["Employer"]}'
        return str


    def produce_citation(self):
        '''
        Produces and returnes citation from job decsriprion. Citation is a small part of job description. It is a surrounding text, which is related to the specific topic
        :return: citation (str)
        '''


        from setting import citation
        if self.description.find(citation) > 0:
        #if self.title=="Data Analyst (Tableau)":

            def get_cit(phrases_list):
                offset = 3
                #print("len phrases_list=",len(phrases_list))
                for n in range(len(phrases_list)):
                    print(n, phrases_list[n-3])
                    if citation in phrases_list[n]:
                        citation_index=n

                        citation_list=phrases_list[citation_index-offset:citation_index+offset]
                        citation_list2= [" ".join(v.split()) for v in citation_list] #removing spaces in each phrase
                        citation_list3 = [ f"{v.strip('.')}." for v in citation_list2 ]
                        citation_text='\n<br/>'.join(citation_list3)  #joining phrases in one html text

                        print(); print('result citation_text=',citation_text); print()


                        return citation_text


            print(self.card_url)
            soup2 = BeautifulSoup(self.description, 'lxml')
            descr_p = list((soup2.find_all('p')))
            descr_p_str = [v.text for v in descr_p]
            #for n in descr_p_str: print('p list=',len(descr_p_str),n)


            #self.description=self.description.replace(';','.')

            descr_text = soup2.text.split('.')
            #for n in descr_text: print('text list=', len(descr_text),n)


            descr_li = list((soup2.find_all('li')))
            descr_li_str = [v.text for v in descr_li]
            #for n in descr_li_str: print('li list=',len(descr_li_str), n)


            if citation in ''.join(descr_p_str):
                self.citation=get_cit (descr_p_str)
            if citation in ''.join(descr_li_str):
                self.citation=get_cit(descr_li_str)
            #if citation in ''.join(descr_text):
                #self.citation=get_cit(descr_text)

        else:
            self.citation=''




    def produce_html (self)-> str:
        '''
        Produces and returnes html-code from jobcard.
        :return: html (str)
        '''

        wrapper_title=f' <h2> {self.title} </h2> '
        url_redir=f'<div><a href = "{self.card_url}" target="_blank"> Job page </a> </div>'
        wrapper_attr=''
        for key, value in self.attr.items():
            if key=='Website':
                wrapper_attr += f'<div class="optionkey"> {key} </div> <div class="optionvalue" style="color:yellow"> <a  href="{value}"> {value} </a></div>'
            else:
                wrapper_attr += f'<div class="optionkey"> {key} </div> <div class="optionvalue"> {value} </div>'

        wrapper_cit = f' <div class="citation"> {self.citation} </div> '

        wrapper=f'<table><tr> <td> <div class="narrow">{wrapper_title} {url_redir} <div class="flexdiv">{wrapper_attr}</div></div> </td> <td><div class="narrow"> <h3>Citation</h3>  <h4>Citation is a small part of job description. It is a surrounding text, which is related to the specific topic </h4>{wrapper_cit} </div></td> </tr></table>'
        return wrapper





















