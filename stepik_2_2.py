from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
        link = "http://suninjuly.github.io/file_input.html"
        browser = webdriver.Chrome()
        browser.get(link)


        input1 = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
        input1.send_keys("y")
        input2 = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
        input2.send_keys("y")
        input3 = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
        input3.send_keys("y")

        file = open("file.txt", "w+")
        file.close()
        element = browser.find_element(By.CSS_SELECTOR, 'input#file')
        current_dir = os.path.abspath(
                os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
        file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
        element.send_keys(file_path)

        #press button
        button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()