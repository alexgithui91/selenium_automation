import os
import time
import pickle
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


sleep_time = 5

# Get Freshdesk username and password
load_dotenv()
username = os.environ.get("secretUser")
password = os.environ.get("secretPassword")


def main():
    """Connect to Freshdesk and export tickets data"""

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.get("https://dayliffservice.freshworks.com/")
    time.sleep(sleep_time)

    email_box = driver.find_element_by_id("username")
    email_box.send_keys(username)

    pwd_box = driver.find_element_by_id("password")
    pwd_box.send_keys(password)

    login_button = driver.find_element_by_class_name("css-o1ejds")
    login_button.click()
    time.sleep(sleep_time)

    cookies = pickle.load(open("cookie.pk1", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get("https://davisandshirtliff.freshdesk.com/helpdesk")
    time.sleep(sleep_time)

    driver.get("https://davisandshirtliff.freshdesk.com/a/tickets")

    time.sleep(sleep_time)

    export_btn = driver.find_element_by_xpath(
        "//*[@id='ember144']/div[2]/div/button[1]"
    )
    export_btn.click()
    time.sleep(sleep_time)

    element = driver.find_element_by_id(
        "select-all-tickets.export.ticketfields"
    )
    webdriver.ActionChains(driver).move_to_element(element).click(
        element
    ).perform()
    time.sleep(sleep_time)

    element = driver.find_element_by_xpath(
        "/html/body/div[8]/div[2]/div[4]/div/div/div/div/div/div[2]/div[4]/button[2]"
    )
    webdriver.ActionChains(driver).move_to_element(element).click(
        element
    ).perform()
    time.sleep(sleep_time)


if __name__ == "__main__":
    main()
