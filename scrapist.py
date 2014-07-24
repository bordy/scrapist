from bs4 import BeautifulSoup
from datetime import datetime, date
import requests

# Sets date to current, formatted for USCCB site
pull_date = datetime.strftime(datetime.today(), '%m%d%y')

cath_response = requests.get('http://www.usccb.org/bible/readings/' + pull_date + '.cfm')
cath_soup = BeautifulSoup(cath_response.text)

# print cath_soup.prettify()

for a in cath_soup.find_all("div", {"class": "bibleReadingsWrapper"}):
    title_text = a.find('h4').text
    body_text = a.find('div', {'class': 'poetry'}).text

    print title_text
    print body_text