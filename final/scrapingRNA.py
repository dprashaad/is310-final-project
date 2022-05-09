import bs4
from bs4 import BeautifulSoup

import requests
def scraping_scripts(insert):
    testing=requests.get(insert)
    results=testing.text
    return results
text=scraping_scripts('https://romanticnovelistsassociation.org/awards/#1558103531462-a03d3a64-9cff')
soup=BeautifulSoup(text, features='html.parser')
findingauthors=str(soup.find_all('ul'))

finding1=findingauthors.split('</em>')
finding2=finding1[1:]
authors=[]

for items in finding2:
    authortemp=items.split()
    authors.append(authortemp[1:3])
# print(authors)
for i in range(len(authors)):
    authors[i]=' '.join(authors[i])

titlescript=soup.find_all('em')
tscript=str(titlescript)
titlescriptfixed=tscript.split('<em>')
titles=[]
for items in titlescriptfixed:
    titles.append(items)
titlecleaning= titles[2:]
secondtitlecleaning=[x[:-7] for x in titlecleaning]
finaltitle=[s.replace('\xa0', '') for s in secondtitlecleaning]
# print(newfinal)
yearscript=str(soup.find_all('ul'))
yearscriptsplit=yearscript.split('<li>')
years=yearscriptsplit[3:]
# print(years)
yearlist=[]
for year in years:
    yearlist.append(year[:4])
print(yearlist)
outfile=open('awardlist.csv', 'w', encoding='utf-8')
for i in range(len(authors)):
    outfile.write(yearlist[i] + ', ' + finaltitle[i] + ', ' + authors[i] + '\n')

outfile.close()
