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

    attempt = driver.find_element_by_xpath(
        "/html/body/div[8]/div[2]/div[4]/div/div/div/div/div/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/div/div[5]/div"
    )
    webdriver.ActionChains(driver).move_to_element(attempt).click(
        attempt
    ).perform()
    time.sleep(sleep_time)

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
