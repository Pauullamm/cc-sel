from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

url = "https://orteil.dashnet.org/cookieclicker/"
wait = WebDriverWait(driver, 10)
driver.get(url)

try:        
    
    consent_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fc-cta-consent")))
    if consent_button:
        consent_button.click()
    eng_button = wait.until(EC.presence_of_element_located((By.ID, "langSelect-EN")))
    if eng_button:
        eng_button.click()
    cookie_count = wait.until(EC.presence_of_element_located((By.ID, "cookies")))
    cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))
    print(cookie_count.text)

    time.sleep(3)
    while True:
        cookie_button.click()
except Exception as e:
    print(e)

finally:

    time.sleep(10)
    driver.quit()


