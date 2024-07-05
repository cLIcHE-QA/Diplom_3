from selenium.webdriver.common.by import By


class BasePageLocators:
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'  # поле "Email" на странице логина и
    # странице восстановления пароля
    INPUT_PASSWORD = By.XPATH, '//input[@type="password"]'  # поле "Пароль" на странице логина и странице
    # восстановления пароля
    INPUT_PASSWORD_ACTIVE = By.CSS_SELECTOR, '.input.input_status_active'  # поле "Пароль" в активном состоянии
    CLOSE_BUTTON = By.XPATH, '//button[contains(@class,"close")]'  # крестик закрытия всплывающего окна "Детали
    # ингредиента", номера заказа, деталь заказа
