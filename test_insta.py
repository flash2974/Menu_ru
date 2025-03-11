from instagrapi import Client
from instagrapi.story import StoryBuilder
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag

ACCOUNT_USERNAME = "menu_ru_chantrerie"
cl = Client()
cl.login(ACCOUNT_USERNAME, "MenuRU2025!")

# cl.photo_upload_to_story('./black.jpg', "cpation")

build = StoryBuilder('./black.jpg', "caption de mede").photo(max_duration=10)

cl.photo_upload_to_story(build.path)
