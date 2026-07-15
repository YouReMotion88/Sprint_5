from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import MainLocators
from locators import LoginLocators

valid_email = 'bulat_gabaev_46_123@ya.ru'
valid_password = '123456'


def test_switch_to_buns_section(driver):

    driver.get("https://stellarburgers.education-services.ru/login")
 
    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(valid_email)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(valid_password)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()


    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON))

    assert driver.current_url == "https://stellarburgers.education-services.ru/"

    
    driver.find_element(*MainLocators.SAUCES_TAB).click()

    driver.find_element(*MainLocators.BUNS_TAB).click()

    assert "tab_tab_type_current" in driver.find_element(*MainLocators.BUNS_TAB).get_attribute("class")

    driver.quit()


def test_switch_to_sauces_section(driver):

    driver.get("https://stellarburgers.education-services.ru/login")

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(valid_email)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(valid_password)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

   
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON))

    assert driver.current_url == "https://stellarburgers.education-services.ru/"

    driver.find_element(*MainLocators.SAUCES_TAB).click()

    assert "tab_tab_type_current" in driver.find_element(*MainLocators.SAUCES_TAB).get_attribute("class")

    driver.quit()



def test_switch_to_fillings_section(driver):

    driver.get("https://stellarburgers.education-services.ru/login")

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(valid_email)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(valid_password)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()


    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON))

    assert driver.current_url == "https://stellarburgers.education-services.ru/"

    driver.find_element(*MainLocators.FILLINGS_TAB).click()

    assert "tab_tab_type_current" in driver.find_element(*MainLocators.FILLINGS_TAB).get_attribute("class")

    driver.quit()
