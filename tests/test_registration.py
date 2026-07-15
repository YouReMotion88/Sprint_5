from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import RegisterLocators
from locators import LoginLocators

from generators import (
    generate_email, 
    generate_password
)

from data import (
    REGISTER_URL, 
    LOGIN_URL,
    VALID_NAME
)


def test_success_registration(driver):

    email = generate_email()
    password = generate_password()

    driver.get(REGISTER_URL)

    driver.find_element(*RegisterLocators.NAME_INPUT).send_keys(VALID_NAME)
    driver.find_element(*RegisterLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterLocators.PASSWORD_INPUT).send_keys(password)

    driver.find_element(*RegisterLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_TITLE)
    )
    
    assert driver.current_url == LOGIN_URL


def test_registration_with_short_password(driver):

    driver.get(REGISTER_URL)

    driver.find_element(*RegisterLocators.NAME_INPUT).send_keys(VALID_NAME)
    driver.find_element(*RegisterLocators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegisterLocators.PASSWORD_INPUT).send_keys("12345")

    driver.find_element(*RegisterLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(RegisterLocators.PASSWORD_ERROR)
    )

    assert driver.find_element(*RegisterLocators.PASSWORD_ERROR).text == "Некорректный пароль"

