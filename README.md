# Simple crawler with the exceptions handling and the logging

## Motivation:
I am a fun of Star Trek. I made this script to scrap Wikipedia to 
find out how many times the expression 'Star Trek' will appear on 
the selected random Wikipedia pages.

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
- The end of url that is stored in the script must be written with 
  the letters from the English alphabet. 
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
- The file events.log is the text file.

## Script Summary:
The script is taking the end of url of Wikipedia (the end of url is 
stored in the script) and is creating the full url adress of the site 
of Wikipedia. Next the script (after the scraping and the processing 
of the information from the page) is printing and saving in the txt 
file getWikiLinks_with_logging.txt: in the first line the end of 
the Wikipedia url, in the seconod line the title of the page, in 
the next few lines the beginning of the page body (sometimes they're 
blank lines/line), the blank line to distinguish the body from 
the last line (this is necessary because we don't know how many lines 
will have the beginning of the body when the text will be wrapped). 
At the end the script is printing and saving in the txt file: 
the occurs of the expression 'Star Trek' and in the last line 
the separator. Next the script is taking the next random link from 
the site, is chacking if the link has not been downloaded once and is 
getting the necessary information from the new page. The script works 
in the loop. All operations are saved in the txt file 
getWikiLinks_with_logging.txt, except for one. If the url has been 
checked once, it will not be saved in this txt file (the end of url 
and other informations), but the appropriate information will be save 
and print thanks to the operations of the logger. The logger saves and 
prints all its occurrences in the form of the information stored in 
the file events.log . To see what it looks like, please open the file 
getWikiLinks_with_logging.txt and the events.log file.

## Version:
The basic version of the code has tag 1.0.
The target code version is 2.0.
