from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math
import os

curr_dir = os.path.abspath(os.path.dirname(__file__))

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
# def scroll(el,driver):
#     driver.execute_script("return arguments[0].scrollIntoView(true);",el)

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Firefox()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()
    browser.switch_to.alert.accept()
    time.sleep(1)
    x = int(browser.find_element(By.ID,"input_value").text)
    res = calc(x)
    answer = browser.find_element(By.ID,"answer")
    answer.send_keys(res)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    
   
    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
