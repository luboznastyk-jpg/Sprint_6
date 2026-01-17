import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from pages.Main_page import MainPage
from url import Urls


@pytest.fixture(scope="session")
def driver():
    service = Service()
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()

