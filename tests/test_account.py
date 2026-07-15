from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import (
    MainLocators,
    LoginLocators,
    AccountLocators,
)

from data import (
    VALID_EMAIL,
    VALID_PASSWORD,
    ACCOUNT_URL,
    BASE_URL
)

def test_open_personal_account(driver):

    driver.get(BASE_URL)

    driver.find_element(*MainLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_TITLE))

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON)
    )

    driver.find_element(*MainLocators.ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(AccountLocators.ORDER_HISTORY_LINK)
    )

    assert driver.current_url == ACCOUNT_URL

