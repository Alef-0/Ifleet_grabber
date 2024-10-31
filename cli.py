from browser import dashboard, elements_dictionary
from dotenv import load_dotenv
from os import getenv
from time import sleep
from selenium.webdriver.common.by import By

def login_service(dash : dashboard):
    # Acess the site
    dash = dashboard()
    dash.gotosite(getenv("ADDRESS"))
    # Wait until login is visible
    dash.wait_element(*elements_dictionary.login_text)
    dash.maximize()
    dash.search_box(*elements_dictionary.login_text, getenv("LOGIN"))
    dash.search_box(*elements_dictionary.password_text, getenv("PASSWORD"))
    dash.click_element(*elements_dictionary.login_button)
    # Wait until bar is visible?
    dash.wait_element(*elements_dictionary.taskbar)

def open_tabs(dash : dashboard):
    # Open armazenamento
    dash.click_element(*elements_dictionary.configurations)
    dash.click_element(*elements_dictionary.storage)
    # Open Backup
    dash.click_element(*elements_dictionary.menu)
    dash.click_element(*elements_dictionary.backup)
    
def setup_cameras(dash : dashboard):
    # dash.click_element(*elements_dictionary.tab_cameras)
    dash.click_element(*elements_dictionary.cam1_btn)
    dash.click_element(*elements_dictionary.cam2_btn)
    dash.click_element(*elements_dictionary.cam3_btn)
    dash.click_element(*elements_dictionary.cam4_btn)
    sleep(10)

def main():
    dash = dashboard()
    login_service(dash)
    # setup_cameras(dash)
    open_tabs(dash)

if __name__=='__main__':
    load_dotenv()
    main()