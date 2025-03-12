from instagrapi import Client
import schedule
from RU_Scraper import *
from dotenv import load_dotenv
from os import getenv
import time

load_dotenv()
USERNAME = getenv("USERNAME")
PASSWORD = getenv("PASSWORD")
cl = Client()

def actions(max_attempts=3):
    attempts = 0
    while attempts <= max_attempts:
        try:
            cl.login(USERNAME, PASSWORD)
            dico = getMenu()
            createImage(dico)
            cl.photo_upload_to_story('./image.png')
            break
        
        except Exception as e:
            print(e)
            attempts += 1
            if attempts <= max_attempts :
                time.sleep(300)
            else :
                break
                
        finally:
            cl.logout()


if __name__ == '__main__':
    hour = "10:20"
    # hour = "17:28"

    schedule.every().monday.at(hour, "Europe/Paris").do(actions)
    schedule.every().tuesday.at(hour, "Europe/Paris").do(actions)
    schedule.every().wednesday.at(hour, "Europe/Paris").do(actions)
    schedule.every().thursday.at(hour, "Europe/Paris").do(actions)
    schedule.every().friday.at(hour, "Europe/Paris").do(actions)

    while True :
        schedule.run_pending()