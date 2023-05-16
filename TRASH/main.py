import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json
from selenium.webdriver.chrome.options import Options

url = "https://www.work.ua/jobs-%D0%B1%D1%83%D1%85%D0%B3%D0%B0%D0%BB%D1%82%D0%B5%D1%80/"
chrome_path = '/Users/admin/Downloads/chromedriver'
s = Service(executable_path=chrome_path)
result = {}


# Прихований режим
# options = Options()
# options.add_argument("--headless=new")


def update_time() -> object:
    while True:
        driver = webdriver.Chrome(service=s)

        try:

            driver.maximize_window()
            driver.get(url)
            time1 = driver.find_elements(By.TAG_NAME, "h2")
            for n, name in enumerate(time1):
                print(n, name.text)
                result.update({n: name.text})
            print(result[0])

            # for n in time1:
            #     print(n.text)
            # # print(time1)
            with open("time.json", "w") as file:
                json.dump(result, file, indent=4, ensure_ascii=False)

        except Exception as ex:
            print(ex)

        finally:

            driver.close()
            driver.quit()
            time.sleep(100)

    return


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


if __name__ == "__main__":
    update_time()
