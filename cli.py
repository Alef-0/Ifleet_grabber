from browser import dashboard, elements_dictionary
from dotenv import load_dotenv
from os import getenv
from time import sleep
from selenium.webdriver.common.by import By

def access_dashboard(dash : dashboard):
    # Acess the site
    dash = dashboard()
    dash.gotosite(getenv("ADDRESS"))
    # Wait until login is visible
    dash.wait_element(*elements_dictionary.login_text)
    dash.maximize()
    dash.search_box(*elements_dictionary.login_text, getenv("USERNAME"))
    dash.search_box(*elements_dictionary.password_text, getenv("PASSWORD"))
    dash.click_element(*elements_dictionary.login_button)
    # Wait until bar is visible?
    dash.wait_element(*elements_dictionary.taskbar)
    # Open armazenamento
    dash.click_element(*elements_dictionary.configurations)
    dash.click_element(*elements_dictionary.storage)
    # Open Backup
    dash.click_element(*elements_dictionary.menu)
    dash.click_element(*elements_dictionary.backup)
    

def main():
    dash = dashboard()
    access_dashboard(dash)

if __name__=='__main__':
    load_dotenv()
    main()