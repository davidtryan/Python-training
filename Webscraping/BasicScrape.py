# Based on prompt from:
#http://docs.python-guide.org/en/latest/scenarios/scrape/#lxml-and-requests

# Need to run the following before executing program
#pip install lxml
#pip install requests
#pip install beautifulsoup4


#import lxml and requests modules
from lxml import html
import requests

#assign the webpage to be used and put it in a tree structure
url = 'http://econpy.pythonanywhere.com/ex/001.html'
page = requests.get(url)
tree = html.fromstring(page.text)

#Create a list of buyers
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#Create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

#Move through all links on webpage
from bs4 import BeautifulSoup
import urllib2

urlM = urllib2.urlopen(url)

content = urlM.read()

soup = BeautifulSoup(content)

links = soup.findAll("a")

for link in links:
  currLink = link
  newPage = requests.get(currLink.get('href'))
  newTree = html.fromstring(newPage.text)
  
  #Create a list of buyers
  newBuyers = newTree.xpath('//div[@title="buyer-name"]/text()')
  #Create a list of prices
  newPrices = newTree.xpath('//span[@class="item-price"]/text()')
  
  buyers.extend(newBuyers)
  prices.extend(newPrices)

#View what was obtained
print 'Buyers: ', buyers
print 'Prices: ', prices
