#!/usr/bin/env python3

import urllib.request
import json
import time

def main():
    APP_ID, APP_SECRET = load_facebook_app_id_secret()
    since = load_last_call_timestamp()

    image_urls = get_new_image_urls(APP_ID, APP_SECRET, since)
    for image_url in image_urls:
        print("Image: ", image_url)

def load_facebook_app_id_secret():
    with open('fb_app.json', 'r') as fp:
        fb_app = json.load(fp)

    return fb_app['id'], fb_app['secret']

def load_last_call_timestamp():
    filename = 'last_call.json'
    with open(filename, 'r') as fp:
        last_call = json.load(fp)

    old_since = last_call['since']
    last_call['since'] = int(time.time())

    with open(filename, 'w') as fp:
        json.dump(last_call, fp)

    return old_since

def get_new_image_urls(APP_ID, APP_SECRET, since):
    url = "https://graph.facebook.com/v2.8/WillyNachdenklich/posts/?"
    url = url + "access_token=" + APP_ID + "|" + APP_SECRET
    url = url + "&fields=full_picture"
    url = url + "&since=" + str(since)

    images = []
    json_data = render_to_json(url)
    for post in json_data['data']:
        try:
            images.append(post['full_picture'])

        except Exception:
            NOP

    return images

def render_to_json(graph_url):
    web_response = urllib.request.urlopen(graph_url)
    readable_page = web_response.read().decode('utf-8')
    json_data = json.loads(readable_page)

    return json_data

if __name__ == "__main__":
    main()
