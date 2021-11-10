import os
import time
import pickle
from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

# Wait time per request
sleep_time = 5

# Get Freshdesk username and password
load_dotenv()
username = os.environ.get("fd_user")
password = os.environ.get("fd_pwd")

# Weeks dict
weeks_dict = {
    "1": [1, 8, 15, 22, 29],
    "2": [2, 9, 16, 23, 30],
    "3": [3, 10, 17, 24, 31],
    "4": [4, 11, 18, 25],
    "5": [5, 12, 19, 26],
    "6": [6, 13, 20, 27],
    "7": [7, 14, 21, 28],
}

# Get date
today = datetime.today().day
month = datetime.today().month
week = 0

for key, value in weeks_dict.items():
    if today in value:
        week = key

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


def run_exporter():
    """Connect to Freshdesk and export tickets data"""

    def login():

        driver.get("https://dayliffservice.freshworks.com/")
        time.sleep(sleep_time)

        email_box = driver.find_element_by_id("username")
        email_box.send_keys(username)

        pwd_box = driver.find_element_by_id("password")
        pwd_box.send_keys(password)

        login_button = driver.find_element_by_class_name("css-o1ejds")
        login_button.click()
        time.sleep(sleep_time)

        # pickle.dump(driver.get_cookies(), open("cookie.pkl", "wb"))
        cookies = pickle.load(open("cookie.pk1", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

    def navigate_to_tickets():

        driver.get("https://davisandshirtliff.freshdesk.com/helpdesk")
        time.sleep(sleep_time)

        driver.get("https://davisandshirtliff.freshdesk.com/a/tickets")

        time.sleep(sleep_time)

    def select_export_criteria():
        date_pick = driver.find_element_by_class_name(
            "ember-power-select-selected-item"
        )
        webdriver.ActionChains(driver).move_to_element(date_pick).click(
            date_pick
        ).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(
            Keys.ARROW_DOWN
        ).send_keys(
            Keys.ARROW_DOWN
        ).send_keys(
            Keys.ARROW_DOWN
        ).send_keys(
            Keys.ARROW_DOWN
        ).send_keys(
            Keys.ARROW_DOWN
        ).send_keys(
            Keys.ARROW_DOWN
        ).send_keys(
            Keys.RETURN
        ).perform()
        time.sleep(sleep_time)

        # Get from date
        click_date_from = driver.find_element_by_xpath(
            "/html/body/div[7]/div[2]/div/div[1]/button[1]"
        )

        for mnth in range(month, 1, -1):
            webdriver.ActionChains(driver).move_to_element(
                click_date_from
            ).click(click_date_from).perform()

        first_day_of_month = driver.find_element_by_xpath(
            "/html/body/div[7]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]"
        )
        webdriver.ActionChains(driver).move_to_element(
            first_day_of_month
        ).click(first_day_of_month).perform()

        # Get to date
        click_date_to = driver.find_element_by_xpath(
            "/html/body/div[7]/div[2]/div/div[1]/button[2]"
        )
        for mnth in range(1, month):
            webdriver.ActionChains(driver).move_to_element(
                click_date_to
            ).click(click_date_to).perform()

        last_day_of_month = driver.find_element_by_xpath(
            "/html/body/div[7]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/button["
            + week
            + "]"
        )
        webdriver.ActionChains(driver).move_to_element(
            last_day_of_month
        ).click(last_day_of_month).perform()

        update_time = driver.find_element_by_xpath(
            "/html/body/div[7]/div[2]/div/div[2]/button[2]"
        )
        update_time.click()

        apply_update_time = driver.find_element_by_xpath(
            "/html/body/div[8]/div[2]/div[3]/div[2]/div/div[2]/div/div/div/div[3]/button"
        )
        apply_update_time.click()

        export_btn = driver.find_element_by_xpath(
            "//*[@id='ember144']/div[2]/div/button[1]"
        )
        export_btn.click()
        time.sleep(sleep_time)

        select_all_tickets = driver.find_element_by_id(
            "select-all-tickets.export.ticketfields"
        )
        webdriver.ActionChains(driver).move_to_element(
            select_all_tickets
        ).click(select_all_tickets).perform()
        time.sleep(sleep_time)

    def export_tickets():
        # Final Export button
        export_data = driver.find_element_by_xpath(
            "/html/body/div[8]/div[2]/div[4]/div/div/div/div/div/div[2]/div[4]/button[2]"
        )
        webdriver.ActionChains(driver).move_to_element(export_data).click(
            export_data
        ).perform()
        time.sleep(sleep_time)

    # Login in to freshdesk
    login()
    # Navigate to all tickets
    navigate_to_tickets()
    # Select time period of export
    select_export_criteria()
    # Export tickets
    export_tickets()


if __name__ == "__main__":
    run_exporter()
