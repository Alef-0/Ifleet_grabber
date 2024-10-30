import browser
from dotenv import load_dotenv
from os import getenv
from time import sleep
from selenium.webdriver.common.by import By

def access_dashboard(dash : browser.dashboard):
    # Acess the site
    dash = browser.dashboard()
    dash.gotosite(getenv("ADDRESS"))
    # Wait until login is visible
    dash.wait_element(By.NAME, "loginUsername-inputEl")
    dash.maximize()
    dash.search_box(By.NAME, "loginUsername-inputEl", getenv("LOGIN"))
    dash.search_box(By.NAME, "loginPassword-inputEl", getenv("PASSWORD"))
    dash.click_element(By.ID, "loginButton-btnIconEl")
    # Wait until bar is visible?
    dash.wait_element(By.ID, "taskbar-1031-innerCt")
    # Open armazenamento
    dash.click_element(By.ID, "button-1030-btnInnerEl")
    dash.click_element(By.ID, "menuitem-1025-itemEl")
    # Open Backup
    dash.click_element(By.ID, "button-1042-btnIconEl")
    dash.click_element(By.XPATH, "//*[text()='Backup']")
    

def main():
    dash = browser.dashboard()
    access_dashboard(dash)

if __name__=='__main__':
    load_dotenv()
    main()