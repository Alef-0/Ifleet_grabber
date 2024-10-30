from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip as pc


import time
import os
from os import path

# Probably won't need to specify but let it here
# msedgewebdriver = "webdriver\\IEDriverServer32.exe"
# final_path = path.join(os.getcwd(), msedgewebdriver)
# webdriver.ie.driver_path = final_path

def setup_edge_ie_mode():
    ie_options = webdriver.IeOptions()
    # So many options to work °_°
    ie_options.ignore_protected_mode_settings = True
    ie_options.ignore_zoom_level = True
    # ie_options.require_window_focus = True
    # ie_options.native_events = False
    ie_options.ensure_clean_session = True
    # ie_options.persistent_hover = True
    # To use CreateProcess() with Internet Explorer 8 or higher, 
    # the value of registry setting in HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\Main\TabProcGrowth 
    # must be '0'; SO CREATE IT
    # ie_options.force_create_process_api = True
    # There also might be other problems, read it here https://www.selenium.dev/documentation/ie_driver_server/

    # Creating options
    driver = webdriver.Ie(options=ie_options)
    # driver.set_script_timeout(30)
    # driver.implicitly_wait(10)
    driver.set_page_load_timeout(5)

    return driver

def main():
    driver = setup_edge_ie_mode() # Get the driver
    waiter = WebDriverWait(driver, 10)
    try:
        driver.get("https://www.google.com.br")
        search_box = driver.find_element(By.NAME, "q")
        pc.copy("teste")
        search_box.send_keys(Keys.CONTROL, 'v')
        search_box.send_keys(Keys.ENTER)
        
        expected_url = "https://www.google.com.br/search"
        waiter.until(EC.url_contains(expected_url))
        driver.get("https://www.python.org")
        search_box = driver.find_element(By.NAME, "q")
        pc.copy("HELLO WORLD")
        search_box.send_keys(Keys.CONTROL, 'v')
        search_box.submit()

        time.sleep(5)

    except Exception as e:
        print("DEU ERRO")
        print(e)
    
    driver.quit()
    print("ACABOU")

from dotenv import load_dotenv
if __name__ == "__main__":
    load_dotenv()
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    print(login, password)
