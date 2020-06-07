from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini a")
    # USER_ICON = (By.CLASS_NAME, "icon-user")

class LoginPageLocators():
    REGISTRATION_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")
    # USER_REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    # USER_REGISTRATION_PASSWORD_1 = (By.ID, "id_registration-password1")
    # USER_REGISTRATION_PASSWORD_2 = (By.ID, "id_registration-password2")
    # USER_REGISTRATION_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    INFO_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    INFO_MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success")

class BasketPageLocators(object):
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.content div#content_inner p")
    ITEM_IN_BASKET = (By.CSS_SELECTOR, "div.basket-items .row")