import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.crous-nantes.fr/restaurant/resto-u-la-chantrerie/')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    date = soup.find("time", class_ = 'menu_date_title')
    print(date.text)
    meal = soup.find("div", class_ = 'meal')
    print(meal.text)
