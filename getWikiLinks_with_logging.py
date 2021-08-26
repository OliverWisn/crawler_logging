# getWikiLinks_with_exceptionHandling.py
"""
Simple crawler with the exceptions handling and the logging.
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import datetime
import random
import re
import sys
import logging

from bs4 import BeautifulSoup


    # logging.basicConfig(filename='example.log', encoding='utf-8'), 
    #   level=logging.DEBUG)

# create logger
logger = logging.getLogger('Mainstream')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('events.log')
fh.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)-12s - %(levelname)-8s \
    - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    # format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    #                    datefmt='%m-%d %H:%M',
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s 
    #   - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
    # logging.basicConfig(filename='example.log', encoding='utf-8')
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')


def getTitle(articleUrl):
    """
    Take the end of url from Wikipedia, create the full url adress of 
    the site of Wikipedia and check the full url's for exceptions. 
    After no exceptions will occur return the end of url.
    """
    url = f"http://pl.wikipedia.org{articleUrl}"
    try:
        html = urlopen(url)
    # Check for the exception that there is no website.
    except HTTPError as e:
        return None
    # Check for the exception that the server is down.
    except URLError as e:
        return "Server not found"
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.h1.get_text()
        title1 = bsObj.findAll("p", [0])
#        title2 = bsObj.find(id="ca-edit").find("span").find("a").attrs['href']
    # Check for the exception that the site has no title.
    except AttributeError as e:
        return "Something is missing in this page"
    else:
        return articleUrl

def getLinks(articleUrl):
    """
    Take the end of url from Wikipedia, create the full url adress of 
    the site of Wikipedia and return all end of url adressess scraped 
    from the created url that concern Wikipedia.
    """
    html = urlopen(f"http://pl.wikipedia.org{articleUrl}")
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", \
        href=re.compile("^(/wiki/)"))

random.seed(datetime.datetime.now())
pages = set()
# Making of the first end of url site from Wikipedia to load.
links = getLinks("/wiki/Star_Trek")
# The loop for the handling of the exceptions, for the saving of them 
# in the txt file and for the saving the endings of wikipedia url pages
# in the txt file.
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    checkofurl = getTitle(newArticle)
    # Handling of the exception HTTPError
    if checkofurl == None:
        print(f"Url: {newArticle} could not be found.")
        with open("getWikiLinks_with_logging.txt", "a") as f:
            f.write(f"Title: {newArticle} could not be found.")
            f.write("\n")
        links = getLinks(newArticle)
    # Handling of the exception URLError
    elif checkofurl == "Server not found":
        print(f"For the url: {newArticle} server not found.")
        with open("getWikiLinks_with_logging.txt", "a") as f:
            f.write(f"For the url: {newArticle} server not found.")
            f.write("\n")
        links = getLinks(newArticle)
    # Handling of the exception AttributeError
    elif checkofurl == "Something is missing in this page":
        print(f"For the url: {newArticle} something is missing in the page.")
        with open("getWikiLinks_with_logging.txt", "a") as f:
            f.write(f"For the url: {newArticle} something is missing") 
            f.write(" in the page.")
            f.write("\n")
        links = getLinks(newArticle)
    # Saving and printing of the end of wikipedia url page in txt file.
    else:
        # the checking if the link has not been downloaded once.
        if newArticle not in pages:
            html = urlopen(f"http://pl.wikipedia.org{checkofurl}")
            bsObj = BeautifulSoup(html, "html.parser")
            print(checkofurl)
            print(bsObj.h1.get_text())
            print(bsObj.findAll("p", [0]))
#            print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
            with open("getWikiLinks_with_logging.txt", "a") as f:
                f.write(checkofurl + "\n")
                f.write(bsObj.h1.get_text() + "\n")
#                f.write(bsObj.find(id="mw-content-text").findAll("p", [0]) + \
#                    "\n")
#                f.write(bsObj.find(id="ca-edit").find("span").find("a").attrs\
#                    ['href'] + "\n")
                f.write("\n")
            newArticle = checkofurl
            pages.add(newArticle)
            links = getLinks(newArticle)
        else:
            logger.info(f"This site has already been checked: {newArticle}")
            newArticle = checkofurl
            links = getLinks(newArticle)