from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math
import os

curr_dir = os.path.abspath(os.path.dirname(__file__))

# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
# def scroll(el,driver):
#     driver.execute_script("return arguments[0].scrollIntoView(true);",el)

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Firefox()
    browser.get(link)
    browser.find_element(By.NAME,"firstname").send_keys("ABOAB")
    browser.find_element(By.NAME,"lastname").send_keys("ABOBA")
    browser.find_element(By.NAME,"email").send_keys("ABOBA@aboba.kz")
    file_path = os.path.join(curr_dir,"empty.txt")
    browser.find_element(By.ID, "file").send_keys(file_path)

    
   
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
