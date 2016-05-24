from lxml import html
from lxml import etree
import requests
#from io import StringIO, BytesIO
import urllib2

# RSS:
#page = requests.get('http://www.investopedia.com/rss/')
#print page.content

#page = requests.get('http://finance.yahoo.com/news/buffett-says-government-did-dow-124652732.html')
#page = requests.get('http://www.investopedia.com/markets/stocks/googl/')
#print type(page.content)
# it's a str
#tree = html.fromstring(page.content)
#print dir(tree)
#print page.content

url = 'http://www.investopedia.com/markets/stocks/googl/'
doc = html.parse(urllib2.urlopen(url))
#tree = etree.HTML(doc)
root = etree.HTML(html.tostring(doc))

l = []
for element in root.iter():
  str = ""
  if element.text:
    str = element.text.strip()
  if "View All" == str:
    l.append(element)

reports = []
for e in l:
  div = e.getparent().getparent()
  next = div.getnext()
  if next.get("class") != "box clear": continue
  children = list(next)
  for ch in children:
    if (ch.tag != "ol" and ch.get("class") != "list"): continue
    items = list(ch)
    for item in items:
      if item.tag == "li":
        news = dict()
        for se in list(item):
          #print etree.tostring(se)
          if se.tag == "a":
            news['article'] = "http://www.investopedia.com" + se.get("href")
            news['img'] = list(se)[0].get("src")
          elif se.tag == "h3":
            news['title'] = list(se)[0].text.strip()
            #print list(se)[0].text.strip()
          elif se.tag == "div":
            #TODO take the entire div tag? contains link for author, article date and time
            news['author'] = list(se)[0].text.strip()
        reports.append(news)

for d in reports:
  print 
  for (k, v) in d.items():
    print k+":"
    print v





#root = tree.getroot()
#print root.tag
#print dir(root)


# print html
page = requests.get('http://www.investopedia.com/markets/stocks/googl/')
#print page.content
