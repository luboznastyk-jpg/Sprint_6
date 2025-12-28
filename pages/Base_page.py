from selenium import webdriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Base_Page:
    item = ['локатор']
    main_title = ['локатор']
    site_logo = ['локатор']
    settlement = ['локатор']

    def __init__(self, driver):
        self.driver = driver

    def check_settlement_name(self):
        actually_settlement = self.driver.find_element(*self.main_title).text
        expected_settlement = 'населённый пункт'
        assert actually_settlement == expected_settlement

    def select_settlement(self):
        self.driver.find_element(*self.item).click()

    def set_settlement(self):
        self.driver.find_element(*self.settlement).send_keys('населённый пункт')

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.site_logo))
