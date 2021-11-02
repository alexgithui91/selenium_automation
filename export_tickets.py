import os
import time
import pickle
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


sleep_time = 3

# Get Freshdesk username and password
load_dotenv()
username = os.environ.get("secretUser")
password = os.environ.get("secretPassword")


def main():
    """Connect to Freshdesk and export tickets data"""
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    try:
        driver.get("https://dayliffservice.freshworks.com/")
        time.sleep(sleep_time)

        email_box = driver.find_element_by_id("username")
        email_box.send_keys(username)

        pwd_box = driver.find_element_by_id("password")
        pwd_box.send_keys(password)

        login_button = driver.find_element_by_class_name("css-o1ejds")
        login_button.click()
        time.sleep(sleep_time)

        # pickle.dump(driver.get_cookies(), open("cookie.pk1", "wb"))
        cookies = pickle.load(open("cookie.pk1", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

    except TimeoutError as err:
        print("Error : ", err)


if __name__ == "__main__":
    main()
