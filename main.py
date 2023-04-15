from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time

import select



driver = webdriver.Chrome(service=Service("D:\\Omer\\Downloads\\chromedriver_win32\\chromedriver.exe"))
driver.get('https://buyme.co.il/')
chrome_options = Options()
chrome_options.add_argument("--headless")
options=chrome_options

driver.find_element(locate_with(By.CLASS_NAME, "notSigned")).click()
time.sleep(3)
driver.find_element(locate_with(By.XPATH, "//span[@class='text-link theme']")).click()

driver.find_element(locate_with(By.XPATH, "//input[@placeholder='שם פרטי']")).send_keys('omer')
driver.find_element(locate_with(By.XPATH, "//input[@placeholder='מייל']")).send_keys('vf5T@gmail.com')
driver.find_element(locate_with(By.XPATH, "//input[@placeholder='סיסמה']")).send_keys('Re123456')
driver.find_element(locate_with(By.XPATH, "//input[@placeholder='אימות סיסמה']")).send_keys('Re123456')
First_Name = 'omer'
driver.find_element(locate_with(By.CLASS_NAME, "fill")).click()
time.sleep(3)
#assert driver.find_element(locate_with(By.XPATH, "//input[@placeholder='שם פרטי']")).text == 'omer'
driver.find_element(locate_with(By.CSS_SELECTOR, "span[class=label]")).click()
time.sleep(3)

rar = driver.find_element(By.CLASS_NAME, "input-label-wrapper")
rar.click()
#selected = Select(rar.find_element(By.TAG_NAME, 'select'))
#selected.select_by_value('1')
rar2 = rar.find_element(By.CSS_SELECTOR,'li[value="1"]')
rar2.click()
time.sleep(2)

rar = driver.find_elements(By.CLASS_NAME, "input-label-wrapper")[1]
rar.click()
rar2 = rar.find_element(By.CSS_SELECTOR,'li[value="11"]')
rar2.click()
time.sleep(2)

rar = driver.find_elements(By.CLASS_NAME, "input-label-wrapper")[2]
rar.click()
rar2 = rar.find_element(By.CSS_SELECTOR,'li[value="22"]')
rar2.click()
time.sleep(2)

driver.find_element(locate_with(By.XPATH, "//input[@placeholder='איזו מתנה תרצו לחפש?']")).send_keys('AZRIELI GIFTCARD')
time.sleep(2)

driver.find_element(locate_with(By.CSS_SELECTOR, "a[rel=nofollow]")).click()
time.sleep(4)

Url = 'https://buyme.co.il/search'
#assert driver.find_element(locate_with(By.XPATH, "//link[@rel='canonical']" and "//link[@href='https://buyme.co.il/search']" )).text == Url

driver.find_element(locate_with(By.CSS_SELECTOR, "div[class=top]")).click()
time.sleep(2)

driver.find_element(locate_with(By.XPATH, "//input[@placeholder='הכנס סכום']")).send_keys('100')
time.sleep(2)

driver.find_element(locate_with(By.CSS_SELECTOR, "button[type=submit]")).click()
time.sleep(2)

# driver.find_element(locate_with(By.CSS_SELECTOR, "div[gtm=למישהו אחר]")).click()
# time.sleep(2)

driver.find_element(locate_with(By.XPATH, "//input[@maxlength='25']")).send_keys('ספיר')
time.sleep(2)

rar = driver.find_element(By.CLASS_NAME, "input-label-wrapper")
rar.click()
rar2 = rar.find_element(By.CSS_SELECTOR,'li[value="10"]')
rar2.click()
time.sleep(2)
selected = Select(driver.find_element(By.NAME, 'eventType'))
# selected.select_by_visible_text('יום הולדת')
time.sleep(3)

