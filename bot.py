from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import sys

import config


class TwitterBot():
    def __init__(self, username, password):
        self.username = username
        self.password = password

        try:
            self.hashtag = config.HASHTAG
        except:
            print("config.HASHTAG must be defined")
            sys.exit(1)

        try:
            self.pages_to_scroll = config.PAGES
        except:
            self.pages_to_scroll = 10

        self.bot = webdriver.Chrome()

    def activate(self):
        print("running...")
        self.bot.get("https://twitter.com/login")
        time.sleep(3)

        usernameBox = self.bot.find_element_by_class_name("js-username-field")
        usernameBox.clear()
        usernameBox.send_keys(self.username)

        passwordBox = self.bot.find_element_by_class_name(
            "js-password-field")
        passwordBox.clear()
        passwordBox.send_keys(self.password)
        passwordBox.submit()

        time.sleep(15)
        self.bot.get(
            "https://twitter.com/search?f=tweets&vertical=default&q=%23{}&src=tyah".format(self.hashtag))

        for x in range(1, self.pages_to_scroll):
            self.bot.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            # for more humanesque scrolling behavior
            time.sleep(random.randrange(10, 30))

        links = []
        for tweet in self.bot.find_elements_by_class_name("tweet"):
            links.append(tweet.get_attribute("data-permalink-path"))

        for link in links:
            self.bot.get("https://twitter.com/{}".format(link))
            favBtn = self.bot.find_element_by_class_name("js-actionFavorite")
            try:
                favBtn.click()
            except Exception as e:
                # sometimes the clicks fail, not sure why yet.
                print("Error: ", e)
            # How long does it take for a human to read a tweet?
            time.sleep(random.randrange(20, 60))


if __name__ == '__main__':
    bot = TwitterBot(config.USERNAME, config.PASSWORD)
    bot.activate()
