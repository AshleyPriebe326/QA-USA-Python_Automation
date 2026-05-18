import data
import helpers

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import UrbanRoutesPage

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert urban_routes_page.get_from_location() == data.ADDRESS_FROM
        assert urban_routes_page.get_to_location() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_supportive_button()
        if not urban_routes_page.is_supportive_selected():
            urban_routes_page.click_supportive_button()

        assert urban_routes_page.is_supportive_selected()

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_supportive_button()
        # Open phone form
        urban_routes_page.click_phone_field()
        # Enter phone
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        # Click Next
        urban_routes_page.click_next()
        # Get SMS code (IMPORTANT requirement)
        from helpers import retrieve_phone_code
        code = retrieve_phone_code(self.driver)
        # Enter SMS code
        urban_routes_page.enter_sms_code(code)
        # Confirm
        urban_routes_page.click_confirm()
        # Assert phone is saved
        assert urban_routes_page.get_phone_value() == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(
            data.ADDRESS_FROM,
            data.ADDRESS_TO
        )
        urban_routes_page.click_supportive_button()
        urban_routes_page.open_payment_method()
        urban_routes_page.click_add_card()
        # Enter card details
        urban_routes_page.enter_card_number(data.CARD_NUMBER)
        urban_routes_page.enter_card_cvv(data.CARD_CODE)
        # IMPORTANT: remove focus so Link becomes active
        urban_routes_page.blur_card_form()
        # Click Link
        urban_routes_page.click_link()
        # Assert payment method changed
        assert urban_routes_page.get_payment_method_text() == "Card"

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_supportive_button()
        urban_routes_page.enter_comment(data.MESSAGE_FOR_DRIVER)
        assert (urban_routes_page.get_comment_value()
                == data.MESSAGE_FOR_DRIVER)

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()