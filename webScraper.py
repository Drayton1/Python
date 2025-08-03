#web scraping
import requests
 
url = "https://pixelford.com/blog/"
response = requests.get(url, headers = {user-agent: 'Shello'})
#print(response.content)
#all websites run on html code
#grab html and use it ot our advantage
html = response.content
soup = BeautifulSoup(html, 'html.parser')
a_tags = soup.find_all('a', class_='entry-title-link')

for a_tag in a_tags:
    print(a_tag)
    
