from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Call a taxi']")
    SUPPORTIVE_BUTTON_LOCATOR = (By.XPATH, "//div[contains(@class,'tcard')][.//div[text()='Supportive']]")
    PHONE_FIELD_LOCATOR = (By.XPATH, "//div[contains(@class,'np-text') and text()='Phone number']")
    PHONE_INPUT_LOCATOR = (By.ID, "phone")
    NEXT_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Next']")
    SMS_CODE_INPUT_LOCATOR = (By.ID, "code")
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Confirm']")
    PAYMENT_METHOD_LOCATOR = (By.XPATH, "//div[contains(@class,'pp-button')][.//div[text()='Payment method']]")
    ADD_CARD_LOCATOR = (By.XPATH, "//div[contains(@class,'pp-row')][.//div[text()='Add card']]")
    CARD_NUMBER_LOCATOR = (By.ID, "number")
    CARD_CVV_LOCATOR = (By.CSS_SELECTOR, "input.card-input[name='code']")
    LINK_BUTTON_LOCATOR = (By.XPATH, "//button[contains(text(),'Link')]")
    PAYMENT_TEXT_LOCATOR = (By.XPATH, "//div[text()='Card']")






    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def click_call_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.CALL_TAXI_BUTTON_LOCATOR)).click()

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_call_taxi_button()

    def get_from_location(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_attribute('value')

    def get_to_location(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_attribute('value')

    def click_supportive_button(self):
        self.driver.find_element(
            *self.SUPPORTIVE_BUTTON_LOCATOR
        ).click()

    def is_supportive_selected(self):
        supportive_button = self.driver.find_element(
            *self.SUPPORTIVE_BUTTON_LOCATOR
        )
        return "active" in supportive_button.get_attribute("class")

    def click_phone_field(self):
        self.driver.find_element(*self.PHONE_FIELD_LOCATOR).click()

    def enter_phone_number(self, phone):
        self.driver.find_element(*self.PHONE_INPUT_LOCATOR).send_keys(phone)

    def click_next(self):
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()

    def enter_sms_code(self, code):
        self.driver.find_element(*self.SMS_CODE_INPUT_LOCATOR).send_keys(code)

    def click_confirm(self):
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

    def get_phone_value(self):
        return self.driver.find_element(*self.PHONE_INPUT_LOCATOR).get_attribute("value")

    def open_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()


    def click_add_card(self):
        self.driver.find_element(*self.ADD_CARD_LOCATOR).click()

    def enter_card_number(self, number):
        self.driver.find_element(*self.CARD_NUMBER_LOCATOR).send_keys(number)

    def enter_card_cvv(self, cvv):
        self.driver.find_element(*self.CARD_CVV_LOCATOR).send_keys(cvv)

    def blur_card_form(self):
        self.driver.find_element(*self.CARD_CVV_LOCATOR).send_keys("\t")

    def click_link(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.LINK_BUTTON_LOCATOR)
        ).click()

    def get_payment_method_text(self):
        return self.driver.find_element(*self.PAYMENT_TEXT_LOCATOR).text