#!/usr/bin/env python3

import willy
import telegram

def main():
    images = willy.get_new_image_urls()
    telegram.send_images(images)

if __name__ == "__main__":
    main()
