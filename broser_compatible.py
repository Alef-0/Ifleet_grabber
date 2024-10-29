from selenium import webdriver
from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import os
from os import path

msedgewebdriver = "webdriver\\IEDriverServer32.exe"
final_path = path.join(os.getcwd(), msedgewebdriver)
# webdriver.ie.driver_path = final_path

def setup_edge_ie_mode():
    options = webdriver.IeOptions()
    
    # Para não dar problemas
    # options.add_additional_option("ie.edgechromium", True)
    # options.add_additional_option("ie.edgepath",final_path)
    options.ignore_zoom_level = True
    options.attach_to_edge_chrome = True
    # options.ignore_protected_mode_settings = True

    driver = webdriver.Ie(options=options)
    driver.set_page_load_timeout(30)
    return driver

def main():
    try:
        driver = setup_edge_ie_mode() # Get the driver
        driver.get("https://www.google.com.br")
        driver.get("https://www.python.org") # Navigate to your website
        
        print("CHEGOU AQUI")
        text = driver.find_element(By.ID, "id-search-field")
        text.send_keys("HELLO WORLD")
        text.send_keys(Keys.RETURN)
        time.sleep(5)
    except Exception as e:
        print(e)
    finally:
        driver.quit()

    print("ACABOU")


if __name__ == "__main__":
    main()
