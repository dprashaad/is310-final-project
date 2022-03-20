import bs4
from bs4 import BeautifulSoup

infile=open('raw_script_urls.txt', 'r', encoding='utf-8')
all_the_text=infile.read()

infile.close()

results = all_the_text.split('+++$+++')

urls = [value for index, value in enumerate(results) if index %2==0]
urls.remove('m0 ')
newurl=[x[:-4] for x in urls]
cleanurl=[x[1:] for x in newurl]
# print(cleanurl)
outfile=open('potentialscripts.txt', 'w', encoding='utf-8')
import requests
def scraping_scripts(insert):
    testing=requests.get(insert)
    results=testing.text
    return results

for url in cleanurl:
    text=scraping_scripts(url)
    soup=BeautifulSoup(text, features='html.parser')
    justscript=soup.find_all('pre')
    script=str(justscript)
    outfile.write(script)

outfile.close()

# outfileagain=open('allscripts.txt', 'r', encoding='utf-8')  #using r uses an existing file bc it's reading it, not creating it
# reading=outfileagain.read()
# soup=BeautifulSoup(reading, features="html.parser")
#
# newfile=open('cleanscripts.txt', 'w', encoding='utf-8')


# justscript=soup.find_all('pre')
# script=str(justscript)
#
# newfile.write(script)
# outfileagain.close()
# print('done')
# newfile.close()
