from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_page_title():
    # Inicializa o driver do Chrome (você pode usar outros browsers como Firefox, Edge, etc.)
    driver = webdriver.Chrome()

    # Abre o site do Google
    driver.get("https://www.google.com")

    # Verifica se o título da página é "Google"
    assert driver.title == "Google"

    # Fecha o navegador
    driver.quit()