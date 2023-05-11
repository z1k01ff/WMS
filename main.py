from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
import json
from selenium.webdriver.chrome.options import Options



def update_time() -> object:
    driver_path = '/Users/admin/Downloads/chromedriver'  # mac driver
    s = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=s)
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')

    global time1
    try:
        url = "https://time.is/ru/"
        driver.maximize_window()
        time1 = driver.find_element(By.ID, "clock").text

        # time.sleep(5)

    except Exception as ex:
        print(ex)

    finally:
        with open("time.json", "w") as file:
            json.dump(time1, file, indent=4, ensure_ascii=False)

        print(time1)

        driver.close()
        driver.quit()

    return time1


def main():
    pass
    # print(update_time())
    # print(update_time())


# if __name__ == '__main__':
#     pass


