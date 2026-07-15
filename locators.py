from selenium.webdriver.common.by import By


class RegisterLocators:

    # Поле "Имя"
    NAME_INPUT = (By.XPATH, "//fieldset[1]//input")

    # Поле "Email"
    EMAIL_INPUT = (By.XPATH, "//fieldset[2]//input")

    # Поле "Пароль"
    PASSWORD_INPUT = (By.XPATH, "//fieldset[3]//input")

    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")

    # Сообщение "Некорректный пароль"
    PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']")

    # Ссылка Войти под формой регистрации
    LOGIN_LINK = (By.CSS_SELECTOR, 'a[href="/login"]')



class MainLocators:
   
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") 
    
    # Кнопка "Личный кабинет"
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")

    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[p[text()='Конструктор']]")

    # Кнопка "Оформить заказ"
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Раздел "Булки"
    BUNS_TAB = (By.XPATH, "//div[span[text()='Булки']]")
    
    # Раздел "Соусы"
    SAUCES_TAB = (By.XPATH, "//div[span[text()='Соусы']]")

    # Раздел "Начинки"
    FILLINGS_TAB = (By.XPATH, "//div[span[text()='Начинки']]")


class LoginLocators:    
    
    # Поле "Email"
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    
    # Поле "Пароль"
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    
    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")

    # Ссылка "Восстановить пароль"
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

    # Заголовок страницы "Вход"
    LOGIN_TITLE = (By.XPATH, ".//h2[text()='Вход']")


class ForgotPasswordLocators:

    # Кнопка "Восстановить"
    RESET_PASSWORD_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

    # Ссылка "Войти"
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class AccountLocators:

    # Ссылка "История заказов"
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")

    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    
    # Логотип Stellar Burgers
    LOGO = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]/a")

    # Кнопка "Выход"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    
