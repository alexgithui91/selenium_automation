import os
import time
import pickle
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import Select
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

    select_all_tickets = driver.find_element_by_id(
        "select-all-tickets.export.ticketfields"
    )
    webdriver.ActionChains(driver).move_to_element(select_all_tickets).click(
        select_all_tickets
    ).perform()
    time.sleep(sleep_time)

    ticket_period = driver.find_element_by_xpath(
        "/html/body/div[8]/div[2]/div[4]/div/div/div/div/div/div[2]/div[2]/div[3]"
    )
    webdriver.ActionChains(driver).move_to_element(ticket_period).click(
        ticket_period
    ).perform()
    time.sleep(sleep_time)

    select_time_range = driver.find_element_by_xpath(
        "/html/body/div[8]/div[2]/div[4]/div/div/div/div/div/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/div/div[5]/div"
    )
    webdriver.ActionChains(driver).move_to_element(select_time_range).click(
        select_time_range
    ).perform()
    time.sleep(sleep_time)

    # Get from date
    click_date_from = driver.find_element_by_xpath(
        "/html/body/div[7]/div[2]/div/div[1]/button[1]"
    )

    for mnth in range(1, 7):
        webdriver.ActionChains(driver).move_to_element(click_date_from).click(
            click_date_from
        ).perform()

    first_day_of_month = driver.find_element_by_xpath(
        "/html/body/div[7]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]"
    )
    webdriver.ActionChains(driver).move_to_element(first_day_of_month).click(
        first_day_of_month
    ).perform()

    time.sleep(sleep_time)

    # Get to date
    click_date_to = driver.find_element_by_xpath(
        "/html/body/div[7]/div[2]/div/div[1]/button[2]"
    )
    for mnth in range(1, 7):
        webdriver.ActionChains(driver).move_to_element(click_date_to).click(
            click_date_to
        ).perform()

    # attempt_2 = driver.find_element_by_xpath(
    #     "/html/body/div[7]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]"
    # )
    # webdriver.ActionChains(driver).move_to_element(attempt_2).click(
    #     attempt_2
    # ).perform()
    # time.sleep(sleep_time)

    # Final Export button
    # element = driver.find_element_by_xpath(
    #     "/html/body/div[8]/div[2]/div[4]/div/div/div/div/div/div[2]/div[4]/button[2]"
    # )
    # webdriver.ActionChains(driver).move_to_element(element).click(
    #     element
    # ).perform()
    # time.sleep(sleep_time)


if __name__ == "__main__":
    main()
