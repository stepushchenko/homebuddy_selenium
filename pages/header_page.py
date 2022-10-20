# external imports
from selenium.webdriver.common.by import By
# internal imports
from pages.base_page import BasePage


class HeaderPage(BasePage):
    search_field = (By.XPATH, "//span[contains(text(),'Search')]")
    sign_in_button = (By.XPATH, "//span[contains(text(), 'Sign in')]/following::div")





