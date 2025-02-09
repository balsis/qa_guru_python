import pytest
from selene import browser, be, have
from selenium import webdriver
import random
import string


def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k = length))


def get_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-webrtc")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/119.0.0.0 Safari/537.36")
    options.add_argument("--window-size=1920,1080")
    return options


@pytest.fixture(autouse = True)
def driver(request):
    browser.config.driver_options = get_options()
    yield
    browser.quit()


class TestGoogleIt:
    def test_google_it(self):
        browser.open('https://google.com')
        browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
        browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser'))

    def test_google_random_string(self):
        browser.open('https://google.com')
        browser.element('[name="q"]').should(be.blank).type(random_string()).press_enter()
        browser.element('p[role="heading"]').should(have.text('ничего не найдено'))
