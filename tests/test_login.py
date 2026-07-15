from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import (
    MainLocators,
    LoginLocators,
    ForgotPasswordLocators,
    RegisterLocators
)

from data import (
    BASE_URL,
    LOGIN_URL,
    REGISTER_URL,
    VALID_EMAIL,
    VALID_PASSWORD,
)


def test_login_with_login_button(driver):

    driver.get(BASE_URL)

    driver.find_element(*MainLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_TITLE)
    )

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON)
    )

    assert driver.current_url == BASE_URL


def test_login_with_account_button(driver):

    driver.get(BASE_URL)  

    driver.find_element(*MainLocators.ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_TITLE)
    )

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON)
    )

    assert driver.current_url == BASE_URL


def test_login_from_registration_form(driver):

    driver.get(REGISTER_URL)

    driver.find_element(*RegisterLocators.LOGIN_LINK).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_TITLE)
    )

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON)
    )

    assert driver.current_url == BASE_URL


def test_login_from_forgot_password_form(driver):

    driver.get(LOGIN_URL)

    driver.find_element(*LoginLocators.FORGOT_PASSWORD_LINK).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(ForgotPasswordLocators.RESET_PASSWORD_BUTTON)
    )

    driver.find_element(*ForgotPasswordLocators.LOGIN_LINK).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_TITLE)
    )

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON)
    )

    assert driver.current_url == BASE_URL

