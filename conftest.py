import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#check parameters for start
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: es or ru")

#fixture for start test
@pytest.fixture(scope="function")
def browser(request):
    #add language
    language = request.config.getoption("language")
    
    #add options for language
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    
    #start browser
    browser = webdriver.Chrome(chrome_options=options)
    
    #quit browser
    yield browser
    browser.quit()