'''
    This is a script used for Web-Scraping
'''

import bs4, requests
from bs4 import BeautifulSoup

# function that uses requests module and soup to get the page data
def getInfo(pageURL):
    # calling requests module for fetching the page
    res = requests.get(pageURL,headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
    res.raise_for_status()

    # calling soup for parsing the html and css selection
    soup = BeautifulSoup(res.text, 'html.parser')

    # soupElement = soup.select('#a-autoid-9-announce')
    # info = soupElement[0].text.strip()

    #  you may add the elements of your choice to read here
    soupElement = soup.find_all('tr')
    info = soupElement

    return info



# Place your product url here
amazonProductURL        = "https://www.amazon.in/Intelligent-Investor-English-Paperback-2013/dp/0062312685"
universityRankingsURL   = "https://www.timeshighereducation.com/world-university-rankings/2019/subject-ranking/computer-science"
info = getInfo(universityRankingsURL)

print(info)