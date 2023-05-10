import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

s = Service(executable_path='C:\chromedriver1\chromedriver.exe')
driver = webdriver.Chrome(service=s)

try:
    driver.maximize_window()
    driver.get("http://wms_ub1rds.berta.corp:8080/safena/start?lang=russian&theme=classic&app=wmsprod")
    # time.sleep(5)

    # Логін
    user_input = driver.find_element(By.ID, 'user')
    user_input.clear()
    user_input.send_keys("TEST3")
    # time.sleep(2)

    # Пароль
    pwd_input = driver.find_element(By.ID, 'pwd')
    pwd_input.clear()
    pwd_input.send_keys("TEST3")
    pwd_input.send_keys(Keys.ENTER)
    time.sleep(2)

    # Повідомленя про те що користувач вже залогінений
    warning_mess = driver.find_element(By.ID, 'SINGLE_LOGIN_WARNING-yes-btnInnerEl')
    if warning_mess:
        ActionChains(driver).click(warning_mess).perform()
        time.sleep(2)

    # Кнопка старт
    start_btm = driver.find_element(By.ID, 'button-1084-btnInnerEl')
    ActionChains(driver).click(start_btm).perform()
    time.sleep(2)

    # Кнопка Транспортние поручения
    menu_tr_btm = driver.find_element(By.ID, 'MENU-F_ZLECENIA_TRANSPORT_MENU-textEl')
    ActionChains(driver).click(menu_tr_btm).perform()
    time.sleep(2)

    # Кнопка Текущие транспортние поручения
    tr_btm = driver.find_element(By.ID, 'MENU-TR_TRANSPORTS_FAST_F-textEl')
    ActionChains(driver).click(tr_btm).perform()
    time.sleep(2)

    time.sleep(50)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
