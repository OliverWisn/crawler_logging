# Simple crawler with the exceptions handling and the logging

## Motivation:
I make this script because I learn the web scraping. I would like to 
walk through the Python Standard Library + beautifulsoup and logging. 

## Requirements: 
python 3.9 - rest in requirements.txt .

## Remarks:
I make this script so that the master branch has always the functioning 
code. To run the script you must run the file 
"getWikiLinks_with_logging.py". The script works in the endless loop 
(in fact the script can hang after 1000 cycles due to recursion in 
some cases), so you have to stop it manually. The script is written in 
UTF-8, so the end of url that is stored in the script must be written 
in UTF-8. If you use the script for a long time and use wikipedia 
resources in this way, think about donation to wikipedia. I normally 
use the logging snippet for internal use only in the debuging and you 
won't see it in the finished client program. I run the individual lines 
in the logging as needed.

## Script Summary:
The script is taking the end of url from Wikipedia (the end of url is 
stored in the script), is saving it in the txt file 
getWikiLinks_with_logging.txt, is creating the full url adress of 
the site of Wikipedia and returns all end of url adressess scraped 
from the created url that concern Wikipedia. Next the script takes 
the next random link from the site, checks if the link has not been 
downloaded once, saves it and gets the end of Wiki links from this new 
site. All operations are additionally shown in the shell, except for 
one. If the url has been checked once, it will not be saved in the txt 
file (the end of url), but the appropriate information will be shown 
in the shell thanks to the operation of the logger. In addition, 
the logger saves all its occurrences in the form of the information 
stored in the file events.log .

## Version:
The basic version of the code has tag 1.0.
