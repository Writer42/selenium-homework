from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
def scroll(el,driver):
    driver.execute_script("return arguments[0].scrollIntoView(true);",el)

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Firefox()
    browser.get(link)
    x = int(browser.find_element(By.ID,"input_value").text)
    res = calc(x)
    answer = browser.find_element(By.ID,"answer")
    scroll(answer,browser)
    answer.send_keys(res)
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    # sum = int(browser.find_element(value="num1").text) + \
    #     int(browser.find_element(value="num2").text)
    # select = Select(browser.find_element(by=By.TAG_NAME, value="select"))
    # select.select_by_value(str(sum))
    # # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
