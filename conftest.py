import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: es or ru")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print("\nStart browser..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(chrome_options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()