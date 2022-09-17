URL = "https://orteil.dashnet.org/experiments/cookie/"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = FILE PATH
s = Service(chrome_driver_path)

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get(URL)

cookie = driver.find_element(By.ID, "cookie")

store = driver.find_elements(By.CSS_SELECTOR, "#store b")

timeout = time.time() + 12
five_min = time.time() + 60*5

while True:
    cookie.click()

    #Every 5 minutes
    if time.time() > timeout:

        # Get current cookie amount
        money = driver.find_element(By.ID, "money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_amount = int(money)


       
        store = driver.find_elements(By.CSS_SELECTOR, "#store b")
        for upgrade in store[::-1]:
            upgrade_text = upgrade.text
            if upgrade_text != "":
                detail = upgrade_text.split("-")
                product = detail[0].strip()
                cost = detail[-1].strip()
                if "," in cost:
                    cost = cost.replace(",", "")
                cost_int = int(cost)
                if cookie_amount >= cost_int:
                    driver.find_element(By.ID, f"buy{product}").click()
                    break
                else:
                    continue

        timeout = time.time() + 12

    if time.time() > five_min:
        cookie_per = driver.find_element(By.ID, "cps").text
        print(cookie_per)
        break
