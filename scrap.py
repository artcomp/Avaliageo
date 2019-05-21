#encoding=utf-8
import json
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import urllib2
import re

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def getNewsLinks(url):
    html_page = urllib2.urlopen(url)
    soup = BeautifulSoup(html_page)


    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        print link.get('href')

def getTitle(url):
	raw_html = simple_get(url)
	html_paragraph =  BeautifulSoup(raw_html, 'html.parser')

	title = html_paragraph.select('title')
	return str(title[0]).split("|")[0].replace("<title>","")

def get_paragraph(url):
	#'https://exame.abril.com.br/economia/os-8-estados-brasileiros-que-devem-superar-o-nivel-pre-crise-em-2019'
	raw_html = simple_get(url)
	html_paragraph =  BeautifulSoup(raw_html, 'html.parser')

	str=""
	for p in html_paragraph.select('p'):
		#print(p.text)
		str= str+p.text+"</p><p>"

	return str


def getJsonReturnListOption(json):
    data = json
    
    list_d = []
    index_to_alpha = 0
    for each in data['geonames']:
        # print each['name'], each['fcode'], each['countryCode']
        iso_state = "/$$$"
        try:
            iso_state = each['adminName1']
            iso_state = '/'+iso_state
        except Exception as e:
            iso_state = "/$$$"
        if len(iso_state) == 0:
            iso_state = "/$$$"
        iso_state = iso_state.replace(' ','---')

        try:
            list_d.append(str(index_to_alpha) + " " + str(each['geonameId']) + " " + each['name'] + " " + each['fcode'] + " " +iso_state+" "+ each['countryCode'])
        except Exception as e:
            list_d.append(str(index_to_alpha) + " " + str(each['geonameId']) + " " + each['name'] + " " + each['fcode'] + " " +iso_state+ " .")
        
        index_to_alpha=index_to_alpha+1

    return list_d


def getJsonAndReturnListOption(json_data):
	data = json.loads(json_data)
	list_data = []
	for each in data['geonames']:
        
		list_data.append(each['name'] + " " + each['fcode'] )
        
	return list_data


def getToponymAndAttachJson(toponimos):

    quantity_results_wanted = '5'
    list_data_to_be_shown = []

    for each in toponimos:
        topoynim_without_spaces = each.replace(' ','+').lower()
        # http://api.geonames.org/searchJSON?formatted=true&q=rio+de+janeiro&maxRows=3&lang=es&username=artdcomp&style=short
        url_search = 'http://api.geonames.org/searchJSON?formatted=true&q='+topoynim_without_spaces+'&maxRows='+quantity_results_wanted+'&lang=pt&username=artdcomp&style=medium'
        json_info = get(url_search).json()
       
        parse_info_to_be_shown = getJsonReturnListOption(json_info)
        list_data_to_be_shown.append(parse_info_to_be_shown)

    return list_data_to_be_shown
















