from behave import given, when, then
from selenium import webdriver
from pages.ML_search_page import MercadoLibreSearch
from pages.result_ML_search_page import MercadoLibreSearchResult

@given('el usuario se encuentra en la pagina de busqueda de mercado libre')
def step_given_homepage(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.mercadolibre.com.co')
    context.driver.maximize_window()
    context.search_page = MercadoLibreSearch(context.driver)
    context.result_ML_search_page = MercadoLibreSearchResult(context.driver)

@when('el busca iphone 13 en la barra de busqueda')
def step_when_search_product(context):
    context.search_page.search()

@then('aparece un resultado que diga iphone 13')
def step_then_verify_results(context):
    assert "iphone 13" in context.result_ML_search_page.isElementPresent().lower()
    
    