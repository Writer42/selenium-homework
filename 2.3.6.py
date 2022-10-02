from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import os

curr_dir = os.path.abspath(os.path.dirname(__file__))

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
def scroll(el,driver):
    driver.execute_script("return arguments[0].scrollIntoView(true);",el)

try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Firefox()
    browser.get(link)
    WebDriverWait(browser,15).until(EC.text_to_be_present_in_element((By.ID,"price"), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()    
    x = int(browser.find_element(By.ID,"input_value").text)
    res = calc(x)
    answer = browser.find_element(By.ID,"answer")
    answer.send_keys(res)
    button = browser.find_element(By.ID, "solve")
    scroll(button, browser)
    button.click()

    
   
    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
