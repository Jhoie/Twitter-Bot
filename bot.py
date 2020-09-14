from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/?lang=en")
        time.sleep(3)
        bot.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/a[2]/div").click()

        time.sleep(2)  # if element not interactable, you have to wait!
        bot.find_element_by_name("session[username_or_email]").send_keys(self.username)
        bot.find_element_by_name("session[password]").send_keys(self.password)
        bot.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div").click()
        time.sleep(30)
        
        
act = TwitterBot("xxxxx", "xxxxx")
act.login()
