import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_chip_basket_button(browser):
    browser.get(link)
    #time.sleep(30)
    try: chip_basket_button = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn-add-to-basket')))
    except: chip_basket_button = None
    assert chip_basket_button != None, "Don't have chip basket button!"
