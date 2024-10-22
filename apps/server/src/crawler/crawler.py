from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import time

def initialize_driver():
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
    return driver

def select_size_button_selector(driver, target_size):
    element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'a[data-option="{target_size}"]'))
        )
    element.click()

def select_size_dropdown_selector(driver, target_size):
    element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'option[value="{target_size}"]'))
        )
    element.click()

def scrap_parfum(driver, target_url, target_size):
    driver.get(target_url)
    time.sleep(3)

    name = driver.find_element(By.ID, 'product-name').text.strip()

    try:
        select_size_dropdown_selector(driver, target_size)
    except:
        select_size_button_selector(driver, target_size)
    
    size = target_size
    price = driver.find_element(By.ID, 'price_display').text.strip()
    isAvailable = not driver.find_element(By.ID, 'stock-notification-request-message').is_displayed()

    return { 'name': name, 'price': price, 'size': size, 'isAvailable': isAvailable }

parfums = [
    {'url': 'https://www.thekingofparfums.com.br/produtos/paco-rabanne-1-million/', 'size': '100 ML'},
    {'url': 'https://www.thekingofparfums.com.br/produtos/giorgio-armani-acqua-di-gio-profondo-lancamento/', 'size': '125ml'},
]

driver = initialize_driver()

for parfum in parfums:
    obj = scrap_parfum(driver, parfum['url'], parfum['size'])

    print(obj['name'])
    print(obj['price'])
    print(obj['size'])
    print(obj['isAvailable'],'\n')

driver.quit()
exit(0)