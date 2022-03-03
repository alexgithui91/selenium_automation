import time
import os
from dotenv import load_dotenv
from selenium import webdriver


def run_bot():
    # Get Email user name and password
    load_dotenv()
    user_name = os.environ.get("user_email")
    user_pwd = os.environ.get("user_pwd")

    driver = webdriver.Chrome("chromedriver")
    driver.maximize_window()
    driver.get("https://www.hackerrank.com/auth/login")

    email_input = driver.find_element_by_id("input-1")
    email_input.send_keys(user_name)

    password_input = driver.find_element_by_id("input-2")
    password_input.send_keys(user_pwd)

    log_in = driver.find_element_by_xpath(
        "//*[@id='tab-1-content-1']/div[1]/form/div[4]/button"
    )
    log_in.click()

    time.sleep(10)

    driver.close()


if __name__ == "__main__":
    run_bot()
