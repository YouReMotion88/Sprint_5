import random

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import RegisterLocators
from locators import LoginLocators


def generate_email():
    return f"bulat_gabaev_46_{random.randint(100, 999)}@ya.ru"


def generate_password():
    return str(random.randint(100000, 999999999))


def test_success_registration(driver):

    email = generate_email()
    password = generate_password()

    driver.get("https://stellarburgers.education-services.ru/register")

    driver.find_element(*RegisterLocators.NAME_INPUT).send_keys("Цезарь")
    driver.find_element(*RegisterLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterLocators.PASSWORD_INPUT).send_keys(password)

    driver.find_element(*RegisterLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_TITLE))
    

    assert driver.current_url == "https://stellarburgers.education-services.ru/login"

    driver.quit()


def test_registration_with_short_password(driver):

    driver.get("https://stellarburgers.education-services.ru/register")

    driver.find_element(*RegisterLocators.NAME_INPUT).send_keys("Цезарь")
    driver.find_element(*RegisterLocators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegisterLocators.PASSWORD_INPUT).send_keys("12345")

    driver.find_element(*RegisterLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(RegisterLocators.PASSWORD_ERROR)
    )

    assert driver.find_element(*RegisterLocators.PASSWORD_ERROR).text == "Некорректный пароль"

    driver.quit()
