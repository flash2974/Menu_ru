import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont




def getMenu() :
    try :
        response = requests.get('https://www.crous-nantes.fr/restaurant/resto-u-la-chantrerie/')
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            date = soup.find("time", class_='menu_date_title')      
            meal = soup.find("ul", class_='meal_foodies')
            if not date or not meal :
                raise Exception('pas date/meal')
    
    except :
        raise Exception('kde')
    
    else :
        dico = {}
        dico['date'] = date.text.strip()
        dico['menu'] = {}
        for meal_item in meal.find_all("li", recursive=False):
            meal_type = meal_item.contents[0].strip()
            
            dico['menu'][meal_type] = []
            
            sub_meals = meal_item.find("ul")
            if sub_meals:
                for sub_meal in sub_meals.find_all("li"):
                    dico['menu'][meal_type].append(sub_meal.text.strip())
        
        return dico
                       


def drawCenter(draw: ImageDraw.Draw, font: ImageFont, image: Image, text, y):
    bbox = draw.textbbox((0, 0), text, font=font)
    
    text_width = bbox[2] - bbox[0]
    x = (image.width - text_width) / 2

    draw.text((x, y), text, fill="white", font=font)


def createImage(dico):
    image = Image.new('RGB', (720, 1280), color=(0, 0, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', 40)

    # Date
    drawCenter(draw, font, image, dico['date'], 170)
    
    y = 250
    for meal_type in dico['menu'] :
        drawCenter(draw, font, image, meal_type + " : ", y)
        y += 40
        
        for sub_meal in dico['menu'][meal_type] :
            drawCenter(draw, font, image, "- "+sub_meal, y)
            y += 40
            
        y += 50

    image.save('image.png')