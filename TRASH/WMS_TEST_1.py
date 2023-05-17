import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json
from selenium.webdriver.chrome.options import Options

url = "http://wms_ub1rds.berta.corp:8080/safena/start?lang=russian&theme=classic&app=wmsprod"
chrome_path = '/Users/admin/Downloads/chromedriver'
# chrome_path = 'C:\chromedriver1\chromedriver.exe'
s = Service(executable_path=chrome_path)


# Прихований режим
# options = Options()
# options.add_argument("--headless=new")

result = {}
def wms_login():

    driver = webdriver.Chrome(service=s)

    try:
        driver.maximize_window()
        driver.get(url)

        # Логін
        user_input = driver.find_element(By.ID, 'user')
        user_input.clear()
        user_input.send_keys("TEST3")

        # Пароль
        pwd_input = driver.find_element(By.ID, 'pwd')
        pwd_input.clear()
        pwd_input.send_keys("TEST3")
        pwd_input.send_keys(Keys.ENTER)
        time.sleep(2)
        try:
            # Повідомленя про те що користувач вже залогінений
            warning_mess = driver.find_element(By.ID, 'SINGLE_LOGIN_WARNING-yes-btnInnerEl')
            if warning_mess:
                ActionChains(driver).click(warning_mess).perform()
                time.sleep(2)
        except Exception as ex:
            print(ex)


    except Exception as ex:
        print(ex)

    finally:
        print("Sucesfull login")
        return driver


def wms_tp(driver) -> object:

    try:
        # Кнопка старт
        start_btm = driver.find_element(By.ID, 'button-1084-btnInnerEl')
        ActionChains(driver).click(start_btm).perform()
        # time.sleep(2)

        # Кнопка Транспортние поручения
        menu_tr_btm = driver.find_element(By.ID, 'MENU-F_ZLECENIA_TRANSPORT_MENU-textEl')
        ActionChains(driver).click(menu_tr_btm).perform()
        time.sleep(2)

        # Кнопка Текущие транспортние поручения
        tr_btm = driver.find_element(By.ID, 'MENU-TR_TRANSPORTS_FAST_F-textEl')
        ActionChains(driver).click(tr_btm).perform()
        time.sleep(1)

        # Pole TIP POROCHENIYA TR_TRANSPORTS_FAST_F-0-F_F_TRANSPORT_TYPE-inputEl
        pole_type_tp = driver.find_element(By.ID, 'TR_TRANSPORTS_FAST_F-0-F_F_TRANSPORT_TYPE-inputEl')
        ActionChains(driver).click(pole_type_tp).perform()
        # pole_type_tp.clear()
        pole_type_tp.send_keys("Відправка")

        # Knopka Search TR_TRANSPORTS_FAST_F-0-_0_GRID-PAGING_SEARCH-btnIconEl
        search_btm = driver.find_element(By.ID, 'TR_TRANSPORTS_FAST_F-0-_0_GRID-PAGING_SEARCH-btnIconEl')
        ActionChains(driver).click(search_btm).perform()
        time.sleep(2)

        # progressbar - 1120 - bar
        kilkist_vidpravok = driver.find_element(By.ID, 'progressbar-1119-bar').text
        kilkist = f"Кількість відправок: {kilkist_vidpravok[17:]}"
        print(kilkist)




    except Exception as ex:
        print(ex)

    finally:

        print("TP Succesfull")
        #kilkist_popovn = f"Кількість відправок: {kilkist_vidpravok[17:]}"
        #result.update({"Кількість відправок": kilkist_vidpravok[17:]})
        #print(result)
        with open("kilkist.json", "w") as file:
            json.dump(kilkist, file, indent=4, ensure_ascii=False)

        driver.close()
        driver.quit()


def wms_popovn(driver) -> object:
    global kilkist_popovn
    try:
        # Кнопка старт
        start_btm = driver.find_element(By.ID, 'button-1084-btnInnerEl')
        # start_btm.click()
        ActionChains(driver).click(start_btm).perform()
        # time.sleep(2)

        # Кнопка Транспортние поручения
        menu_tr_btm = driver.find_element(By.ID, 'MENU-F_ZLECENIA_TRANSPORT_MENU-textEl')
        # menu_tr_btm.click()
        ActionChains(driver).click(menu_tr_btm).perform()
        time.sleep(2)

        # Кнопка Текущие транспортние поручения
        tr_btm = driver.find_element(By.ID, 'MENU-TR_TRANSPORTS_FAST_F-textEl')
        # tr_btm.click()
        ActionChains(driver).click(tr_btm).perform()
        time.sleep(1)

        # Pole TIP POROCHENIYA TR_TRANSPORTS_FAST_F-0-F_F_TRANSPORT_TYPE-inputEl
        pole_type_tp = driver.find_element(By.ID, 'TR_TRANSPORTS_FAST_F-0-F_F_TRANSPORT_TYPE-inputEl')
        ActionChains(driver).click(pole_type_tp).perform()
        # pole_type_tp.clear()
        pole_type_tp.send_keys("Поповнення збору")

        # Knopka Search TR_TRANSPORTS_FAST_F-0-_0_GRID-PAGING_SEARCH-btnIconEl
        search_btm = driver.find_element(By.ID, 'TR_TRANSPORTS_FAST_F-0-_0_GRID-PAGING_SEARCH-btnIconEl')
        ActionChains(driver).click(search_btm).perform()
        time.sleep(2)

        # progressbar - 1120 - bar
        kilkist_popovn = driver.find_element(By.ID, 'progressbar-1119-bar').text
        print(kilkist_popovn == False)
        kilkist_popovn = f"Кількість поповнень: {kilkist_popovn[17:]}"
        print(kilkist_popovn)

    except Exception as ex:
        print(ex)

    finally:

        print("TP Succesfull")
        with open("../app/kilkist_popovn.json", "w") as file:
            if kilkist_popovn:
                json.dump(kilkist_popovn, file, indent=4, ensure_ascii=False)

        driver.close()
        driver.quit()


if __name__ == "__main__":
    wms_tp(wms_login())