from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class MercadoLibreSearchResult(BasePage):
    RESULT_SEARCH = (By.XPATH, '/html/body/main/div/div[2]/section/div[7]/ol/li[1]/div/div/div/div[2]/h3/a')
    
    def isElementPresent(self):
        elemento = self.find_element(self.RESULT_SEARCH)
        texto = elemento.text
        print(texto)
        return texto