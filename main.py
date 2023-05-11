import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json
from selenium.webdriver.chrome.options import Options

url = "https://time.is/ru/"
chrome_path = '/Users/admin/Downloads/chromedriver'
s = Service(executable_path=chrome_path)

# Прихований режим
options = Options()
options.add_argument("--headless=new")


def update_time() -> object:
    driver = webdriver.Chrome(service=s, options=options)

    global time1
    try:
        driver.maximize_window()
        driver.get(url)
        time1 = driver.find_element(By.ID, "clock").text


    except Exception as ex:
        print(ex)

    finally:
        with open("time.json", "w") as file:
            json.dump(time1, file, indent=4, ensure_ascii=False)

        print(time1)

        driver.close()
        driver.quit()

    return time1


def update_date() -> object:
    driver = webdriver.Chrome(service=s)
    global date1
    try:
        driver.maximize_window()
        driver.get(url)
        date1 = driver.find_element(By.ID, "dd").text


    except Exception as ex:
        print(ex)

    finally:
        with open("date.json", "w") as file:
            json.dump(date1, file, indent=4, ensure_ascii=False)

        print(date1)

        driver.close()
        driver.quit()

    return date1
