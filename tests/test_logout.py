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
    LOGIN_URL
)


def test_logout_from_account(driver):

    driver.get(LOGIN_URL)

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

    driver.find_element(*AccountLocators.LOGOUT_BUTTON).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_TITLE)
    )

    assert driver.current_url == LOGIN_URL

   


