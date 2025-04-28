from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class MercadoLibreSearch(BasePage):
    SEARCH_FIELD = (By.CLASS_NAME, 'nav-search-input')
    SEARCH_BUTTON = (By.CLASS_NAME, 'nav-search-btn')
    
    def search(self):
        self.enter_text(self.SEARCH_FIELD, 'iphone 13')
        self.click(self.SEARCH_BUTTON)


  