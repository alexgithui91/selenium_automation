import os
import time
import pickle
from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver

# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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

    search_mail = driver.find_element_by_xpath(
        "/html/body/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/div/input"
    )
    search_mail.send_keys("support@freshdesk.com <support@freshdesk.com>")


if __name__ == "__main__":
    main()
