from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import MainLocators
from locators import LoginLocators
from locators import AccountLocators

valid_email = 'bulat_gabaev_46_123@ya.ru'
valid_password = '123456'

def test_open_personal_account(driver):

    driver.get('https://stellarburgers.education-services.ru/')

    driver.find_element(*MainLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_TITLE))

    assert driver.current_url == "https://stellarburgers.education-services.ru/login"

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(valid_email)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(valid_password)

    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON))

    assert driver.current_url == "https://stellarburgers.education-services.ru/" 

    driver.find_element(*MainLocators.ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AccountLocators.ORDER_HISTORY_LINK))

    assert driver.current_url == 'https://stellarburgers.education-services.ru/account/profile'

    driver.quit()
