from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    RESET_BUTTON = By.XPATH, '//button[text()="Восстановить"]'  # кнопка "Восстановить" на странице восстановления
    # пароля
    SAVE_BUTTON = By.XPATH, '//button[text()="Сохранить"]'  # кнопка "Сохранить" на странице восстановления пароля
    SHOW_PASSWORD_ICON = By.XPATH, '//div[contains(@class,"icon-action")]'  # иконка показа/скрытия пароля в поле
    # "Пароль"
