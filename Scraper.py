#for any given webpage, the user has the option of finding all URL/Hyperlinks // the top 3 words that appear on webpage // eventually map out the webserver and all its links
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re


#takes HTML, parses through and returns all anchor tags
def parse_url(url):
    html = urllib.request.urlopen(url).read() #opens URL
    sifter = BeautifulSoup(html, 'html.parser') #sifts and return one large string
    tags = sifter('a', None) #extracts all anchor tags
    return tags

#takes all anchor tags, captures URLs and returns total list of URL
def cycle_links(anchor_list):
    all_urls = []
    for tag in anchor_list:
        #gets HTML tag as string
        x = tag.get('href', None)
        all_urls.append(x)
    return all_urls

#passes a keyword,
def keyword_parser(keyword):
    html = urllib.request.urlopen(url).read()
    sifter = BeautifulSoup(html, 'html.parser')
    return sifter


url = input('Enter URL: ')
choice = input('Search for URL, keyword, or map? ').lower()


#decision tree: URL
if choice == 'url':
    anchor_list = parse_url(url)
    total_url = cycle_links(anchor_list)
    print(total_url)

#decision tree: KEYWORD
elif choice == 'keyword':
    keyword = input('Enter keyword: ').lower()
    top_words = keyword_parser(keyword)
    print(top_words)

#decision tree: WORD LIST
elif choice == 'map':


print(parsed_link)
