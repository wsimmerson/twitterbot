from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

import env


class TwitterBot():
    def __init__(self, username, password):
        self.username = username
        self.password = password

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
            "https://twitter.com/search?f=tweets&vertical=default&q=%23webdev&src=tyah")

        for x in range(1, 10):
            self.bot.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randrange(10, 30))

        # tweets = self.bot.find_element_by_class_name("tweet")
        links = []
        for tweet in self.bot.find_elements_by_class_name("tweet"):
            links.append(tweet.get_attribute("data-permalink-path"))

        for link in links:
            self.bot.get("https://twitter.com/{}".format(link))
            favBtn = self.bot.find_element_by_class_name("js-actionFavorite")
            favBtn.click()
            time.sleep(random.randrange(30, 60))


if __name__ == '__main__':
    bot = TwitterBot(env.USERNAME, env.PASSWORD)
    bot.activate()
