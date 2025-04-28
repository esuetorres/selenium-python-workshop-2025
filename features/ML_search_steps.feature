Feature: Busqueda MELI
    Scenario: busqueda de iphone 13
        Given el usuario se encuentra en la pagina de busqueda de mercado libre
        When el busca iphone 13 en la barra de busqueda
        Then aparece un resultado que diga iphone 13