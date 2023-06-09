import json
from selenium.webdriver.common.by import By
from base_page import BasePage
import time

class four_page(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def send_text(self):
        json_file = open('data.json', 'r')
        data = json.load(json_file)
        text1 = data['sender']
        text2 = data['blessing']
        picture = data['picture']
        phone1 = data['sender_phone']
        phone2 = data['recipt_phone']
       # Url = data['Four_url']
       # self.driver.get(Url)
        self.send_key(By.XPATH, "//input[@maxlength='25']", text1)
        time.sleep(1)
        blessing = self.driver.find_element(By.CLASS_NAME, "input-label-wrapper")
        blessing.click()
        blessing.find_element(By.CSS_SELECTOR, 'li[value="10"]').click()
        self.clear_element(By.XPATH, "//textarea[@rows='4']")
        self.send_key(By.XPATH, "//textarea[@rows='4']", text2)
        self.send_key(By.NAME, "logo", picture)
        self.click_element(By.XPATH, "//button[@gtm='המשך']")
        sms = self.driver.find_element(By.CLASS_NAME, "method-icon")
        sms.click()
        sms.find_element(By.XPATH, "//input[@placeholder='נייד מקבל/ת המתנה']").send_keys(phone1)
        self.send_key(By.XPATH, "//input[@placeholder='שם שולח המתנה']", text1)
        self.send_key(By.XPATH, "//input[@placeholder='מספר נייד']", phone2)
        self.driver.find_element(By.XPATH, "//button[@gtm='המשך לתשלום']").click()
        self.driver.find_element(By.XPATH, "//button[@gtm='המשך לתשלום']").screenshot('4')


    def tearDown(self):
        self.driver.quit()