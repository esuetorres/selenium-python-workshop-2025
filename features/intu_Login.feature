Feature: Login de Intu 
    Scenario: credenciales incorrectas Intu
        Given el usuario se encuentra en la pagina de login de Intu
        When el usuario escribe credenciales erroneas 
        Then aparece un mensaje de error