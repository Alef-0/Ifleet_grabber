from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip as pc
from selenium.webdriver.common.action_chains import ActionChains

import time
import os
from os import path

class elements_dictionary:
    login_text = (By.NAME, "loginUsername-inputEl")
    password_text = (By.NAME, "loginPassword-inputEl")
    login_button = (By.ID, "loginButton-btnIconEl")
    taskbar = (By.ID, "taskbar-1031-innerCt")
    # Para abrir outras abas
    configurations = (By.ID, "button-1030-btnInnerEl")
    storage = (By.ID, "menuitem-1025-itemEl")
    menu = (By.ID, "button-1042-btnIconEl")
    backup = (By.XPATH, "//*[text()='Backup']") # Não tem botão, é só um local
    # Aba de cameras
    tab_cameras = (By.ID, "splitbutton-1260")
    cam1_btn = (By.ID, "splitbutton-1274")
    cam2_btn = (By.ID, "splitbutton-1275")
    cam3_btn = (By.ID, "splitbutton-1276")
    cam4_btn = (By.ID, "splitbutton-1277")


class dashboard():
    def __init__(self):
        ie_options = webdriver.IeOptions()

        # So many options to work °_°
        ie_options.ignore_protected_mode_settings = True
        ie_options.ignore_zoom_level = True
        ie_options.ensure_clean_session = True
        # ie_options.persistent_hover = True
        # ie_options.require_window_focus = True
        # ie_options.native_events = False
        # ie_options.force_create_process_api = True
        
        # To use CreateProcess() with Internet Explorer 8 or higher, 
        # the value of registry setting in HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\Main\TabProcGrowth 
        # must be '0'; SO CREATE IT
        # There also might be other problems, read it here https://www.selenium.dev/documentation/ie_driver_server/
        # NECESSARIO PARA TUDO FUNCIONAR

        # Creating options
        self.driver = webdriver.Ie(options=ie_options)
        self.driver.set_page_load_timeout(60)
        self.waiter : WebDriverWait = WebDriverWait(self.driver, 60)

    def gotosite(self, site): self.driver.get(site)
    
    def maximize(self): self.driver.maximize_window()

    def wait_element(self, by_search, name):
        self.waiter.until(
             EC.visibility_of_element_located((by_search, name))
        )

    def search_box(self, by_search, name, text):
        self.wait_element(by_search, name)
        pc.copy(text)
        print("VALUE ON COPY: ", text)
        el = self.driver.find_element(by_search, name)
        el.clear()
        el.send_keys(Keys.CONTROL + 'v')
            

    def click_element(self, by_search, name):
        self.wait_element(by_search, name)
        el = self.driver.find_element(by_search, name)
        ActionChains(self.driver).move_to_element(el).click().perform()