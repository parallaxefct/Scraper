#connect to given webpage // scrape for all URL links
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

#provide url // assign entire string to varible // parse string via BeautifulSoup // returns anchor to TAGS
def parse_url(url):
    html = urllib.request.urlopen(url).read()
    sifter = BeautifulSoup(html, 'html.parser')
    #sifter pulls html anchors and assigns to 'tags' varibale
    tags = sifter('a', None)
    return tags
#passes anchor_tags and position // iterates through list and captures url at position and returns
def cycle_links(anchor_tags):
    for tag in anchor_tags:
        #gets HTML tag as string
        x = tag.get('href', None)
        position -= 1
    return x


def keyword_parser(keyword):
    html = urllib.request.urlopen(url).read()
    sifter = BeautifulSoup(html, 'html.parser')
    return sifter


url = input('Enter URL: ')
choice = input('Search for URL, keyword, or word list? ').lower()


#decision tree: URL
if choice == 'url':
    anchor_list = parse_url(url)
    total_url = cycle_links(anchor_list)
    print(total_url)

#decision tree: KEYWORD
elif choice == 'keyword':
    keyword = input('Enter keyword: ').lower()

#decision tree: WORD LIST
elif choice == 'word list':


#count = int(input('Enter count: '))
#position = int(input('Enter position: '))


#pass url through and recieve anchor list
anchor_tags = parse_url(url)
#cycle through links based on VALUE of position // return URL
parsed_link = cycle_links(anchor_tags, position)


while count != 1:
    #pass new URL through and recieve new anchor list
    anchor_tags = parse_url(parsed_link)
    #cycle through new list of anchor tags
    parsed_link = cycle_links(anchor_tags, position)
    count -= 1

print(parsed_link)
