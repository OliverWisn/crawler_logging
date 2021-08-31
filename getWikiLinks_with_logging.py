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
    url = f"http://en.wikipedia.org{articleUrl}"
    try:
        html = urlopen(url)
    # Check for the exception that there is no website.
    except HTTPError:
        return None
    # Check for the exception that the server is down.
    except URLError:
        return "Server not found"
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.h1.get_text()
        beginning_body = bsObj.find(id="mw-content-text").find("p").get_text()
        times_my_text = len(bsObj.findAll(lambda tag: tag.get_text() == \
            "Star Trek"))
    # Check for the exception that the attribut error occurs.
    except AttributeError:
        return "Something is missing in this page"
    else:
        return articleUrl

def getLinks(articleUrl):
    """
    Take the end of url from Wikipedia, create the full url adress of 
    the site of Wikipedia and return all end of url adressess scraped 
    from the created url that concern Wikipedia's urls.
    """
    html = urlopen(f"http://en.wikipedia.org{articleUrl}")
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", \
        href=re.compile("^(/wiki/)((?!:).)*$"))

random.seed(datetime.datetime.now())
pages = set()
# Making of the first end of url site from Wikipedia to load.
links = getLinks("/wiki/Star_Trek")
# The loop for the handling of the exceptions, for the printing and 
# the saving of them in the txt file. The loop prints and saves in 
# the txt file: the ends of Wikipedia url's, the title of the site, 
# the beginning of the page content and the information how many times 
# the expression 'Star Trek' occurs.
while len(links) > 0:
    # Exceptions handling.
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    checkofurl = getTitle(newArticle)
    # Handling of the exception HTTPError
    if checkofurl == None:
        print(f"Url: {newArticle} could not be found.")
        print("----------------------------------------")
        with open("getWikiLinks_with_logging.txt", "a", encoding="utf-8") as f:
            f.write(f"Title: {newArticle} could not be found."+"\n")
            f.write("----------------------------------------"+"\n")
        links = getLinks(newArticle)
    # Handling of the exception URLError
    elif checkofurl == "Server not found":
        print(f"For the url: {newArticle} server not found.")
        print("----------------------------------------")
        with open("getWikiLinks_with_logging.txt", "a", encoding="utf-8") as f:
            f.write(f"For the url: {newArticle} server not found."+"\n")
            f.write("----------------------------------------"+"\n")
        links = getLinks(newArticle)
    # Handling of the exception AttributeError
    elif checkofurl == "Something is missing in this page":
        print(f"For the url: {newArticle} something is missing in the page.")
        print("----------------------------------------")
        with open("getWikiLinks_with_logging.txt", "a", encoding="utf-8") as f:
            f.write(f"For the url: {newArticle} something is missing") 
            f.write(" in the page."+"\n")
            f.write("----------------------------------------"+"\n")
        links = getLinks(newArticle)
    # Saving and printing in txt file of: the ends of Wikipedia url's, 
    # the title of the site, the beginning of the page content, 
    # the information how many times the expression 'Star Trek' occurs.
    else:
        # the checking if the link has not been downloaded once.
        if newArticle not in pages:
            html = urlopen(f"http://en.wikipedia.org{checkofurl}")
            bsObj = BeautifulSoup(html, "html.parser")
            print(checkofurl)
            print(bsObj.h1.get_text())
            print(bsObj.find(id="mw-content-text").find("p").get_text())
            my_text_appearance = len(bsObj.findAll(lambda tag: tag.get_text()==\
                "Star Trek"))
            print(f"The expression 'Star Trek' on this page appears\
                {my_text_appearance} times")
            print("----------------------------------------")
            with open("getWikiLinks_with_logging.txt", "a",\
             encoding="utf-8") as f:
                f.write(checkofurl+"\n")
                f.write(bsObj.h1.get_text()+"\n")
                f.write((bsObj.find(id="mw-content-text").find("p").get_text())\
                    +"\n")
                f.write(f"The expression 'Star Trek' on this page appears\
                    {my_text_appearance} times"+"\n")
                f.write("----------------------------------------"+"\n")
            newArticle = checkofurl
            pages.add(newArticle)
            links = getLinks(newArticle)
        # If the link has been downloaded once, select the next link 
        # and save the debug message in the logger text file.
        else:
            logger.info(f"This site has already been checked: {newArticle}")
            newArticle = checkofurl
            links = getLinks(newArticle)