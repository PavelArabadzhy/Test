import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='module', autouse=True)
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=Options())
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()