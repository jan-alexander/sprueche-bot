#!/usr/bin/env python3

import urllib.request
import urllib.parse
import json

def main():
    images = []
    images.append("https://www.google.de/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png")

    send_images(images)

def send_images(images):
    TOKEN, CHAT_ID = load_telegram_bot_token_chatid()

    for image in images:
        send_image(TOKEN, CHAT_ID, image)

def send_image(TOKEN, CHAT_ID, image):
    url = "https://api.telegram.org/bot"
    url = url + TOKEN
    url = url + "/sendPhoto"
    url = url + "?chat_id=" + str(CHAT_ID)
    url = url + "&photo=" + urllib.parse.quote(image)

    urllib.request.urlopen(url)

def load_telegram_bot_token_chatid():
    with open('tg_bot.json', 'r') as fp:
        tg_app = json.load(fp)

    return tg_app['token'], tg_app['chat']

if __name__ == "__main__":
    main()
