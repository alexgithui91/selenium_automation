import os
import time
import pickle
import webbrowser
from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager import firefox
from webdriver_manager.firefox import GeckoDriverManager

# Wait time per request
sleep_time = 5

# Get Freshdesk username and password
load_dotenv()
username = os.environ.get("email_user")
password = os.environ.get("email_pwd")


def main():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.get("https://outlook.office.com/mail/inbox")
    time.sleep(sleep_time)

    email_box = driver.find_element_by_id("i0116")
    email_box.send_keys(username)

    next_button = driver.find_element_by_id("idSIButton9")
    next_button.click()
    time.sleep(sleep_time)

    pwd_box = driver.find_element_by_id("i0118")
    pwd_box.send_keys(password)

    login_button = driver.find_element_by_id("idSIButton9")
    login_button.click()
    time.sleep(sleep_time)

    stay_signed_in = driver.find_element_by_id("idSIButton9")
    stay_signed_in.click()
    time.sleep(sleep_time)

    # pickle.dump(driver.get_cookies(), open("cookie2.pk1", "wb"))
    cookies = pickle.load(open("cookie2.pk1", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    # time.sleep(sleep_time)

    search_mail = driver.find_element_by_id("searchBoxColumnContainerId")

    webdriver.ActionChains(driver).move_to_element(search_mail).click(
        search_mail
    ).send_keys("Export of tickets created within").send_keys(
        Keys.RETURN
    ).perform()
    time.sleep(sleep_time)

    attempt = driver.find_element_by_id("All results")
    webdriver.ActionChains(driver).move_to_element(attempt).click(
        attempt
    ).send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN).perform()
    time.sleep(sleep_time)

    download_links = []
    elem = driver.find_elements_by_xpath("//*[@href]")
    for e in elem:
        if e.get_attribute("href").startswith(
            "https://eur01.safelinks.protection.outlook.com/"
        ):
            download_links.append(e.get_attribute("href"))

    webbrowser.open_link(download_links[1])


if __name__ == "__main__":
    main()
