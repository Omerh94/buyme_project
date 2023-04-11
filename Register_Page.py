import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


class RegisterPage():
    def __init__(self, driver):
        self.driver = driver
    def send_text(self):
        self.driver.find_element(locate_with(By.CLASS_NAME, "notSigned")).click()
        time.sleep(1)
        self.driver.find_element(locate_with(By.XPATH, "//span[@class='text-link theme']")).click()

        self.driver.find_element(locate_with(By.XPATH, "//input[@placeholder='שם פרטי']")).send_keys('refael')
        self.driver.find_element(locate_with(By.XPATH, "//input[@placeholder='מייל']")).send_keys('gsahl5T@gmail.com')

        self.driver.find_element(locate_with(By.XPATH, "//input[@placeholder='סיסמה']")).send_keys('Re123456')
        self.driver.find_element(locate_with(By.XPATH, "//input[@placeholder='אימות סיסמה']")).send_keys('Re123456')
        self.driver.find_element(locate_with(By.CLASS_NAME, "fill")).click()

    def tearDown(self):
        self.driver.quit()
