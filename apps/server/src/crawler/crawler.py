import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def initialize_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def scrapParfum(driver, target_url):
    driver.get(target_url)
    time.sleep(3)

    name = driver.find_element(By.ID, 'product-name').text.strip()
    price = driver.find_element(By.ID, 'price_display').text.strip()
    size = driver.find_element(By.CSS_SELECTOR, 'option[selected="selected"]').text.strip()
    isAvailable = not driver.find_element(By.ID, 'stock-notification-request-message').is_displayed()

    return { 'name': name, 'price': price, 'size': size, 'isAvailable': isAvailable }

parfuns = [
    'https://www.thekingofparfums.com.br/produtos/giorgio-armani-acqua-di-gio-profondo-lancamento/',
    'https://www.thekingofparfums.com.br/produtos/paco-rabanne-1-million-royal/',
    'https://www.thekingofparfums.com.br/produtos/invictus-paco-rabanne/'
]

driver = initialize_driver()

for url in parfuns:
    obj = scrapParfum(driver, url)

    print(obj['name'])
    print(obj['price'])
    print(obj['size'])
    print(obj['isAvailable'],'\n')

driver.quit()
exit(0)