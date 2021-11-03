import os
import time
import pickle
from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.firefox import GeckoDriverManager

# Wait time per request
sleep_time = 5

# Get Freshdesk username and password
load_dotenv()
username = os.environ.get("secretUser")
password = os.environ.get("secretPassword")


def main():
    pass


if __name__ == "__main__":
    main()
