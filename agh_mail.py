
from typing import List

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from time import sleep

BASE_URL = "https://poczta.agh.edu.pl"
CHROME_PROFILE_PATH = "C:\\Users\\subza\\AppData\\Local\\Google\\Chrome\\User Data\\Default"


def _get_web_driver() -> WebDriver:
    WINDOW_SIZE = "1920,1080"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    # chrome_options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")

    return webdriver.Chrome(
        executable_path="drivers/chromedriver.exe", options=chrome_options)


class AghMail:

    def __init__(self, uname, pwd):
        self.uname = uname
        self.pwd = pwd

    def get_unread_adresses(self) -> List:
        driver = _get_web_driver()
        driver.get(BASE_URL)
        assert "poczta.agh.edu.pl" in driver.title

        name_field = driver.find_element_by_id("rcmloginuser")
        pwd_field = driver.find_element_by_id("rcmloginpwd")
        submit_button = driver.find_element_by_id("rcmloginsubmit")

        sleep(3)
        name_field.send_keys(self.uname)
        pwd_field.send_keys(self.pwd)
        submit_button.send_keys(Keys.RETURN)

        assert f"Odebrane" in driver.title

        elements = driver.find_elements_by_css_selector(
            ".message.unread .subject .adr span")


        def map_element_to_email(el: WebElement):
            return el.get_property("title")

        emails = list(map(map_element_to_email, elements))

        driver.quit()

        return emails

