from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "Profile name"
USERNAME = input("Email: ")
PASSWORD = input("Password: ")


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get("https://www.instagram.com/")

    def login(self):
        time.sleep(5)
        email_field = self.driver.find_element_by_name("username")
        email_field.send_keys(USERNAME)
        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.ENTER)
        time.sleep(20)

    def find_followers(self):
        self.driver.get(url=f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(10)
        followers_field = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        )
        followers_field.click()
        time.sleep(2)
        modal = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[2]'
        )
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        time.sleep(2)
        all_button_field = self.driver.find_elements_by_css_selector("li button")
        for button in all_button_field:
            button.click()
            time.sleep(3)
        self.driver.quit()


insta_bot = InstaFollower(CHROME_DRIVER)
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()


