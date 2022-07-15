import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.allsides.com/media-bias/media-bias-ratings'
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
    }
r = requests.get(url, headers=header)
soup = bs(r.content, "html.parser")

#select_one('body') gets the body element
#select_one('.temp') to get <a class="temp"></a>
#select_one('#temp') to get <a id="temp"></a>
#select_one('.temp a') to get <div class="temp"><a></a></div>
#select_one('.temp.example') to get <a class="temp example"></a>

rows = soup.select('tbody tr')

row = rows[0]
name = row.select_one('.views-field-title')
nametext = row.select_one('.views-field-title').text.strip()
print(name)
print(nametext)

allsides_page = row.select_one('.views-field-title a')['href'] #Selecting attribute href from the element a
allsides_page = 'https://www.allsides.com' + allsides_page
print(allsides_page)

mydivs = soup.find_all("div", {"class": "stylelistrow"}) # return all divs with class "stylelistrow"