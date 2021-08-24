# getWikiLinks_with_exceptionHandling.py
"""
Get Wiki link and save it in the file. Take the next random link from 
the site, check if the link has not been downloaded once, save it and 
get Wiki links from the new site. Take the next random link ... . 
The program works in the endless loop.
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import datetime
import random
import re
import sys

from bs4 import BeautifulSoup


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
        print(e)
        return None
    # Check for the exception that the server is down.
    except URLError as e:
        print(e)
        return "Server not found"
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.body.h1
    # Check for the exception that the site has no title.
    except AttributeError as e:
        return None
    else:
        return articleUrl

def getLinks(articleUrl):
    """
    Take the end of url from Wikipedia, create the full url adress of 
    the site of Wikipedia and return all url adressess scraped from 
    the created url that concern the Wikipedia.
    """
    html = urlopen(f"http://pl.wikipedia.org{articleUrl}")
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", \
        href=re.compile("^(/wiki/)((?!:).)*$"))

random.seed(datetime.datetime.now())
pages = set()
# Making of the first end of url site from Wikipedia to load.
links = getLinks("/wiki/Olgierd")
# The loop for the handling of the exceptions, for the saving of them 
# in the txt file and for the saving the endings of wikipedia url pages
# in the txt file.
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    checkofurl = getTitle(newArticle)
    # Handling of the exception HTTPError
    if checkofurl == None:
        print(f"Url: {newArticle} could not be found.")
        with open("getWikiLinks_with_exceptionHandling.txt", "a") as f:
            f.write(f"Title: {newArticle} could not be found.")
            f.write("\n")
        links = getLinks(newArticle)
    # Handling of the exception URLError
    elif checkofurl == "Server not found":
        print(f"For the url: {newArticle} server not found.")
        with open("getWikiLinks_with_exceptionHandling.txt", "a") as f:
            f.write(f"For the url: {newArticle} server not found.")
            f.write("\n")
        links = getLinks(newArticle)
    # Saving and printing of the end of wikipedia url page in txt file.
    else:
        # the checking if the link has not been downloaded once.
        if newArticle not in pages:
            print(checkofurl)
            with open("getWikiLinks_with_exceptionHandling.txt", "a") as f:
                f.write(checkofurl)
                f.write("\n")
            newArticle = checkofurl
            pages.add(newArticle)
            links = getLinks(newArticle)
        else:
            newArticle = checkofurl
            links = getLinks(newArticle)