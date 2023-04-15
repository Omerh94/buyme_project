import json
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Register_Page import RegisterPage
from home_screen import homeScreen
from third_page import ThirdPage
from four_page import four_page

class Test_Buyme_Pages(TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome(service=Service("C:\\Users\\Refael\\Downloads\\chromedriver_win32\\chromedriver.exe"))

        self.Register_Page = RegisterPage(self.driver)
        self.home_screen = homeScreen(self.driver)
        self.Third_Page = ThirdPage(self.driver)
        self.four_page = four_page(self.driver)

    def test_register_box(self):
        self.Register_Page.send_text()
        self.home_screen.send_text()
        self.Third_Page.send_text()
        self.four_page.send_text()

    def tearDown(self):
        self.driver.quit()