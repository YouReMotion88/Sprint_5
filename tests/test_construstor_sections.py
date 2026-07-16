from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import MainLocators
from data import BASE_URL


def test_switch_to_buns_section(driver):

    driver.get(BASE_URL)

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(MainLocators.BUNS_TAB)
    )
   
    driver.find_element(*MainLocators.SAUCES_TAB).click()
    driver.find_element(*MainLocators.BUNS_TAB).click()

    assert "tab_tab_type_current" in driver.find_element(
        *MainLocators.BUNS_TAB
    ).get_attribute("class")


def test_switch_to_sauces_section(driver):

    driver.get(BASE_URL)

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(MainLocators.BUNS_TAB)
    )

    driver.find_element(*MainLocators.SAUCES_TAB).click()

    assert "tab_tab_type_current" in driver.find_element(
        *MainLocators.SAUCES_TAB
    ).get_attribute("class")


def test_switch_to_fillings_section(driver):

    driver.get(BASE_URL)

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(MainLocators.BUNS_TAB)
    )

    driver.find_element(*MainLocators.FILLINGS_TAB).click()

    assert "tab_tab_type_current" in driver.find_element(
        *MainLocators.FILLINGS_TAB
    ).get_attribute("class")
