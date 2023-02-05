# BeauifulSoub--> pip install beautifulsoup4
# requests    --> pip install requests
# ----------------------------------
import requests
from bs4 import BeautifulSoup

def google_search(query):
    response = requests.get(f"https://www.google.com/search?q={query}")
    soup = BeautifulSoup(response.text,'html.parser')
    result = []
    for r in soup.find_all('div',class_="BNeawe"):
        anchors = r.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = r.find('span').text 
            item = {
                "link": link,
                "title": title,
            }
            result.append(item)
    return result
gs = google_search("Python Programming")
for indx, val in enumerate(gs):
    print(f"Result number : {str(indx+1)}\n")
    print(val["title"])
    print(val["link"][1:])
    print("="*80)
    print("\n")
