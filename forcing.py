from bs4 import BeautifulSoup
import requests
from datetime import datetime

def getSite():
    response = requests.get('https://www.crous-nantes.fr/restaurant/resto-u-la-chantrerie/')
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        try:
            date = soup.find("time", class_='menu_date_title')
            print(date.text)
            meal = soup.find("div", class_='meal')
            print(meal.text)
        except Exception as e:
            raise Exception('pas de balise')

# Heure de fin (18h00)
end_time = datetime.now().replace(hour=12, minute=0, second=0, microsecond=0)

while True:
    try:
        getSite()
    except Exception as e:
        continue
    else:
        print(f"récup à {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.")
        break

    # Vérifier si l'heure actuelle est passée l'heure de fin
    if datetime.now() >= end_time:
        break