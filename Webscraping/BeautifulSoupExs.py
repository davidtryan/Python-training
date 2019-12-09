# More examples using BeautifulSoup for webscraping
# http://www.pythonforbeginners.com/python-on-the-web/beautifulsoup-4-python/
# http://www.newthinktank.com/2010/11/python-2-7-tutorial-pt-13-website-scraping/
# http://www.pythonforbeginners.com/beautifulsoup/scraping-websites-with-beautifulsoup
# Before running execute the following:
#pip install beautifulsoup4

####################################################################
### This finds all the links included in the webpage listed and
### prints them iteratively to the screen
####################################################################
from bs4 import BeautifulSoup
import urllib2 
from urllib import urlopen

#Pull the links and html tags on python.org
url = urllib2.urlopen("http://www.python.org")

content = url.read()

soup = BeautifulSoup(content)

links = soup.findAll("a")
print links

#Pull the links from reddit and print them
pageFile = urllib2.urlopen("http://www.reddit.com")

pageHtml = pageFile.read()

pageFile.close()

soup = BeautifulSoup("".join(pageHtml))

#sAll = soup.findAll("li")
sAll = soup.findAll("a")

for href in sAll:
    print href
	
	

	
	
	
####################################################################	
### This code scrapes a news feed and pulls out article titles
### and their links. This uses re to identify and separate titles
### and links from the main website body information. We then move
### through the document and pull out links and then paragraphs 
### in the articles corresponding to the links and titles and
### prints them iteratively.
####################################################################	
from urllib import urlopen

import re

# Copy all of the content from the provided web page
webpage = urlopen('http://www.huffingtonpost.com/news/rss-feed/').read()

# Grab everything that lies between the title tags using a REGEX
patFinderTitle = re.compile('<h3><a href.*>(.*)</a></h3>')

# Grab the link to the original article using a REGEX
patFinderLink = re.compile('<h3><a href="(.*)"')

# Store all of the titles and links found in 2 lists
findPatTitle = re.findall(patFinderTitle,webpage)

findPatLink = re.findall(patFinderLink,webpage)

# Create an iterator that will cycle through the first 16 articles and skip a few
listIterator = []

listIterator[:] = range(0,len(findPatLink))
print listIterator

for i in listIterator:
  print findPatTitle[i]
  print findPatLink[i]
  
  articlePage = urlopen(findPatLink[i]).read()
  
  divBegin = articlePage.find('<!-- Entry Text -->')
  
  article = articlePage[divBegin:(divBegin+1000)]
  
  soup = BeautifulSoup(article)
  
  paragList = soup.findAll('p')
  
  for i in paragList:
    print i

  print "\n"
  
  

 
#################################################################### 
### This code scrapes a news feed and pulls out article titles
### and their links. This uses BeautifulSoup to search for 'h3'
### which picks out a label that includes the title and link. We
### further parsed the title and link out of the extracted info. 
####################################################################
# Copy all of the content from the provided web page
webpage = urlopen('http://www.huffingtonpost.com/news/rss-feed/').read()

# Grab everything that lies between the title tags using a REGEX
patFinderTitle = re.compile('<h3><a href.*>(.*)</a></h3>')

# Grab the link to the original article using a REGEX
patFinderLink = re.compile('<h3><a href="(.*)"')

# Store all of the titles and links found in 2 lists
findPatTitle = re.findall(patFinderTitle,webpage)

findPatLink = re.findall(patFinderLink,webpage)

# Create an iterator that will cycle through the first 16 articles and skip a few
listIterator = []

listIterator[:] = range(0,len(findPatLink))

soup2 = BeautifulSoup(webpage)

titleSoup = soup2.findAll('h3')

for i in titleSoup:
  a = str(i.findAll('a'))
  if a:
	start = a.find('href="')
	end = a.find('">')
	linkText = a[start+6:end]
	
	start2 = a.find('html">')
	end2 = a.find('"(/a')
	titleText = a[start2+6:end2-4]
	print titleText
	print linkText
  print '\n'
  
print "\n"





