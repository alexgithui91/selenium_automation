from dotenv import load_dotenv
from selenium import webdriver

# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.keys import Keys


# print(driver.title)
# search_bar = driver.find_element_by_name("q")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)
# print(driver.current_url)


def run_bot():
    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://gmail.com")
    # driver.close()


if __name__ == "__main__":
    run_bot()
