from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import RegisterLocators
from locators import MainLocators
from locators import LoginLocators
from locators import ForgotPasswordLocators

valid_email = 'bulat_gabaev_46_123@ya.ru'
valid_password = '123456'

def test_login_with_login_button(driver):

    driver.get('https://stellarburgers.education-services.ru/')

    driver.find_element(*MainLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_TITLE))

    assert driver.current_url == "https://stellarburgers.education-services.ru/login"

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(valid_email)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(valid_password)

    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON))

    assert driver.current_url == "https://stellarburgers.education-services.ru/"

    driver.quit()


def test_login_with_account_button(driver):

    driver.get('https://stellarburgers.education-services.ru/')  

    driver.find_element(*MainLocators.ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_TITLE))

    assert driver.current_url == "https://stellarburgers.education-services.ru/login"

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(valid_email)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(valid_password)

    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON))

    assert driver.current_url == "https://stellarburgers.education-services.ru/"

    driver.quit()


def test_login_from_registration_form(driver):

    driver.get("https://stellarburgers.education-services.ru/register")

    driver.find_element(*RegisterLocators.LOGIN_LINK).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_TITLE))

    assert driver.current_url == "https://stellarburgers.education-services.ru/login"

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(valid_email)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(valid_password)

    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON))

    assert driver.current_url == "https://stellarburgers.education-services.ru/"

    driver.quit()


def test_login_from_forgot_password_form(driver):

    driver.get("https://stellarburgers.education-services.ru/login")

    driver.find_element(*LoginLocators.FORGOT_PASSWORD_LINK).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ForgotPasswordLocators.RESET_PASSWORD_BUTTON))

    assert driver.current_url == "https://stellarburgers.education-services.ru/forgot-password"
    
    driver.find_element(*ForgotPasswordLocators.LOGIN_LINK).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_TITLE))

    assert driver.current_url == "https://stellarburgers.education-services.ru/login"

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(valid_email)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(valid_password)

    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON))

    assert driver.current_url == "https://stellarburgers.education-services.ru/"

    driver.quit()
