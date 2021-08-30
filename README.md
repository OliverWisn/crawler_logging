# Simple crawler with the exceptions handling and the logging

## Motivation:
I am a fun of Star Trek. I made this script to scrap Wikipedia to 
find out how many times the expression 'Star Trek' will appear on 
the selected Wikipedia random pages.

## Requirements: 
python 3.9 - rest in requirements.txt .

## Remarks:
- I made this script so that the master branch has always the functioning 
  code. 
- To run the script you must run the file 
  "getWikiLinks_with_logging.py". 
- The script works in the endless loop (in fact the script can hang 
  after 1000 cycles due to recursion in some cases), so you have to 
  stop it manually. 
- The script is written in UTF-8, so the end of url that is stored in 
  the script must be written in UTF-8. 
- If you use the script for a long time and use Wikipedia resources in 
  this way, think about donation to Wikipedia. 
- I normally use the logging snippet for internal use only in 
  the debugging and you won't see it in the finished client program. 
  I run the individual lines of the code in the logging as needed.
- Wikipedia is very friendly for the low speed bots, but however, some 
  sites are blocked anyway for the bots. This blocked sites are written
  in the file robots.txt from Wikipedia as disallows. I simplified 
  the script by not including of the code relating to the file 
  robots.txt handling. Then this program can only be used for 
  the learning, not for the production environment.

## Script Summary:
The script is taking the end of url from Wikipedia (the end of url is 
stored in the script), is printing and saving from the site in the txt file 
getWikiLinks_with_logging.txt. , is creating the full url adress of 
the site of Wikipedia and returns all ends of url adressess scraped 
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
