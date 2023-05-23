import time
import asyncio
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json
from selenium.webdriver.chrome.options import Options
from selenium_to_text import selenium_to_json

url = "http://wms_ub1rds.berta.corp:8080/safena/start?lang=russian&theme=classic&app=wmsprod"
chrome_path = '/Users/admin/Downloads/chromedriver'
# chrome_path = 'C:\chromedriver1\chromedriver.exe'
s = Service(executable_path=chrome_path)


# async def fun1():
#     await asyncio.sleep(60)
#     print('fun1 завершена')
#     return "fun1"
#
#
# async def fun2():
#     await asyncio.sleep(60)
#     print('fun2 завершена')
#     return "fun2"
#

# async def main():
#     task1 = asyncio.create_task(fun1())
#     task2 = asyncio.create_task(fun2())
#
#     await task1
#     await task2
#
#
# asyncio.run(main())


def driver():
    driver = webdriver.Chrome(service=s)
    try:
        driver.maximize_window()
        driver.get(url)
        print("Driver initialised")
        # await asyncio.sleep(10)

    except Exception as ex:
        print(ex)

    finally:
        print("Driver reinicialised")
        return driver


test = driver()


async def wms_login(driver=test):
    # driver = webdriver.Chrome(service=s)

    try:
        driver.maximize_window()
        driver.get(url)

        # Логін
        # user_input = driver.find_element(By.ID, 'user').clear() poprobuvaty!!!!!!!
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
            # Повідомлення про те що користувач вже залогінений
            warning_mess = driver.find_element(By.ID, 'SINGLE_LOGIN_WARNING-yes-btnInnerEl')
            if warning_mess:
                ActionChains(driver).click(warning_mess).perform()
                time.sleep(2)
        except Exception as ex:
            print(ex)

        await asyncio.sleep(10)
    except Exception as ex:
        print(ex)

    finally:
        print("Sucesfull login")
        # return driver


async def wms_tp_fast(driver=test):
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

    except Exception as ex:
        print(ex)

    finally:
        print("TP successful opening")


def wms_vidpravka(driver) -> object:
    try:

        # Pole TIP POROCHENIYA
        pole_type_tp = driver.find_element(By.ID, 'TR_TRANSPORTS_FAST_F-0-F_F_TRANSPORT_TYPE-inputEl')
        ActionChains(driver).click(pole_type_tp).perform()
        pole_type_tp.clear()
        pole_type_tp.send_keys("Відправка")

        # Knopka Search
        search_btm = driver.find_element(By.ID, 'TR_TRANSPORTS_FAST_F-0-_0_GRID-PAGING_SEARCH-btnIconEl')
        ActionChains(driver).click(search_btm).perform()
        time.sleep(2)

        # Poshuk vsih elementiv po uchastku
        tp_pole_uchastok = driver.find_elements(By.XPATH,
                                                "//td[@class='x-grid-cell x-grid-td x-grid-cell-qgridcolumn-1143']")
        selenium_to_json(tp_pole_uchastok, "kilkist_vidpravok")

    except Exception as ex:
        print(ex)

    finally:
        print("TP vidpravka Succesfull")


async def wms_popovn(driver=test) -> object:
    global kilkist_popovn
    try:

        # Pole TIP POROCHENIYA TR_TRANSPORTS_FAST_F-0-F_F_TRANSPORT_TYPE-inputEl
        pole_type_tp = driver.find_element(By.ID, 'TR_TRANSPORTS_FAST_F-0-F_F_TRANSPORT_TYPE-inputEl')
        ActionChains(driver).click(pole_type_tp).perform()
        pole_type_tp.clear()
        pole_type_tp.send_keys("Поповнення збору")

        # Knopka Search TR_TRANSPORTS_FAST_F-0-_0_GRID-PAGING_SEARCH-btnIconEl
        search_btm = driver.find_element(By.ID, 'TR_TRANSPORTS_FAST_F-0-_0_GRID-PAGING_SEARCH-btnIconEl')
        ActionChains(driver).click(search_btm).perform()
        time.sleep(2)

        tp_uchastok = driver.find_elements(By.XPATH,
                                           "//td[@class='x-grid-cell x-grid-td x-grid-cell-qgridcolumn-1143']")
        # time.sleep(5)

        selenium_to_json(tp_uchastok, "kilkist_popovnen")

    except Exception as ex:
        print(ex)

    finally:
        print("TP popovnenya Succesfull")


def wms_exit(driver=test):
    driver.close()
    driver.quit()

async def main():
    task1 = asyncio.create_task(wms_login())
    task2 = asyncio.create_task(wms_tp_fast())
    task3 = asyncio.create_task(wms_popovn())

    await task1
    await task2
    await task3
async def loop():
    while True:
        asyncio.run(main())
        await asyncio.sleep(20)
        await loop()

async def main2():




if __name__ == "__main__":
    loop()


# можливо потрібно буде об'єднати в одну ф-цію через driver!!!!!
